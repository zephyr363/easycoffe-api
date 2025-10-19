from ninja_extra import NinjaExtraAPI

from .v1.user import UserController
from .v1.profile import ProfileController

api = NinjaExtraAPI()

api.register_controllers(UserController)
api.register_controllers(ProfileController)