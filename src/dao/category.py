from app.models import CoffeeCategory
from dto.coffee import CoffeeCategorySchema
from django.shortcuts import get_list_or_404

class CoffeeCategoryDAO:
    def __init__(self):
        pass
    
    def find_all(self,):
        objects = get_list_or_404(CoffeeCategory)
        return [CoffeeCategorySchema.model_validate(obj) for obj in objects]