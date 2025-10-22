from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .user import User


class CoffeeProduct(models.Model):
    # Основная информация
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    # Бренд и производитель
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, verbose_name="Бренд")

    # Категории
    CATEGORY_CHOICES = [
        ("freeze_dried", "Сублимированный"),
        ("spray_dried", "Распылительной сушки"),
        ("microground", "Микромолотый"),
        ("capsules", "Капсулы"),
        ("sticks", "Стики"),
    ]
    category = models.ForeignKey("CoffeeCategory", on_delete=models.CASCADE)

    # Характеристики кофе
    ROAST_LEVEL_CHOICES = [
        ("light", "Светлая"),
        ("medium", "Средняя"),
        ("dark", "Тёмная"),
    ]
    roast_level = models.CharField(
        max_length=10, choices=ROAST_LEVEL_CHOICES, verbose_name="Обжарка"
    )

    ACIDITY_LEVEL_CHOICES = [
        ("low", "Низкая"),
        ("medium", "Средняя"),
        ("high", "Высокая"),
    ]
    acidity_level = models.CharField(
        max_length=10, choices=ACIDITY_LEVEL_CHOICES, verbose_name="Кислотность"
    )

    # Упаковка
    net_weight = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="Вес нетто (г)"
    )
    package_type = models.CharField(
        max_length=50, verbose_name="Тип упаковки"
    )  # банка, пачка, стики

    # Цена и наличие
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    old_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Старая цена",
    )
    stock_quantity = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Количество на складе",
    )
    is_available = models.BooleanField(default=True, verbose_name="Доступен")

    # SEO и метаданные
    meta_title = models.CharField(max_length=200, blank=True, verbose_name="Meta Title")
    meta_description = models.TextField(blank=True, verbose_name="Meta Description")

    # Даты
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class CoffeeCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название бренда")
    description = models.TextField(blank=True, verbose_name="Описание бренда")
    logo = models.ImageField(upload_to="brands/", blank=True, verbose_name="Логотип")
    country = models.CharField(max_length=50, verbose_name="Страна происхождения")

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    def __str__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = [
        (1, "1 - Ужасно"),
        (2, "2 - Плохо"),
        (3, "3 - Нормально"),
        (4, "4 - Хорошо"),
        (5, "5 - Отлично"),
    ]

    product = models.ForeignKey(
        CoffeeProduct,
        related_name="reviews",
        on_delete=models.CASCADE,
        verbose_name="Продукт",
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    rating = models.IntegerField(choices=RATING_CHOICES, verbose_name="Рейтинг")
    comment = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_approved = models.BooleanField(default=False, verbose_name="Одобрен")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        unique_together = ["product", "user"]  # Один отзыв на товар от пользователя
        ordering = ["-created_at"]

    def __str__(self):
        return f"Отзыв от {self.user} на {self.product}"


class CoffeeProductImage(models.Model):
    image = models.ImageField(
        upload_to="products/", verbose_name="Основное изображение"
    )
    index = models.PositiveIntegerField(unique=True)

    class Meta:
        ordering = [
            "index",
        ]
