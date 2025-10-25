from django.http import HttpRequest
from ninja_extra import api_controller, paginate, route
from ninja_extra.pagination import PageNumberPaginationExtra,PaginatedResponseSchema
from ninja_extra.security import django_auth
from injector import inject
from dao.coffee import CoffeeDAO
from dto.coffee import CoffeeCreateSchema, CoffeeSchema


@api_controller("/v1/coffees", tags=["Coffee"], auth=django_auth)
class CoffeeController:
    @inject
    def __init__(self, coffee_dao: CoffeeDAO):
        self.coffee_dao = coffee_dao

    @route.get("/", response=PaginatedResponseSchema[CoffeeSchema], auth=None)
    @paginate(PageNumberPaginationExtra, page_size=10)
    def list_Coffees(self, request: HttpRequest,):
        return self.coffee_dao.find_all()

    @route.post('/', response=CoffeeSchema)
    def create_coffee(self, request: HttpRequest, data: CoffeeCreateSchema):
        return self.coffee_dao.create()