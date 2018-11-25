library(XML)
library(xml2)


# readLines()
url = "http://www.r-datacollection.com/materials/html/fortunes.html"
fortunes = readLines(con = url)

print(fortunes)
typeof(fortunes)
mode(fortunes)
class(fortunes)
length(fortunes)

for(i in fortunes) {
    print(i)
}


# XML::htmlParse()
url = "http://www.r-datacollection.com/materials/html/fortunes.html"
parsed_fortunes = XML::htmlParse(file = url)
print(parsed_fortunes)
typeof(parsed_fortunes)
mode(parsed_fortunes)
class(parsed_fortunes)


h1 = list("body" = function(x){NULL})
parsed_fortunes = XML::htmlTreeParse(file = url, handlers = h1, asTree = TRUE)
print(parsed_fortunes)
parsed_fortunes$file
parsed_fortunes$version
parsed_fortunes$children


# h = list(
#     startELement = function(node, ...) {
#         name = xmlName(node)
#         if(name %in% c("div", "title")) {
#             NULL
#         } else {node}
#     },
#     comment = function(node) {NULL},
#     text = function(node) {NULL},
#     cdata = function(node) {NULL},
#     processingInstruction = function(node) {NULL},
#     namespace = function(node) {NULL},
#     entity = function(node) {NULL}
# )
# parsed_tree = XML::htmlTreeParse(file = url, handlers = h, asTree = TRUE)


getItalics = function() {
    i_container = character()
    list(
        i = function(node, ...) {
            i_container <<- c(i_container, xmlValue(node))
            },
        returnI = function() i_container
    )
}
h = getItalics()
invisible(htmlTreeParse(file = url, handlers = h))
h$returnI
