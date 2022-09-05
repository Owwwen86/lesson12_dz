from flask import Flask, request, render_template, send_from_directory
# from functions import ...


# Импортируем блюпринты из их пакетов
from main.views_main import main_blueprint
from loader.views_loader import loader_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# Регистрируем блюпринт main и loader
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(host='127.0.0.2', port=4000)

