# extensions.py
import redis
import os

from flask import jsonify
from flask_jwt_extended import JWTManager

from src.drivers import CacheDriverFactory


jwt = JWTManager()
jwt_redis_blocklist = CacheDriverFactory.create_driver()
jwt_prefix = "user-session:"


# @jwt.revoked_token_loader


# Callback function to check if a JWT exists in the redis blocklist
@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    token_in_redis = jwt_redis_blocklist.get(jti)

    if token_in_redis is None:
        return (
            jsonify(
                {
                    "message": "Token has been revoked",
                    "error": "token_revoked",
                }
            ),
            401
        )


@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:
        return {"is_admin": True}
    return {"is_admin": False}


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return (
        jsonify(
            {
                "message": "The token has expired",
                "error": "token_expired"
            }
        ),
        401
    )


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return (
        jsonify(
            {
                "message": "Signature verification failed.",
                "error": "invalid_token"
            }
        ),
        401
    )


@jwt.unauthorized_loader
def unauthorized_loader_callback(error):
    return (
        jsonify(
            {
                "message": "request does not contains access token",
                "error": "authorization_required"
            }
        ),
        401
    )

