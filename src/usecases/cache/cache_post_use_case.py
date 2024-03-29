from http import HTTPStatus

from flask import abort

from src.drivers import CacheDriverFactory
from src.usecases.use_case_base import UseCaseBase


class CachePostUseCase(UseCaseBase):

    def __init__(self):
        self.cache_driver = CacheDriverFactory.create_driver()

    def run(self, data):
        return self.set_in_cache(data)

    def set_in_cache(self, data: dict):

        response = self.cache_driver.set(data["key"], data["value_str"])

        if response["status"] == "ERROR":
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
            "data": {
                data["key"]: self.cache_driver.get(data["key"])["data"]
            }
        }



