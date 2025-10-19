from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from ninja.errors import HttpError
from django.http import HttpRequest
from app.models import User
from dto.user import LoginSchema, UserListSchema, UserDetailSchema


class UserDAO:
    def find_all(self) -> list[UserListSchema]:
        entities = User.objects.all()
        return [UserListSchema.model_validate(entity) for entity in entities]

    def find_one(self, id: int) -> UserDetailSchema:
        entity = get_object_or_404(User.objects.prefetch_related("profile"), pk=id)
        return UserDetailSchema.model_validate(entity)

    def create(self, dto: LoginSchema) -> UserDetailSchema:
        try:
            entity = User.objects.create_user(**dto.model_dump())
            return UserDetailSchema.model_validate(entity)
        except IntegrityError:
            raise HttpError(400, "User with this email already exists.")

    def login(self, request: HttpRequest, dto: LoginSchema) -> UserDetailSchema:
        try:
            entity = authenticate(request, **dto.model_dump())
            if entity is not None:
                login(entity)
                return UserDetailSchema.model_validate(entity)
            else:
                raise HttpError(401, "Authentication failed.")
        except User.DoesNotExist:
            raise HttpError(401, "Invalid credentials.")

    def logout(self, request: HttpRequest) -> None:
        logout(request)
