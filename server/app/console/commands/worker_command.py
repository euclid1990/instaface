from app import app
from redis import Redis
from rq import Worker, Queue, Connection

class WorkerCommand(object):
    @classmethod
    def run(cls):
        redis_host = app.config['REDIS_HOST']
        redis_port = app.config['REDIS_PORT']
        redis_password = app.config['REDIS_PASSWORD']

        # Listening for work on high, normal, low
        listen = ['high', 'default', 'low']

        # Tell RQ what Redis connection to use
        conn = Redis(host=redis_host, port=redis_port, db=0, password=redis_password)

        with Connection(conn):
            # Workers will read jobs from the given queues
            worker = Worker(map(Queue, listen))
            worker.work()
