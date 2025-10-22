from django.db import models


class PromoCode(models.Model):
    DISCOUNT_TYPE_CHOICES = [
        ('percentage', 'Процент'),
        ('fixed', 'Фиксированная сумма'),
    ]
    
    code = models.CharField(max_length=50, unique=True, verbose_name="Код")
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_TYPE_CHOICES, verbose_name="Тип скидки")
    discount_value = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Значение скидки")
    min_order_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Минимальная сумма заказа")
    max_uses = models.PositiveIntegerField(default=1, verbose_name="Максимум использований")
    used_count = models.PositiveIntegerField(default=0, verbose_name="Количество использований")
    valid_from = models.DateTimeField(verbose_name="Действует с")
    valid_to = models.DateTimeField(verbose_name="Действует до")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    
    class Meta:
        verbose_name = "Промокод"
        verbose_name_plural = "Промокоды"
    
    def __str__(self):
        return self.code