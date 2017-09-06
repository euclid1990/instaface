import os
from dotenv import load_dotenv
from app import app, Autoload

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

if __name__ == "__main__":
    Autoload(app).config()
    app.run(host="0.0.0.0", port=4300, debug=app.config['APP'].APP_DEBUG)
