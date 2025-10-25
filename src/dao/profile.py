from django.shortcuts import get_object_or_404
from dto.user import ProfileSchema, CreateProfileSchema
from app.models import Profile
from django.db import IntegrityError
from ninja.errors import HttpError

class ProfileDAO:
    def find_all(self) -> list[ProfileSchema]:
        entities = Profile.objects.all()
        return [ProfileSchema.model_validate(entity) for entity in entities]

    def find_one(self, id: int) -> ProfileSchema:
        entity = get_object_or_404(
            Profile.objects.select_related("user", "location"), pk=id
        )
        return ProfileSchema.model_validate(entity)

    def create(self, dto: CreateProfileSchema) -> ProfileSchema:
        try:
            entity = Profile.objects.create(**dto.model_dump())
            return ProfileSchema.model_validate(entity)
        except IntegrityError:
            raise HttpError(400, "Profile with this user already exists.")
        
    