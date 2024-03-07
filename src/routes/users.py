from flask import jsonify

from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt

from http import HTTPStatus

from src.repositories import RolesRepository
from src.schemas.request.users.users_post_request import UserPostRequest
from src.schemas.request.users.user_get_request import UserGetRequestSchema
from src.schemas.request import UserDeleteRequest
from src.schemas.request import UserPatchRequest, UserQuerySchema
from src.schemas.responses.users.user_response import UserResponse
from src.usecases.users import (
    UsersPostUseCase,
    UserPatchUseCase,
    UserDeleteUseCase,
    UsersGetUseCase
)
from src.repositories.users.users_repository import UserRepository

blue_print = Blueprint("users", __name__, description="Operation on users")


@blue_print.route("/users")
class User(MethodView):

    @blue_print.arguments(UserGetRequestSchema, location="query")
    @blue_print.response(200, UserResponse(many=True))
    def get(self, filters):
        use_case = UsersGetUseCase(UserRepository())
        return use_case.run(filters)

    @blue_print.arguments(UserPostRequest)
    @blue_print.response(201, UserResponse)
    def post(self, user_data):
        use_case = UsersPostUseCase(UserRepository(), RolesRepository())
        return use_case.run(user_data)

    @blue_print.arguments(UserPatchRequest, location="json")
    @blue_print.arguments(UserQuerySchema, location="query")
    @blue_print.response(201, UserResponse)
    def patch(self, user_data, query):
        user_data["users"] |= query
        use_case = UserPatchUseCase(UserRepository())
        return use_case.run(user_data["users"])

    @blue_print.arguments(UserDeleteRequest, location="query")
    @blue_print.response(HTTPStatus.NO_CONTENT)
    def delete(self, user_data):
        use_case = UserDeleteUseCase(UserRepository())
        use_case.run(user_data)


@blue_print.route("/users/profile")
class UserProfile(MethodView):

    @blue_print.response(HTTPStatus.OK, UserResponse)
    @jwt_required()
    def get(self):
        current_user = get_jwt()
        return jsonify(current_user), 200

