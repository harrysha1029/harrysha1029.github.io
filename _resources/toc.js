var ToC =
  "<nav role='navigation' id='toc' class='table-of-contents'>" +
    "<h4 id='hi'>Table of Contents</h2>" +
    "<ul>";

var newLine, el, title, link, this_level;
var level = 0;

$("h2, h3").each(function() {
  el = $(this);
  this_level = el.prop("nodeName") == 'H3' ? 1 : 0
  title = el.text();
  link = "#" + el.attr("id");
  newLine = 
        "<li>" +
        "<a href='" + link + "'>" +
            title +
        "</a>" +
        "</li>";
  if ((level == 0) && (this_level == 1)) {
    newLine = 
        "<ul>" + newLine
  }
  if ((level == 1) && (this_level == 0)) {
    newLine =
        "</ul>" +
        newLine
  }
  if (title !='HS') {
    ToC += newLine;
  }
  level = this_level;

});

ToC +=
   "</ul>" +
  "</nav>";

$(".sidebar").prepend(ToC);
// $(window).scroll(function() { 
//     $("#hi").css('top', $(this).scrollTop());
// });