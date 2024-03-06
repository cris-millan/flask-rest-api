from flask_smorest import abort
from http import HTTPStatus
from src.repositories.users.users_repository_base import UserRepositoryBase
from src.usecases.use_case_base import UseCaseBase


class UserPatchUseCase(UseCaseBase):

    def __init__(self, user_repository: UserRepositoryBase):
        self.user_repository = user_repository

    def run(self, data: dict):
        # Validate that email is not already exist.
        return self._user_update(data)

    def _user_update(self, user_data: dict):

        user = self.user_repository.find_user(user_data["id"])

        if user["status"] == "ERROR":
            return abort(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                message="unexpected error",
                errors={
                    "id": "201-" + user["id"],
                    "details": "unexpected error"
                },
            )

        if user["data"] is None:
            return abort(
                HTTPStatus.UNPROCESSABLE_ENTITY,
                message="User not found",
                errors={
                    "id": "USS-201-000",
                    "details": "users not found"
                },
            )

        user_model = user["data"]
        user_updated = self.user_repository.update_user(user_model, user_data)

        if user_updated["status"] == "ERROR":
            return abort(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                message="unexpected error",
                errors={
                    "id": "201-" + user["id"],
                    "details": "unexpected error"
                },
            )

        if user_updated["data"] is None:
            return abort(
                HTTPStatus.UNPROCESSABLE_ENTITY,
                message="email already in use",
                errors={
                    "id": "USS-201-000",
                    "details": "email already in use"
                },
            )

        return user_updated["data"]

