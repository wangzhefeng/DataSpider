# httr

if(!require(httr)) install.packages('httr')
if(!require(jsonlite)) install.packages('jsonlite')
if(!require(xml2)) install.packages('xml2')


#===============================================================================
# An HTTP request consists of the following parts:
#===============================================================================
# 1. HTTP verb (GET, POST, DELETE, etc.)
# 2. The base URL for the API
# 3. The URL path or endpoint
# 4. URL query arguments (e.g., ?foo=bar)
# 5. Optional headers
# 6. An optional request body


# An HTTP GET request example:

# -> GET /repos/hadley/httr HTTP/1.1
# -> Host: api.github.com
# -> Accept: application/vnd.github.v3+json
# -> Authorization: 


#===============================================================================
# An HTTP response consists of the following parts:
#===============================================================================
# 1. An HTTP status code.
# 2. Headers, key-value pairs.
# 3. A body typically consisting of XML, JSON, plain text, HTML, or some kind of binary representation.


# An HTTP response example:

# <- HTTP/1.1 200 OK
# <- Server: GitHub.com
# <- Content-Type: application/json; charset=utf-8
# <- X-RateLimit-Limit: 5000
# <- X-RateLimit-Remaining: 4998
# <- X-RateLimit-Reset: 1459554901
# <- 
# <- {
# <-   "id": 2756403,
# <-   "name": "httr",
# <-   "full_name": "hadley/httr",
# <-   "owner": {
# <-     "login": "hadley",
# <-     "id": 4196,
# <-     "avatar_url": "https://avatars.githubusercontent.com/u/4196?v=3",
# <-     ...
# <-   },
# <-   "private": false,
# <-   "html_url": "https://github.com/hadley/httr",
# <-   "description": "httr: a friendly http package for R",
# <-   "fork": false,
# <-   "url": "https://api.github.com/repos/hadley/httr",
# <-   ...
# <-   "network_count": 1368,
# <-   "subscribers_count": 64
# <- }

#===============================================================================
# Set content-type and accept headers.
#===============================================================================
content_type(type)
content_type_json()
content_type_xml()
accept(type)
accept_json()
accept_xml()

GET("http://httpbin.org/headers", content_type("text/csv"))
GET("http://httpbin.org/headers", content_type("text/json"))
GET("http://httpbin.org/headers", content_type("text/xml"))
GET("http://httpbin.org/headers", content_type(".csv"))
GET("http://httpbin.org/headers", content_type(".json"))
GET("http://httpbin.org/headers", content_type(".xml"))
GET("http://httpbin.org/headers", content_type_json())
GET("http://httpbin.org/headers", content_type_xml())

GET("http://httpbin.org/headers", accept("text/csv"))
GET("http://httpbin.org/headers", accept("text/json"))
GET("http://httpbin.org/headers", accept("text/xml"))
GET("http://httpbin.org/headers", accept(".csv"))
GET("http://httpbin.org/headers", accept(".json"))
GET("http://httpbin.org/headers", accept(".xml"))
GET("http://httpbin.org/headers", accept_xml())
GET("http://httpbin.org/headers", accept_json())

#===============================================================================
# response header
#===============================================================================
HEAD(url)
headers(response) == HEAD(url)$headers

#===============================================================================
# response body
#===============================================================================
http_type(response)
content(response)

# ===============================================================================
github_api = function(path) {
	url = modify_url("https://api.github.com", path = path)
	response = GET(url, accept_json())
	if (http_type(response) != "application/json") {
		stop("API did not return json", call. = FALSE)
	}
	response_content = response.content()
	return response, response_content
}


response = github_api(path = "/repos/hadley/httr")
response
