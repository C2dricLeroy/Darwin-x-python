from ..service.user_service import UserService


class UserController:
    def get_user_informations(self, investor_id):
        user_service = UserService()
        return user_service.get_user_informations(investor_id)
