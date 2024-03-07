from sqlalchemy.exc import SQLAlchemyError

from src.data.postgres.models import RoleModel
from src.repositories.roles.roles_repository_base import RolesRepositoryBase


class RolesRepository(RolesRepositoryBase):
    def get_all_roles(self, filters) -> dict:

        pass

    def get_users(self, filters) -> dict:

        pass

    def find_role(self, id) -> dict:
        try:
            user = RoleModel.query.filter(RoleModel.id == id).first()

            return {
                "status": "SUCCESS",
                "data": user
            }

        except SQLAlchemyError as error:
            print(error)
            return {
                "status": "ERROR",
                "id": "XXXX",
            }

    def find_role_by_role_code(self, role_code) -> dict:
        try:
            role = RoleModel.query.filter(RoleModel.role_code == role_code).first()

            return {
                "status": "SUCCESS",
                "data": role
            }

        except SQLAlchemyError as error:
            print(error)
            return {
                "status": "ERROR",
                "id": "XXXXA",
            }
