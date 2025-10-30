from django.http import HttpRequest
from ninja_extra import api_controller, paginate, route
from ninja_extra.pagination import PageNumberPaginationExtra, PaginatedResponseSchema
from ninja_extra.security import django_auth
from ninja import Query
from typing import Optional
from injector import inject
from dao import CoffeeDAO, CoffeeCategoryDAO 
from dto.coffee import CoffeeCreateSchema, CoffeeSchema, CoffeeCategorySchema


@api_controller("/v1/coffees", tags=["Coffee"], auth=django_auth)
class CoffeeController:
    @inject
    def __init__(self, coffee_dao: CoffeeDAO, category_dao: CoffeeCategoryDAO):
        self.coffee_dao = coffee_dao
        self.category_dao = category_dao

    @route.get("/", response=PaginatedResponseSchema[CoffeeSchema], auth=None)
    @paginate(PageNumberPaginationExtra, page_size=12)  # Увеличил page_size для лучшего UX
    def list_coffees(
        self, 
        request: HttpRequest,
        search: Optional[str] = None,
        category: Optional[str] = None,
        price_min: Optional[float] = None,
        price_max: Optional[float] = None,
        ordering: Optional[str] = None
    ):
        return self.coffee_dao.find_all(
            search=search,
            category=category,
            price_min=price_min,
            price_max=price_max,
            ordering=ordering
        )

    @route.get('/categories', response=PaginatedResponseSchema[CoffeeCategorySchema], auth=None)
    @paginate(PageNumberPaginationExtra, page_size=50)  # Увеличил для всех категорий
    def list_coffee_categories(self, request: HttpRequest):
        return self.category_dao.find_all()
    
    @route.post('/', response=CoffeeSchema)
    def create_coffee(self, request: HttpRequest, data: CoffeeCreateSchema):
        return self.coffee_dao.create()