
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


document.getElementById("inc0").addEventListener("click", function(e) {
    e.stopImmediatePropagation();
    increment(0);
}, false);

document.getElementById("dec0").addEventListener("click", function(e) {
    e.stopImmediatePropagation();
    decrement(0);
}, false);

document.getElementById("gallery0").addEventListener("click", function(e) {
    e.stopImmediatePropagation();
    increment(0);
}, false);



document.getElementById("inc1").addEventListener("click", function(e) {
    e.stopImmediatePropagation();
    increment(1);
}, false);

document.getElementById("dec1").addEventListener("click", function(e) {
    e.stopImmediatePropagation();
    decrement(1);
}, false);

document.getElementById("gallery1").addEventListener("click", function(e) {
    e.stopImmediatePropagation();
    increment(1);
}, false);



document.getElementById("inc2").addEventListener("click", function(e) {
    e.stopImmediatePropagation();
    increment(2);
}, false);

document.getElementById("dec2").addEventListener("click", function(e) {
    e.stopImmediatePropagation();
    decrement(2);
}, false);

document.getElementById("gallery2").addEventListener("click", function(e) {
    e.stopImmediatePropagation();
    increment(2);
}, false);

