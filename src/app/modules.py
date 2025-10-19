from anydi import provider

from dao import *

class AppModule:
    @provider(scope='singleton')
    def user_dao(self) -> UserDAO:
        return UserDAO()
    
    