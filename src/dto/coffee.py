from typing import List, Optional
from ninja import ModelSchema, Schema
from app.models import *
from .user import UserSchema, ProfileSchema


class CoffeeCategorySchema(ModelSchema):
    class Meta:
        model = CoffeeCategory
        fields = "__all__"


class BrandSchema(ModelSchema):
    owner: ProfileSchema

    class Meta:
        model = Brand
        fields = "__all__"


class CoffeeImageSchema(ModelSchema):
    class Meta:
        model = CoffeeProductImage
        fields = "__all__"
        exclude = ["coffee"]


class CoffeeSchema(ModelSchema):
    category: CoffeeCategorySchema
    brand: BrandSchema
    coffee_images: Optional[List[CoffeeImageSchema]] = None
    avg_rating: Optional[float] = None

    class Meta:
        model = CoffeeProduct
        fields = "__all__"


class ReviewSchema(ModelSchema):
    product: CoffeeSchema
    user: UserSchema

    class Meta:
        model = Review
        fields = "__all__"


class CoffeeCreateSchema(ModelSchema):
    brand_id: int
    category_id: int

    class Meta:
        model = CoffeeProduct
        fields = [
            "name",
            "description",
            "price",
            "stock_quantity",
            "roast_level",
            "acidity_level",
            "net_weight",
        ]
