from ninja_extra import NinjaExtraAPI

from .v1.user import UserController
from .v1.profile import ProfileController
from .v1.coffee import CoffeeController

api = NinjaExtraAPI(
    title='EasyCoffeeAPI',
    
)

api.register_controllers(UserController, CoffeeController, ProfileController)
