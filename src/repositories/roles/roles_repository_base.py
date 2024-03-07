from abc import ABC, abstractmethod
from src.data.postgres.models.user_model import UserModel


class RolesRepositoryBase(ABC):

    @abstractmethod
    def get_all_roles(self, filters) -> dict:
        pass

    @abstractmethod
    def get_users(self, filters) -> dict:
        pass

    @abstractmethod
    def find_role(self, id) -> dict:
        pass

    def find_role_by_role_code(self, role_code) -> dict:
        pass
