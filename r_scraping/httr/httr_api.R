# Install and Load the httr packages
if(!require(httr)) install.packages('httr')
if(!require(httr)) install.packages('jsonlite')
if(!require(xml2)) install.packages('xml2')
packageVersion('httr')
packageVersion('jsonlite')
packageVersion('xml2')

# build with
sessionInfo()
# ==============================================================================
# Find the most recent R questions on stackoverflow
r <- GET(
    url = "http://api.stackexchange.com",
    path = "questions",
    query = list(
        site = "stackoverflow.com",
        tagged = "r"
    )
)
# Check the request succeeded
stop_for_status(r)
# Automatically parse the response 
questions = content(r)
questions$items[[1]]$title
# ==========================================
# functions
## Open specified url in browser.
BROWSE("http://had.co.nz")
HEAD("http://www.baidu.com")
headers(HEAD("http://www.baidu.com"))
modify_url(url, 
           scheme = NULL, 
           hostname = NULL, port = NULL,
           path = NULL, 
           query = NULL, 
           params = NULL, 
           fragment = NULL,
           username = NULL, password = NULL)
GET(url = modify_url, 
    query = list(), 
    user_agent(agent),
    add_headers(..., .headers = character()),
    body = list(),
    set_cookies(),
    authenticate(user, password, type = "basic"),
    content_type(type),
    content_type_json(),
    content_type_xml(),
    accept(type),
    accept_json(),
    accept_xml(),
    path = "search",
    verbose(),
    handle,
    timeout(10),
    use_proxy(url, port = NULL, username = NULL, password = NULL,
              auth = "basic")
)
POST(url = modify_url(), query = list(), add_headers(), body = list())


http_type(response)
http_error(response)
httr_dr()
option = httr_options()
curl_docs("CURLOPT_XOAUTH2_BEARER")


status_code(response)
content(response)
headers(response)
cookies(response)


oauth1.0_token()
oauth2.0_access_token()
oauth2.0_authorize_url()
oauth2.0_token()


# resp_XML = GET("http://www.colourlovers.com/api/color/6B4106?format=xml")
# resp_json = GET("http://www.colourlovers.com/api/color/6B4106?foramt=json")
# ==========================================
# First steps
  # Send a simple request
  # Parse the response
  # Return a helpful object
  # Turn API errors into R errors
  # Set a user agent
library(httr)


# Set a user agent
ua = user_agent("http://github.com/hadley/httr")
ua
# Passing parameters
# URL path, URL query arguments, HTTP headers, request body
# URL path
modify_url()
POST(modify_url("https://httpbin/org", path = "/post"))
# Query arguments
GET(url, query = list())
POST(url, query = list())
POST("http://httpbin.org/post", query = list(foo = "bar"))
# HTTP headers
GET(url, add_headers())
POST(url, add_headers())
POST("http://httpbin.org/post", add_headers(foo = "bar"))

# Request body
GET(url, body = list())
POST(url, body = list())
## as form
POST("http://httpbin.org/post", body = list(foo = "bar"), encode = "form")
POST("http://httpbin.org/post", body = list(foo = "bar"), encode = "json")

## as json

github_api = function(path) {
  # Send a simple request
  url = modify_url("https://api.github.com", path = path)
  resp = GET(url, ua)
  
  # Parse the response
  # Return a helpful object
  if (http_type(resp) != "application/json") {
    stop("API did not return json", call. = FALSE)
  }
  parsed = jsonlite::fromJSON(content(resp, "text"), simplifyVector = FALSE)
  
  # Turn API errors into R errors
  if(http_error(resp)) {
    stop(
      sprintf(
        "Github API request failed [%s]\n%s\n<%s>",
        status_code(resp),
        parsed$message,
        parsed$documentation_url
      ),
      call. = FALSE
    )
  }
  structure(
    list(
      content = parsed,
      path = path,
      response = resp
    ),
    class = "github_api"
  )
}

print.github_api = function(x, ...) {
  cat("<Github ", x$path, ">\n", sep = "")
  str(x$content)
  invisible(x)
}

github_api("users/hadley")



# Authentication
# 1.“Basic” authentication: This requires a username and password (or sometimes just a username). This is passed as part of the HTTP request.
GET("http://httpbin.org", authenticate("username", "password"))
# 2.Basic authentication with an API key: An alternative provided by many APIs is an API “key” or “token” which is passed as part of the request. It is better than a username/password combination because it can be regenerated independent of the username and password.

# 3.OAuth: OAuth is a protocol for generating a user- or session-specific authentication token to use in subsequent requests. (An early standard, OAuth 1.0, is not terribly common any more. 
oauth1.0_token()
oauth2.0_token()


github_pat = function() {
  pat = Sys.getenv('GITHUB_PAT')
  if (identical(pat, "")) {
    stop("Please set env var GITHUB_PAT to your github personal access token", call. = FALSE)
  }
  pat
}


# Rate limiting
rate_limit = function() {
  req = github_api("/rate_limit")
  core = req$content$resources$core
  
  reset = as.POSIXct(core$reset, origin = "1970-01-01")
  cat(core$remaining, " / ", core$limit,
      " (Resets at ", strftime(reset, "%H:%M:%S"), ")\n",
      sep = "")
}
rate_limit



