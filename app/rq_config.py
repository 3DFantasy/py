import multiprocessing
import os
from redis import Redis
from rq import Queue
from rq.worker import RoundRobinWorker
from dotenv import load_dotenv

load_dotenv(override=True)

redis_queue = os.getenv("REDIS_QUEUE")
redis_username = os.getenv("REDIS_USERNAME")
redis_host = os.getenv("REDIS_HOST")
redis_password = os.getenv("REDIS_PASSWORD")
redis_port = int(os.getenv("REDIS_PORT"))

redis_url = f"redis://{redis_username}:{redis_password}@{redis_host}:{redis_port}/0"
redis_conn = Redis.from_url(redis_url)


def init_rq_worker(queue_names: list[str]):
    queues = []
    for queue_name in queue_names:
        queue = Queue(
            queue_name,
            connection=redis_conn,
            default_result_ttl=60,
            default_timeout=1200,
        )
        queues.append(queue)

    worker = RoundRobinWorker(queues, connection=redis_conn)

    worker.work()


def rq_lifespan_start():
    """Start the RQ workers when FastAPI starts and clean up on shutdown."""
    worker_processes: list[multiprocessing.Process] = []
    num_workers = os.getenv("RQ_WORKER_NUMBER")
    num_queues = os.getenv("RQ_QUEUE_NUMBER")
    queue = os.getenv("REDIS_QUEUE")
    queue_names: list[str] = []

    for i in range(int(num_queues)):
        queue_names.append(f"{queue}-{i}")

    for i in range(int(num_workers)):
        worker_process = multiprocessing.Process(
            target=init_rq_worker,
            args=(queue_names,),
            daemon=True,
        )
        worker_process.start()
        worker_processes.append(worker_process)

    return worker_processes


def rq_lifespan_end(worker_processes: list[multiprocessing.Process]):
    print("Shutting down workers...")
    for process in worker_processes:
        process.terminate()
