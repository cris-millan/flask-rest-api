import os

from src.drivers.cache.cache_driver import RedisCacheDriver, CacheDriver


class CacheDriverFactory:

    @staticmethod
    def create_driver(driver_name: str = None) -> CacheDriver:
        driver_name = driver_name or os.getenv("CACHE_DRIVER_NAME", "redis")

        if driver_name == "redis":
            print("create Redis driver")
            return RedisCacheDriver()
        elif driver_name == "B":
            raise ValueError("No implemented")
        else:
            raise ValueError("Invalid driver type")
