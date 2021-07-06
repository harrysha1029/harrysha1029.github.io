POST_HTML = """
    <div class="post">
        <div><h2>{title}</h2></div>
        <div></div>

        <div>
            <a id="dec{ind}"> Back  </a> - <a id="inc{ind}"> Forward </a>
        </div>

        <div></div>

        <img class="gallery" id="gallery{ind}" src="{initial_image}" alt="">
        <div class="paragraph" id="paragraph{ind}">
            {initial_text}
        </div>
    </div>
"""

def get_post_html(title, ind, initial_image, initial_text):
    return POST_HTML.format(
        title = title,
        ind = ind,
        initial_image = initial_image,
        initial_text = initial_text
    )

INDEX_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./style.css" type="text/css">
    <link href="https://fonts.googleapis.com/css2?family=Lora&display=swap" rel="stylesheet">
    <title>Harry's Travels</title>
    <script src="./script.js" defer></script>
</head>
<body>
    {posts}
</body>
</html>

"""

def get_index_html(posts):
    return INDEX_HTML.format(
        posts = posts
    )

JS_FUNCTIONS = """
document.getElementById("inc{ind}").addEventListener("click", function(e) {
    e.stopImmediatePropagation();
    increment({ind});
}, false);

document.getElementById("dec{ind}").addEventListener("click", function(e) {
    e.stopImmediatePropagation();
    decrement({ind});
}, false);

document.getElementById("gallery{ind}").addEventListener("click", function(e) {
    e.stopImmediatePropagation();
    increment({ind});
}, false);
"""

def get_js_functions(index):
    return JS_FUNCTIONS.replace("{ind}", str(index))

def get_script_js(funs):
    return SCRIPT_JS.replace(
        "{functions}",funs
    )

SCRIPT_JS = """
var data = [];
var num_posts;
var counters;

function mod(n, m) {
    return ((n % m) + m) % m;
}

function compute_height() {
    gal_width = document.getElementsByClassName("post")[0].clientWidth*0.7;
    return gal_width*2/3;
}

function set_max_heights() {
    var elements = document.getElementsByClassName('gallery');
    console.log("HI");
    height = compute_height();
    for (var i = 0; i < elements.length; i++) {
        elements[i].style["max-height"] = height + 'px';
    }
}

fetch("./data.json")
  .then(response => response.json())
  .then(json => {
      data = json;
      num_posts = data.length;
      counters = new Array(num_posts).fill(0);
      set_max_heights();
});

function increment(index) {
    post_data = data[index];
    counters[index] = mod(counters[index] + 1, post_data.n_images);
    image = post_data.media[counters[index]];
    text = post_data.text[counters[index]];
    document.getElementById("gallery" + index).src = image;
    document.getElementById("paragraph" + index).innerHTML = text;
}
function decrement(index, images) {
    post_data = data[index];
    counters[index] = mod(counters[index] - 1, post_data.n_images);
    image = post_data.media[counters[index]];
    text = post_data.text[counters[index]];
    document.getElementById("gallery" + index).src = image;
    document.getElementById("paragraph" + index).innerHTML = text;
}

window.addEventListener('resize', set_max_heights);

{functions}
"""