from ninja_extra import api_controller, http_get
from ninja_extra.security import django_auth
from django.http import HttpRequest, HttpResponse
import anydi
from dao import UserDAO
from dto.user import LoginSchema


@api_controller("/v1/users", tags=["Users"], auth=django_auth)
class UserController:
    def __init__(self, user_dao: UserDAO = anydi.auto):
        self.user_dao = user_dao

    @http_get("/", auth=None)
    def list_users(self, request: HttpRequest):
        return self.user_dao.find_all()

    @http_get("/{user_id}/", auth=None)
    def get_user(self, request: HttpRequest, user_id: int):
        return self.user_dao.find_one(user_id)

    @http_get("/create/", auth=None)
    def create_user(self, request: HttpRequest, data: LoginSchema):
        return self.user_dao.create(data)

    @http_get("/login/", auth=None)
    def login_user(self, request: HttpRequest, data: LoginSchema):
        return self.user_dao.login(request, data)

    @http_get("/logout/")
    def logout_user(self, request: HttpRequest):
        self.user_dao.logout(request)
        return HttpResponse(status=204)
