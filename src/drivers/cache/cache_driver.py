from abc import ABC, abstractmethod
import redis
import os

from src.config.files import cache_config


class CacheDriver(ABC):

    @abstractmethod
    def set(self, key, data, **kwargs):
        pass

    @abstractmethod
    def get(self, key, **kwargs):
        pass

    @abstractmethod
    def delete(self, key, **kwargs):
        pass

    @abstractmethod
    def update(self, key, data, **kwargs):
        pass


class RedisCacheDriver(CacheDriver):

    def __init__(self, config: dict = None):
        config = config or cache_config.CACHE_CONFIG["redis"]
        print(config)

        self.cache = redis.StrictRedis(
            host=config["host"],
            port=config["port"],
            db=config["db"],
            decode_responses=config["decode_responses"]
        )

    def set(self, key, data, **kwargs):
        try:
            ex = kwargs.get('ex', None)
            response = self.cache.set(key, data, ex)
        except Exception as ex:
            print("error exception :", ex)
            print("Exception info", type(ex).__name__)

            return {
                "Status": "ERROR",
                "id": "XXX-XXX-XXX",
                "details": type(ex).__name__
            }
        return {
            "status": "SUCCESS",
            "data": response
        }

    def get(self, key, **kwargs):

        try:
            response = self.cache.get(key)
        except Exception as ex:
            print("error exception :", ex)
            print("Exception info", type(ex).__name__)
            return {
                "Status": "ERROR",
                "id": "XXX-XXX-XXX",
                "details": type(ex).__name__
            }

        return {
            "status": "SUCCESS",
            "data": response
        }

    def delete(self, key, **kwargs):
        try:
            response = self.cache.delete(key)
        except Exception as ex:
            print("error exception :", ex)
            print("Exception info", type(ex).__name__)
            return {
                "Status": "ERROR",
                "id": "XXX-XXX-XXX",
                "details": type(ex).__name__
            }
        return {
            "status": "SUCCESS",
            "data": response
        }

    def update(self, key, data, **kwargs):
        try:
            self.cache.delete(key)
            response = self.cache.set(key, data)
        except Exception as ex:
            print("error exception :", ex)
            print("Exception info", type(ex).__name__)
            return {
                "Status": "ERROR",
                "id": "XXX-XXX-XXX",
                "details": type(ex).__name__
            }

        return {
            "status": "SUCCESS",
            "data": response
        }
