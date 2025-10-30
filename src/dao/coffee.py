from app.models import *
from dto.coffee import *
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Q
from typing import Optional

class CoffeeDAO:
    def find_all(
        self,
        search: Optional[str] = None,
        category: Optional[str] = None,
        price_min: Optional[float] = None,
        price_max: Optional[float] = None,
        ordering: Optional[str] = None
    ):
        queryset = CoffeeProduct.objects.select_related('category', 'brand').annotate(
            avg_rating=Avg('reviews__rating')
        )
        
        # Применяем фильтры
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | 
                Q(description__icontains=search) |
                Q(brand__name__icontains=search)
            )
        
        if category:
            queryset = queryset.filter(category__name=category)
        
        if price_min is not None:
            queryset = queryset.filter(price__gte=price_min)
        
        if price_max is not None:
            queryset = queryset.filter(price__lte=price_max)
        
        # Применяем сортировку
        if ordering:
            if ordering.startswith('-'):
                field = ordering[1:]
                if field in ['price', 'avg_rating', 'name']:
                    queryset = queryset.order_by(f'-{field}')
            else:
                if ordering in ['price', 'avg_rating', 'name']:
                    queryset = queryset.order_by(ordering)
        else:
            # Сортировка по умолчанию
            queryset = queryset.order_by('-avg_rating', 'name')
        
        return [CoffeeSchema.model_validate(obj) for obj in queryset]

    def find_one(self, id: int):
        obj = get_object_or_404(
            CoffeeProduct.objects.select_related("brand", "category", "coffee_images"),
            pk=id,
        )
        return CoffeeSchema.model_validate(obj)
    
    def create(self, dto: CoffeeCreateSchema):
        ...