from http import HTTPStatus

from flask_smorest import abort
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity

from passlib.hash import pbkdf2_sha256

from src.repositories import UserRepositoryBase
from src.usecases.use_case_base import UseCaseBase


class AuthPostUseCase(UseCaseBase):

    def __init__(self, user_repository: UserRepositoryBase):
        self.user_repository = user_repository

    def run(self, data):
        return self._create_token(data)

    def _create_token(self, user_data: dict):

        # Validate that email is not already exist.
        user = self.user_repository.find_user_by_email(user_data["email"])

        if user["status"] == "ERROR":
            return abort(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                message="unexpected error",
                errors={
                    "id": "AUT-201-" + user["id"],
                    "details": "unexpected error"
                },
            )

        if user["data"] is None:
            return abort(
                HTTPStatus.UNPROCESSABLE_ENTITY,
                message="user does not exist",
                errors={
                    "id": "AUT-201-000",
                    "details": "user does not exist"
                },
            )

        user = user["data"]

        # validate password

        if pbkdf2_sha256.verify(user_data["password"], user.password):
            additional_claims = {
                "id": user.id,
                "email": user.email,
                "role": None
            }

            access_token = create_access_token(
                identity=user.id,
                fresh=True,
                additional_claims={"user": additional_claims}
            )

            refresh_token = create_refresh_token(identity=user.id)

            return {
                "access_token": access_token,
                "refresh_token": refresh_token
            }

        return abort(
            HTTPStatus.UNPROCESSABLE_ENTITY,
            message="user does not exist",
            errors={
                "id": "AUT-201-000",
                "details": "user does not exist"
            },
        )
