from map_server import app as map_app
from scheduler import app as sched_app

if __name__ == "__main__":
    map_app.run(port=7001)
    sched_app.run(port=7002)
