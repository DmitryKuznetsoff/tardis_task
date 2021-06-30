from flask import Flask
import redis


def init_redis():
    pool = redis.ConnectionPool(host='redis', port=6379)
    return redis.Redis(connection_pool=pool)


app = Flask(__name__)
