import os

TOKEN_CONFIG = {
    "token_prefix_key": os.getenv("TOKEN_PREFIX_KEY", "user-auth:"),
    "token_block_expiration": int(os.getenv("TOKEN_BLOCK_EXPIRATION_MIN", 60)),
    "token_live": int(os.getenv("TOKEN_LIVE_MIN", 60)),
    "fresh_token_live": int(os.getenv("FRESH_TOKEN_LIVE_MIN", 1480))
}
