if(!require(rvest)) install.packages('rvest')
if(!require(stringr)) install.packages('stringr')

if(!require(xlsx)) install.packages('xlsx')

url = "http://www.zyzw.com/twzs010.htm"
web = read_html(url, encoding = 'GBK')
web
Name = web %>% 
  html_nodes('b') %>%
  html_text(trim = FALSE) %>% 
  gsub("(\\n\\t|，|\\d|、)", "", .) %>% 
  grep("\\S", ., value = TRUE) %>% 
  str_trim(side = "both") %>% 
  .[1:54] %>% 
  .[setdiff(1:54, c(35, 39))]

link = paste0("http://www.zyzw.com/zgsjyc/zgsjyc", springf("%03d", 1:52), ".htm")
img_link = paste0("http://www.zyzw.com/zgsjyc/zgsjyct/zgsjyc", sprintf("%03d", 1:52), ".jpg")
mydata = data.frame(Name = Name, link = link, img_link = img_link)

if(!require(lubridate)) install.packages('lubridate')
if(!require(ggplot2)) install.packages('ggplot2')
if(!require(plyr)) install.packages('plyr')
if(!require(RColorBrewer)) install.packages('RColorBrewer')
if(!require(dplyr)) install.packages('dplyr')
if(!require(maptools)) install.packages('maptools')
if(!require(ggthemes)) install.packages('ggthemes')
if(!require(leafletCN)) install.packages('leafletCN')
if(!require(leaflet)) install.packages('leaflet')
if(!require(htmltools)) install.packages('htmltools')
if(!require(shiny)) install.packages('shiny')
if(!require(shinydashborad)) install.packages('shinydashborad')
if(!require(rgdal)) install.packages('rgdal')

