# read the douban movie top250 page source code

# base::readLines
html_lines <- readLines('http://movie.douban.com/top250')
doc <- paste0(html_lines, collapse = '')

# RegExp
library(stringr)
title_lines <- grep('class="title"', html_lines, value = TRUE)
titles <- gsub('.*>(.*?)<.*', '\\1', title_lines, perl = TRUE)
titles

# XPath
library(xml2)
titles <- read_html(doc) %>%
  xml_find_all('.//span[@class="title"]') %>%
  xml_text()
titles

# CSS selector
library(rvest)
title <- read_html(doc) %>%
  html_nodes('.title') %>%
  html_text()
titles



# RCurl::getURL
library(RCurl)
html_lines <- RCurl::getURL('http://movie.douban.com/top250')
doc <- paste0(html_lines, collapse = '')

# httr::GET
library(httr)
html_lines <- httr::GET('http://movie.douban.com/top250')
doc <- paste0(html_lines, collapse = '')

# xml2
library(xml2)
html_lines <- xml2::read_html('http://movie.douban.com/top250')
doc <- paste0(html_lines, collapse = '')






