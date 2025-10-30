from django.db import models
from .profile import Profile
from .coffee import CoffeeProduct


class Cart(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, verbose_name="Профиль"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return f"Корзина {self.user}"

class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, related_name="items", on_delete=models.CASCADE, verbose_name="Корзина"
    )
    product = models.ForeignKey(
        CoffeeProduct, on_delete=models.CASCADE, verbose_name="Продукт"
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    class Meta:
        verbose_name = "Элемент корзины"
        verbose_name_plural = "Элементы корзины"
        unique_together = ["cart", "product"]

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
