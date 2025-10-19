from ninja_extra import api_controller, http_get
import anydi
from dao import ProfileDAO


@api_controller("/v1/profiles", tags=["Profiles"])
class ProfileController:
    def __init__(self, profile_dao: ProfileDAO = anydi.auto):
        self.profile_dao = profile_dao

    @http_get("/")
    def list_profiles(self, request):
        return self.profile_dao.find_all()

    @http_get("/{profile_id}/")
    def get_profile(self, request, profile_id: int):
        return self.profile_dao.find_one(profile_id)

    @http_get("/create/")
    def create_profile(self, request):
        return self.profile_dao.create()

    @http_get("/update/{profile_id}/")
    def update_profile(self, request, profile_id: int):
        return {"message": f"Profile {profile_id} updated"}
