import uuid
from sqlalchemy.dialects.postgresql import UUID
from src.data.postgres.db import db


class RoleModel(db.Model):

    __tablename__ = "roles"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    role_name = db.Column(db.String(length=40), nullable=False, unique=False)
    role_code = db.Column(db.String(length=40), nullable=False, unique=False)
    role_description = db.Column(db.String(length=150), nullable=False, unique=False)
    users = db.relationship('UserModel', backref='roles', lazy=True)

    def serialize(self):
        return {
            'id': str(self.id),
            'role_name': self.role_name,
            'role_code': self.role_code,
            'role_description': self.role_description
        }

