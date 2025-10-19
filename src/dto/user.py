from typing import Optional
from ninja import ModelSchema, Schema
from django.utils.module_loading import import_string as importString


class LoginSchema(Schema):
    email: str
    password: str


class UserListSchema(ModelSchema):
    class Config:
        model = importString("app.models.User")
        model_fields = "__all__"
        exclude = ["password"]


class LocationSchema(ModelSchema):
    class Config:
        model = importString("app.models.Location")
        model_fields = "__all__"
        exclude = ["lprofile"]


class ProfileListSchema(ModelSchema):
    user: UserListSchema

    class Config:
        model = importString("app.models.Profile")
        model_fields = "__all__"


class UserDetailSchema(UserListSchema):
    profile: Optional[ProfileListSchema] = None

class ProfileDetailSchema(ModelSchema):
    user: UserListSchema
    location: Optional[LocationSchema] = None

    class Config:
        model = importString("app.models.Profile")
        model_fields = "__all__"
        

class CreateProfileSchema(Schema):
    user_id: int
    phone_number: str
    photo: Optional[str] = None
    full_name: Optional[str] = None
    birth_date: Optional[str] = None