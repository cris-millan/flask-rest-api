from flask import jsonify

from flask.views import MethodView
from flask_smorest import Blueprint

from src.schemas.request import CachePostRequest, CacheGetRequest
from src.usecases.cache import CacheGetUseCase
from src.usecases.cache import CachePostUseCase
from flask_jwt_extended import jwt_required

blue_print = Blueprint("cache", __name__, description="Operation on users")


@jwt_required()
@blue_print.route("/cache")
class Cache(MethodView):
    @blue_print.arguments(CachePostRequest)
    def post(self, data):
        use_case = CachePostUseCase()
        return (
            jsonify(
                use_case.run(data)
            ),
            200
        )

    @blue_print.arguments(CacheGetRequest, location="query")
    def get(self, data):
        use_case = CacheGetUseCase()
        return (
            jsonify(
                use_case.run()
            ),
            200
        )

