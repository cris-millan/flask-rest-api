from sqlalchemy.exc import SQLAlchemyError

from src.data.postgres.db import db
from src.data.postgres.models import UserModel
from src.repositories.users.users_repository_base import UserRepositoryBase
import logging


class UserRepository(UserRepositoryBase):

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_all_users(self) -> dict:

        try:
            users = UserModel.query.all()
            return {
                "status": "SUCCESS",
                "data": users
            }

        except SQLAlchemyError as error:
            self.logger.error(error)
            return {
                "status": "ERROR",
                "id": "XXXX",
            }

    def get_users(self, filters: dict) -> dict:
        try:
            # Comenzar con una query que selecciona todos los registros
            query = UserModel.query

            # Aplicar filtros dinámicamente
            for field, value in filters.items():
                # Asumiendo que los campos en el modelo tienen el mismo nombre que los campos en filters
                field_filter = getattr(UserModel, field, None)

                if field_filter is not None:
                    # Aplicar filtro parcial utilizando ilike para cadenas
                    if isinstance(value, str):
                        query = query.filter(field_filter.ilike(f"%{value}%"))
                    else:
                        # Para otros tipos de datos, usar la igualdad normal
                        query = query.filter(field_filter == value)

            # Ejecutar la query y obtener los resultados
            users = query.all()

            print(users)

            return {
                "status": "SUCCESS",
                "data": users
            }

        except SQLAlchemyError as error:
            self.logger.error(error)
            return {
                "status": "ERROR",
                "id": "XXXX",
            }

    def find_user(self, id: str) -> dict:

        try:
            user = UserModel.query.filter(UserModel.id == id).first()
            return {
                "status": "SUCCESS",
                "data": user
            }

        except SQLAlchemyError as error:
            print(error)
            self.logger.error(error)
            return {
                "status": "ERROR",
                "id": "XXXX",
            }

    def find_user_by_email(self, email: str) -> dict:
        try:
            user = UserModel.query.filter(UserModel.email == email).first()
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

    def find_user_by_phone(self, phone_number: str) -> dict:
        try:
            user = UserModel.query.filter(UserModel.phone_number == phone_number).first()
            return {
                "status": "SUCCESS",
                "data": user
            }
        except SQLAlchemyError as error:
            self.logger.error(error)
            return {
                "status": "ERROR",
                "id": "XXXX",
            }

    def create_user(self, user_data) -> dict:
        user = UserModel(**user_data)

        try:
            db.session.add(user)
            db.session.commit()
            return {
                "status": "SUCCESS",
                "data": user
            }
        except SQLAlchemyError as error:
            db.session.rollback()
            self.logger.error(error)
            return {
                "status": "ERROR",
                "id": "XXXX",
            }

    def update_user(self, user: UserModel, user_data: dict) -> dict:
        try:
            user.update_from_dict(user_data)
            db.session.commit()

            return {
                "data": user,
                "status": "SUCCESS",
            }
        except SQLAlchemyError as error:
            db.session.rollback()
            self.logger.error(error)
            return {
                "status": "ERROR",
                "id": "XXXX",
            }

    def delete_user(self, **kwargs) -> dict:
        user = None

        if kwargs.get('user_id') is not None:
            try:
                user = UserModel.query.filter(UserModel.id == kwargs.get('user_id')).first()

            except SQLAlchemyError as error:
                self.logger.error(error)
                return {
                    "status": "ERROR",
                    "id": "XXXX",
                }

        if kwargs.get('user_model') is not None:
            user = kwargs.get('user_model')

        try:
            db.session.delete(user)
            db.session.commit()
            return {
                "status": "SUCCESS",
            }
        except SQLAlchemyError as error:
            db.session.rollback()
            self.logger.error(error)
            return {
                "status": "ERROR",
                "id": "XXXX",
            }
