from django.db import models
from .user import User


class Location(models.Model):
    profile = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="location"
    )
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )

    def __str__(self):
        return f"Location of {self.user.email}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=400, null=False, blank=False)
    phone_number = models.CharField(max_length=12, null=False, blank=False)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)
    Location = models.OneToOneField(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="lprofile",
    )

    def __str__(self):
        return f"{self.user.email}"
