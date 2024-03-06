from flask_smorest import abort
from http import HTTPStatus
from src.repositories.users.users_repository_base import UserRepositoryBase
from src.usecases.use_case_base import UseCaseBase


class UserDeleteUseCase(UseCaseBase):

    def __init__(self, user_repository: UserRepositoryBase):
        self.user_repository = user_repository

    def run(self, user_data: dict):
        return self.delete_user(user_data["id"])

    def delete_user(self, user_id) -> dict:
        user = self.user_repository.find_user(user_id)

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
                message="users not found",
                errors={
                    "id": "USS-201-000",
                    "details": "users not found"
                },
            )

        user_deleted = self.user_repository.delete_user(user_model=user["data"])

        if user_deleted["status"] == "ERROR":
            return abort(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                message="unexpected error",
                errors={
                    "id": "201-" + user["id"],
                    "details": "unexpected error"
                },
            )