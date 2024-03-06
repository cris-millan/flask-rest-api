import uuid
from sqlalchemy.dialects.postgresql import UUID
from src.data.postgres.db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False, unique=False)
    last_name = db.Column(db.String, nullable=False, unique=False)
    phone_number = db.Column(db.String, nullable=True, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False, unique=False)
    is_log_in = db.Column(db.Boolean, nullable=False, default=False)
    is_email_verify = db.Column(db.Boolean, nullable=False, default=False)
    is_phone_verify = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), nullable=True)
    modified_at = db.Column(db.DateTime(timezone=True), onupdate=db.func.now(), nullable=True)
    created_by_id = db.Column(db.String(36), nullable=True)
    modified_by_id = db.Column(db.String(36), nullable=True)
    role_id = db.Column(UUID(as_uuid=True), db.ForeignKey('roles.id'), nullable=False)

    def update_from_dict(self, data):
        """
        Actualiza los campos del usuario utilizando un diccionario de datos.

        :param data: Diccionario de datos con los nuevos valores para los campos del usuario.
        """
        for key, value in data.items():
            setattr(self, key, value)

    def serialize(self):
        return {
            'id': str(self.id),
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone_number': self.phone_number,
            'email': self.email,
            'password': self.password,
            'created_at': self.created_at,
            'modified_at': self.modified_at,
            'created_by_id': self.created_by_id,
            'modified_by_id': self.modified_by_id
        }
