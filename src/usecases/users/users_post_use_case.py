from flask_smorest import abort
from http import HTTPStatus
from passlib.hash import pbkdf2_sha256

from src.repositories import RolesRepositoryBase
from src.repositories.users.users_repository_base import UserRepositoryBase
from src.usecases.use_case_base import UseCaseBase


class UsersPostUseCase(UseCaseBase):

    def __init__(self, user_repository: UserRepositoryBase, role_repository: RolesRepositoryBase):
        self.user_repository = user_repository
        self.role_repository = role_repository

    def run(self, user_data):
        return self._create_user(user_data)

    def _create_user(self, user_data):

        # Validate that email is not already exist.
        print(user_data)
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
                    "id": "USS-201-00",
                    "details": "phone number already in use"
                },
            )

        user_data["password"] = pbkdf2_sha256.hash(user_data["password"])

        # get client role

        client_role = self.role_repository.find_role_by_role_code(role_code="client")

        if client_role["status"] == "ERROR":
            return abort(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                message="unexpected error",
                errors={
                    "id": "201-" + client_role["id"],
                    "details": "unexpected error"
                },
            )

        if client_role["data"] is None:
            return abort(
                HTTPStatus.UNPROCESSABLE_ENTITY,
                message="Role not found",
                errors={
                    "id": "USS-201-000",
                    "details": "Role not found"
                },
            )

        client_role = client_role["data"]
        user_data["role_id"] = client_role.id
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
