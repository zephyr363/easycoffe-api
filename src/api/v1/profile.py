from ninja_extra import api_controller, route
from injector import inject
from dao import ProfileDAO
from dto.user import CreateProfileSchema


@api_controller("/v1/profiles", tags=["Profiles"])
class ProfileController:
    @inject
    def __init__(self, profile_dao: ProfileDAO):
        self.profile_dao = profile_dao

    @route.get("/")
    def list_profiles(self, request):
        return self.profile_dao.find_all()

    @route.get("/{profile_id}/")
    def get_profile(self, request, profile_id: int):
        return self.profile_dao.find_one(profile_id)

    @route.post("/create/")
    def create_profile(self, request, data: CreateProfileSchema):
        return self.profile_dao.create(data)

    @route.patch("/update/{profile_id}/")
    def update_profile(self, request, profile_id: int):
        return {"message": f"Profile {profile_id} updated"}
