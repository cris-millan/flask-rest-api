from datetime import timedelta
from http import HTTPStatus

from flask_smorest import abort
from flask_jwt_extended import get_jwt

from src.config import TOKEN_CONFIG
from src.drivers import CacheDriverFactory
from src.usecases.use_case_base import UseCaseBase


class AuthLogOutPostUseCase(UseCaseBase):
    def __init__(self):
        self.jwt_blocklist = CacheDriverFactory.create_driver()
        self.key_prefix = TOKEN_CONFIG["token_prefix_key"]
        self.access_expires = timedelta(minutes=TOKEN_CONFIG["token_block_expiration"])

    def run(self, data):
        return self._log_out()

    def _log_out(self):
        key = self.key_prefix + get_jwt()["jti"]

        response = self.jwt_blocklist.get(key)

        if response["status"] == "ERROR":
            return abort(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                message="something wrong happen",
                errors={
                    "id": "AUT-201-XXXX",
                    "details": "user does not exist"
                },
            )

        if response["data"] is not None:
            return abort(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                message="The token is already revoked",
                errors={
                    "id": "AUT-201-XXXX",
                    "details": "The token is already revoked"
                },
            )

        response = self.jwt_blocklist.set(key, "", ex=self.access_expires)

        if response["status"] == "ERROR":
            return abort(
                HTTPStatus.UNPROCESSABLE_ENTITY,
                message="user does not exist",
                errors={
                    "id": "AUT-201-000",
                    "details": "user does not exist"
                },
            )

        return {
            "message": "Access token revoked"
        }



