from http import HTTPStatus

from flask import abort

from src.drivers import CacheDriverFactory
from src.usecases.use_case_base import UseCaseBase


class CacheGetUseCase(UseCaseBase):

    def __init__(self):
        self.cache_driver = CacheDriverFactory.create_driver()

    def run(self, data):
        data = self.cache_driver.get(key=data["key"])

        if data["status"] == "ERROR":
            return abort(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                message="unexpected error",
                errors={
                    "id": "201-" + data["id"],
                    "details": "unexpected error"
                },
            )

        return {
            "status": "success",
            "data": data["data"]
        }


