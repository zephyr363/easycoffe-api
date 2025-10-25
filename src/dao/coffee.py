from app.models import *
from dto.coffee import *
from django.shortcuts import get_object_or_404
from django.db.models import Avg

class CoffeeDAO:
    def find_all(self):
        objects = CoffeeProduct.objects.select_related('category', 'brand').annotate(
            avg_rating=Avg('reviews__rating')
        )
        return [CoffeeSchema.model_validate(obj) for obj in objects]

    def find_one(self, id: int):
        obj = get_object_or_404(
            CoffeeProduct.objects.select_related("brand", "category", "coffee_images"),
            pk=id,
        )
        return CoffeeSchema.model_validate(obj)

    def create(self, dto: CoffeeCreateSchema):
        ...