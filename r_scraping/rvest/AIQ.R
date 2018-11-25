library(rvest)
library(tidyverse)

doc <- xml2::read_html('http://www.pm25s.com/cn/rank/')
cities <- doc %>% 
  html_nodes('.cityrank a') %>%  # CSS selector
  html_text()

AIQ <- doc %>%
  html_nodes("span[class^='lv']") %>% # Rep Express
  html_text() %>%
  .[c(F, F, T)] %>%
  as.numeric()

data <- data.frame(city = cities, AIQ = AIQ)
