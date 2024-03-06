from http import HTTPStatus

from flask_smorest import abort
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity

from passlib.hash import pbkdf2_sha256

from src.usecases.use_case_base import UseCaseBase


class AuthRefreshTokenPostUseCase(UseCaseBase):

    def run(self, data):
        return self._create_refresh_token()

    def _create_refresh_token(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {
            "access_token": new_token,
        }
