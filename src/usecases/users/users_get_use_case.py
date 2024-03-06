from flask_smorest import abort
from http import HTTPStatus
from src.repositories.users.users_repository_base import UserRepositoryBase
from src.usecases.use_case_base import UseCaseBase


class UsersGetUseCase(UseCaseBase):

    def __init__(self, user_repository: UserRepositoryBase) -> None:
        self.user_repository = user_repository

    def run(self, filters: dict):

        users = self.user_repository.get_users(filters)

        if users["status"] == "ERROR":
            return abort(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                message="unexpected error",
                errors={
                    "id": "201-" + users["id"],
                    "details": "unexpected error"
                }
            )

        return users["data"]
