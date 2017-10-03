# Prevented from writing .pyc or .pyo files and __pycache__ folders
import sys; sys.dont_write_bytecode = True

from app import app

if __name__ == "__main__":
    app.run(host=app.config['APP'].APP_HOST, port=int(app.config['APP'].APP_PORT), debug=app.config['APP'].APP_DEBUG)
