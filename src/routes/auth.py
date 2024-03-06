from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required

from http import HTTPStatus

from src.repositories import UserRepository
from src.schemas.request import AuthPostRequest
from src.usecases.auth.auth_logout_post_use_case import AuthLogOutPostUseCase
from src.usecases.auth.auth_post_use_case import AuthPostUseCase
from src.usecases.auth.auth_refresh_token_use_case import AuthRefreshTokenPostUseCase

blue_print = Blueprint("auth", __name__, description="Operation on auth")


@blue_print.route("/auth")
class Auth(MethodView):

    @blue_print.arguments(AuthPostRequest)
    # @blue_print.response(HTTPStatus.OK, AuthPostRequest)
    def post(self, auth_data):
        use_case = AuthPostUseCase(UserRepository())
        return use_case.run(auth_data)


@blue_print.route("/auth/refresh")
class AuthRefresh(MethodView):

    @jwt_required(refresh=True)
    def post(self):
        use_case = AuthRefreshTokenPostUseCase()
        return use_case.run({})


@blue_print.route("/auth/logout")
class AuthLogout(MethodView):

    @jwt_required(refresh=True)
    @blue_print.response(HTTPStatus.OK)
    def post(self):
        use_case = AuthLogOutPostUseCase()
        return use_case.run({})
