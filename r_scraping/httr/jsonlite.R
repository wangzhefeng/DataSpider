#===============================================================================
#                                 jsonlite
#===============================================================================
if(!require(jsonlite)) install.packages("jsonlite")



# fromJSON(R_data)
fromJSON(txt, 
         simplifyVector = TRUE,                 # Array of primitives(元组): ["Amsterdam", "Rotterdam", "Utrecht", "Den Haag"]
         simplifyDataFrame = simplifyVector,    # Array of Objects(对象): [{"name":"Erik", "age":43}, {"name":"Anna", "age":32}]
         simplifyMatrix = simplifyVector,       # Array of arrays(数组): [ [1, 2, 3], [4, 5, 6] ]
         flatten = FALSE)
# toJOSN(JSON_data)
# prettify(JSON_data)
# minify(JSON_data)


toJSON(mtcars)
fromJSON(toJSON(mtcars))
all.equal(mtcars, fromJSON(toJSON(mtcars)))
#=======================================================
# Atomic Vector
json = '["Mario", "Peach", null, "Bowser"]'
fromJSON(json)                         # vector
fromJSON(json, simplifyVector = TRUE)
fromJSON(json, simplifyVector = FALSE) # list


#======================================================
# Data Frames
json = '[
    {"Name": "Mario", "Age": 32, "Occupation": "Plumber"},
    {"Name": "Peach", "Age": 21, "Occupation": "Princess"}, 
    {},
    {"Name": "Bowser", "Occupation": "Koopa"}
]'

mydf = fromJSON(json, simplifyDataFrame = TRUE)
mydf

mydf$Ranking = c(3, 1, 2, 4)
toJSON(mydf, pretty = TRUE)




#=====================================================
# Matrices and Arrays
json = '[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]'

mymatrix = fromJSON(json)
mymatrix = fromJSON(json, simplifyMatrix = TRUE)
mymatrix

toJSON(mymatrix, pretty = TRUE)


json = '[
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]'

myarray = fromJSON(json)
myarray[1, , ]
myarray[2, , ]
myarray[3, , ]
myarray[, , 1]
myarray[, , 2]
myarray[, 1, ]
myarray[, 2, ]



#===============================================================================
#                Fetching JSON data from REST APIs
#===============================================================================
if(!require(jsonlite)) install.packages("jsonlite")

# Github
hadley_orgs = fromJSON("https://api.github.com/users/hadley/orgs")
hadley_repos = fromJSON("https://api.github.com/users/hadley/repos")
gg_commits = fromJSON("https://api.github.com/repos/hadley/ggplot2/commits")
gg_issues = fromJSON("https://api.github.com/repos/hadley/ggplot2/issues")

paste(format(gg_issues$user$login), ":", gg_issues$title)


# CitiBike NYC
citebike = fromJSON("http://citibikenyc.com/stations/json")
stations = citebike$stationBeanList
colnames(stations)

# Ergast
res = fromJSON("http://ergast.com/api/f1/2004/1/results.json")
drivers = res$MRData$RaceTable$Results[[1]]$Driver
colnames(drivers)

drivers[1:10, c("givenName", "familyName", "code", "nationality")]



















