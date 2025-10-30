from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .profile import Profile


class CoffeeProduct(models.Model):
    # Категории
    ACIDITY_LEVEL_CHOICES = [
        ("low", "Низкая"),
        ("medium", "Средняя"),
        ("high", "Высокая"),
    ]
    ROAST_LEVEL_CHOICES = [
        ("light", "Светлая"),
        ("medium", "Средняя"),
        ("dark", "Тёмная"),
    ]
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    category = models.ForeignKey(
        "CoffeeCategory", on_delete=models.CASCADE, verbose_name="Категория"
    )
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, verbose_name="Бренд")
    roast_level = models.CharField(
        max_length=10, choices=ROAST_LEVEL_CHOICES, verbose_name="Обжарка"
    )
    acidity_level = models.CharField(
        max_length=10, choices=ACIDITY_LEVEL_CHOICES, verbose_name="Кислотность"
    )
    net_weight = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="Вес нетто (г)"
    )
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    stock_quantity = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Количество на складе",
    )
    is_available = models.BooleanField(default=True, verbose_name="Доступен")
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

    class Meta:
        verbose_name = "Категория кофе"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название бренда")
    description = models.TextField(blank=True, verbose_name="Описание бренда")
    logo = models.ImageField(upload_to="brands/", blank=True, verbose_name="Логотип")
    country = models.CharField(max_length=50, verbose_name="Страна происхождения")

    owner = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
    )

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
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        verbose_name="Профиль",
        related_name="author_reviews",
    )
    rating = models.IntegerField(choices=RATING_CHOICES, verbose_name="Рейтинг")
    comment = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_approved = models.BooleanField(default=False, verbose_name="Одобрен")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        unique_together = ["product", "author"]  # Один отзыв на товар от пользователя
        ordering = ["-created_at"]

    def __str__(self):
        return f"Отзыв от {self.author.user.email} на {self.product}"


class CoffeeProductImage(models.Model):
    coffee = models.ForeignKey(
        CoffeeProduct, on_delete=models.CASCADE, related_name="coffee_images"
    )
    image = models.ImageField(
        upload_to="products/", verbose_name="Основное изображение"
    )
    index = models.PositiveIntegerField(unique=True)

    class Meta:
        ordering = [
            "index",
        ]
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return self.coffee.name