import json

POST_PATH = "posts.json"


def load_posts() -> list[dict]:
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_picture(picture) -> str:
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path


def get_posts_by_word(word: str) -> list[dict]:
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def func_add_post(post: dict) -> dict:
    posts = load_posts()
    posts.append(post)
    with open(POST_PATH, 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)
    return posts
