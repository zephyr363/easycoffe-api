from django.contrib import admin
from app.models import *

admin.site.site_header = "EasyCoffee"


@admin.register(User)
class UserAdminModel(admin.ModelAdmin):
    list_display = ('email', 'is_active')


@admin.register(Profile)
class ProfileAdminModel(admin.ModelAdmin):
    pass


@admin.register(CoffeeProduct)
class CoffeeProductAdminModel(admin.ModelAdmin):
    pass


@admin.register(CoffeeCategory)
class CoffeeCategoryAdminModel(admin.ModelAdmin):
    pass


@admin.register(Brand)
class CoffeeBrandAdminModel(admin.ModelAdmin):
    pass

@admin.register(CoffeeProductImage)
class CoffeeImageAdminModel(admin.ModelAdmin):
    pass

@admin.register(Review)
class CoffeeReviewAdminModel(admin.ModelAdmin):
    pass