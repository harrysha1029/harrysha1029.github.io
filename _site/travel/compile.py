import os
import json
from pathlib import Path
from typing import Mapping
from travel.templates.templates import *
import dropbox
import argparse

DB_BASE_PATH = Path('/Random_Code/web/website/travel/post_media/')
LOCAL_BASE_PATH_POSTS = Path('travel/posts/')
LOCAL_BASE_PATH_MEDIA = Path('travel/post_media/')
TOKEN_PATH = Path("travel/token.txt")


def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def save_json(path, obj):
    with open(path, 'w') as f:
        return json.dump(obj, f, indent=4)

def get_posts():
    posts = reversed(sorted(os.listdir(LOCAL_BASE_PATH_POSTS)))
    # posts = sorted(os.listdir(LOCAL_BASE_PATH_POSTS)) # TODO option for chronological
    return [f for f in posts if f !='.DS_Store']

def text_dict_to_list(text, n_images):
    text_list = [0 for _ in range(n_images)]
    for k, v in text.items():
        text_list[k-1] = v

    for t in range(1, len(text_list)):
        if text_list[t] == 0:
            text_list[t] = text_list[t-1]

    return text_list

def post_to_links(name, local=False):
    if local:
        return post_to_links_local(name)
    else:
        return post_to_links_db(name)

def sort_links(links):
    return sorted(links, key=lambda x: int(Path(x).stem))

def post_to_links_local(name):
    path = Path(LOCAL_BASE_PATH_MEDIA) / name
    sorted_media = sort_links([str(path / f) for f in os.listdir(path) if 'jpg' in f])
    sorted_media = [x.replace("travel", ".") for x in sorted_media]
    return sorted_media

def post_to_links_db(name):
    with open(TOKEN_PATH, 'r') as f:
        access_token = f.read().strip()

    dbx = dropbox.Dropbox(access_token)
    print('Connected to Dropbox')
    media_folder = str(DB_BASE_PATH / name)
    names = [entry.name for entry in dbx.files_list_folder(media_folder).entries if 'jpg' in entry.name]
    sorted_names = sort_links(names)
    urls = [
        dbx.sharing_create_shared_link(media_folder + "/" + name).url for name in sorted_names
    ]
    return [
        x.replace("dl=0", "raw=1") for x in urls
    ]

def post_to_dict(name, local=False):
    text = load_json(LOCAL_BASE_PATH_POSTS / name)
    title = text.pop("title")
    media_name = text.pop("media_name")
    text = {
        int(k): v for k, v in text.items()
    }
    media = post_to_links(media_name, local)

    n_images = len(media)
    text_list = text_dict_to_list(text, n_images)

    return {
        "title":title,
        # "folder":str(post),
        "media":media,
        "text":text_list,
        "n_images":n_images
    }

def write_data(posts, local=False):
    list_of_posts = [post_to_dict(p, local) for p in posts]
    save_json("travel/data.json", list_of_posts)
    return list_of_posts

def write_html(list_of_posts):
    post_htmls = [
        get_post_html(
            title=p['title']
            , ind=i
            , initial_image = p['media'][0]
            , initial_text = p['text'][0]
        ) for i, p in enumerate(list_of_posts)
    ]

    index_html = get_index_html("\n\n".join(post_htmls))
    with open("travel/index.html", 'w') as f:
        f.write(index_html)
    return index_html

def write_js(posts):
    functions = [
        get_js_functions(ind) for ind in range(len(posts))
    ]
    script = get_script_js("\n\n".join(functions))
    with open("travel/script.js", 'w') as f:
        f.write(script)
    return script


def compile(local=False):
    posts = get_posts()
    list_of_posts = write_data(posts, local)
    write_html(list_of_posts)
    write_js(posts)