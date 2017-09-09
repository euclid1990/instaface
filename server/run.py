from app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4300, debug=app.config['APP'].APP_DEBUG)
