from ninja import ModelSchema
from app.models import *


class CoffeeCategorySchema(ModelSchema):
    class Meta:
        model = CoffeeCategory
        fields = "__all__"


class BrandSchema(ModelSchema):
    class Meta:
        model = Brand
        fields = "__all__"


class CoffeeListSchema(ModelSchema):
    category: CoffeeCategorySchema
    brand: BrandSchema
    class Meta:
        model = CoffeeProduct
        fields = "__all__"
