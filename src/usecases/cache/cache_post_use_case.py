from src.drivers import CacheDriverFactory
from src.usecases.use_case_base import UseCaseBase


class CachePostUseCase(UseCaseBase):

    def __init__(self):
        self.cache_driver = CacheDriverFactory.create_driver()

    def run(self, data):
        return self.set_in_cache(data)

    def set_in_cache(self, data: dict):
        self.cache_driver.set(data["key"], data["data"])

        return {
            "status": "success",
            "data": self.cache_driver.get(data["key"])
        }



