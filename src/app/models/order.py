from django.db import models
from .user import User
from .coffee import CoffeeProduct


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ("pending", "Ожидает обработки"),
        ("confirmed", "Подтверждён"),
        ("preparing", "Готовится"),
        ("shipped", "Отправлен"),
        ("delivered", "Доставлен"),
        ("cancelled", "Отменён"),
    ]

    PAYMENT_STATUS_CHOICES = [
        ("pending", "Ожидает оплаты"),
        ("paid", "Оплачен"),
        ("failed", "Ошибка оплаты"),
        ("refunded", "Возврат"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    order_number = models.CharField(
        max_length=20, unique=True, verbose_name="Номер заказа"
    )

    # Статусы
    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS_CHOICES,
        default="pending",
        verbose_name="Статус заказа",
    )
    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default="pending",
        verbose_name="Статус оплаты",
    )

    # Адрес доставки
    delivery_address = models.TextField(verbose_name="Адрес доставки")
    phone = models.CharField(max_length=20, verbose_name="Телефон для связи")

    # Стоимость
    subtotal = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Подытог"
    )
    delivery_cost = models.DecimalField(
        max_digits=8, decimal_places=2, default=0, verbose_name="Стоимость доставки"
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Итого")

    # Комментарии
    customer_notes = models.TextField(blank=True, verbose_name="Комментарий клиента")
    admin_notes = models.TextField(blank=True, verbose_name="Заметки администратора")

    # Даты
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Заказ #{self.order_number}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE, verbose_name="Заказ"
    )
    product = models.ForeignKey(
        CoffeeProduct, on_delete=models.CASCADE, verbose_name="Продукт"
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    price = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Цена за единицу"
    )

    class Meta:
        verbose_name = "Элемент заказа"
        verbose_name_plural = "Элементы заказа"

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_total_price(self):
        return self.quantity * self.price
