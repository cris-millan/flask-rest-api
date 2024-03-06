from flask import jsonify

from flask.views import MethodView
from flask_smorest import Blueprint

from src.usecases.cache.cache_post_use_case import CachePostUseCase
from flask_jwt_extended import jwt_required

blue_print = Blueprint("cache", __name__, description="Operation on users")


@blue_print.route("/cache")
class Cache(MethodView):

    @jwt_required()
    def post(self):
        use_case = CachePostUseCase()
        # use_case.run({"key": "Millan", "data": "Cristian Ruben Millan Ruiz"})
        return (
            jsonify(
                use_case.run({"key": "Millan", "data": "Cristian Ruben Millan Ruiz"})
            ),
            200
        )

