from ninja_extra import api_controller, route
from ninja_extra.security import django_auth
from django.http import HttpRequest, HttpResponse
from injector import inject
from dao import UserDAO
from dto.user import LoginSchema


@api_controller("/v1/users", tags=["Users"], auth=django_auth)
class UserController:
    @inject
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    @route.get("/", auth=None)
    def list_users(self, request: HttpRequest):
        return self.user_dao.find_all()

    @route.post("/", auth=None)
    def create_user(self, request: HttpRequest, data: LoginSchema):
        return self.user_dao.create(data)

    @route.post("/login", auth=None)
    def login_user(self, request: HttpRequest, data: LoginSchema):
        return self.user_dao.login(request, data)

    @route.get("/logout")
    def logout_user(self, request: HttpRequest):
        self.user_dao.logout(request)
        return HttpResponse(status=204)

    @route.get("/{user_id}/")
    def get_user(self, request: HttpRequest, user_id: int):
        return self.user_dao.find_one(user_id)

    @route.get("/me/", auth=django_auth)
    def get_me(self, request: HttpRequest):
        return self.user_dao.find_one(request.user.id)
