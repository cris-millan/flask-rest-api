from abc import ABC, abstractmethod
from src.data.postgres.models.user_model import UserModel


class UserRepositoryBase(ABC):
    """

    """

    @abstractmethod
    def get_all_users(self) -> dict:
        """
        get all the users from database

        :return:
        """
        pass

    @abstractmethod
    def get_users(self, filters: dict) -> dict:
        """
        get all the users from database

        :return:
        """
        pass

    @abstractmethod
    def find_user(self, user_id: str) -> dict:
        """

        :param user_id:
        :return:
        """
        pass

    @abstractmethod
    def find_user_by_email(self, email: str) -> dict:
        """
        find a users by users email

        :param email: str
        :return:
        """
        pass

    @abstractmethod
    def find_user_by_phone(self, email: str) -> dict:
        """

        :param email: str
        :return:
        """
        pass

    @abstractmethod
    def create_user(self, user_data) -> dict:
        """

        :param user_data:
        :return:
        """
        pass

    @abstractmethod
    def update_user(self, user_model: UserModel, user_data: dict) -> dict:
        """

        :param user_model:
        :param user_data:
        :return:
        """

    @abstractmethod
    def delete_user(self, **kwargs) -> dict:
        """

        Args:
        **kwargs:
            user_model (UserModel): users model to delete.
            user_id (str): User Id to delete

        :return:
        """

        pass

