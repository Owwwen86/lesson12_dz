from flask import render_template, Blueprint, request

from functions import get_posts_by_word

from json import JSONDecodeError

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates_main')


@main_blueprint.route('/')
def catalog_page():
    return render_template("index.html")


@main_blueprint.route('/search/')
def search_page():
    search_querry = request.args.get('s', '')
    try:
        posts = get_posts_by_word(search_querry)
    except FileNotFoundError:
        return "Файл не найден"
    except JSONDecodeError:
        return 'Невалидный файл'
    return render_template('post_list.html', posts=posts, search_querry=search_querry)
