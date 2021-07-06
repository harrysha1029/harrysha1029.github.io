import markdown2
import argparse
import shutil
import os
from pathlib import Path
import travel.compile


def read_file(path):
    with open("templates/index.html", 'r') as f:
        return f.read()


def update_meta_with_defaults(meta, path):
    if 'template' not in meta:
        meta['template'] = 'templates/index.html'
    if 'name' not in meta:
        meta['out_path'] = f"{str(Path(path).stem)}.html"
    return meta

def render_md(path):
    html = markdown2.markdown_path(path, extras=['code-friendly', 'footnotes', 'header-ids', 'highlightjs-lang', 'metadata', 'fenced-code-blocks'])
    meta = html.metadata
    meta = update_meta_with_defaults(meta, path)
    template = read_file(meta['template'])
    with open(f"_site/" + meta['out_path'], 'w') as f:
        f.write(template.format(content=html))

def render_mds():
    paths = [Path("md") / x for x in os.listdir('md')]
    for p in paths:
        render_md(p)

def compile(local):
    shutil.rmtree('_site')
    os.mkdir("_site")
    render_mds()
    shutil.copytree('imgs', '_site/imgs')
    shutil.copytree('resources', '_site/resources')
    shutil.copy("style.css", '_site/style.css')
    travel.compile.compile(local)
    shutil.copytree('travel', '_site/travel')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l','--local', default=False, action='store_true')
    args = parser.parse_args()

    compile(args.local)

main()
