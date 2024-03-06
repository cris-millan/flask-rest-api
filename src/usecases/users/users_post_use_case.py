from flask_smorest import abort
from http import HTTPStatus
from passlib.hash import pbkdf2_sha256
from src.repositories.users.users_repository_base import UserRepositoryBase
from src.usecases.use_case_base import UseCaseBase


class UsersPostUseCase(UseCaseBase):

    def __init__(self, user_repository: UserRepositoryBase):
        self.user_repository = user_repository

    def run(self, user_data):
        return self._create_user(user_data)

    def _create_user(self, user_data):

        # Validate that email is not already exist.
        user = self.user_repository.find_user_by_email(user_data["email"])

        if user["status"] == "ERROR":
            return abort(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                message="unexpected error",
                errors={
                    "id": "201-" + user["id"],
                    "details": "unexpected error"
                },
            )

        if user["data"]:
            return abort(
                HTTPStatus.UNPROCESSABLE_ENTITY,
                message="email already in use",
                errors={
                    "id": "USS-201-000",
                    "details": "email already in use"
                },
            )

        user = self.user_repository.find_user_by_phone(user_data["phone_number"])

        if user["status"] == "ERROR":
            return abort(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                message="unexpected error",
                errors={
                    "id": "201-" + user["id"],
                    "details": "unexpected error"
                },
            )

        if user["data"]:
            return abort(
                HTTPStatus.UNPROCESSABLE_ENTITY,
                message="phone number already in use",
                errors={
                    "id": "USS-201-000",
                    "details": "phone number already in use"
                },
            )

        user_data["password"] = pbkdf2_sha256.hash(user_data["password"])

        user = self.user_repository.create_user(user_data)

        if user["status"] == "ERROR":
            return abort(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                message="unexpected error",
                errors={
                    "id": "201-" + user["id"],
                    "details": "unexpected error"
                },
            )

        return user["data"]
