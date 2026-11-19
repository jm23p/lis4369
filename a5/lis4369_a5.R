# clear RStudio console, environment, plot panes and free up memory at once:
rm(list = ls(envir = globalenv()), envir = globalenv()); if(!is.null(dev.list())) dev.off(); gc(); cat("\014")

# set working directory
setwd('C:/Users/fsuma/lis4369/a5')

# assignment:
# scalars: most basic way to store a number is through assignment
# assignment is specified with "<-" characters
# assigns number on right of assignment symbol, and stores it in variable on left
a <- 9
a # print value of a

a + 5 # print a + 5

b <- sqrt(a) # assign square root of a to b
b # print value of b

# nonscalar data types:
# easiest way to store list of numbers, through assignment, using c command
# note: c means combine
# vectors (one dimensional arrays), by default, are specified with the c command

c <- c(1,2,5.3,6,-2,4) # also, numeric vector
print(c)

typeof(c) # print data type

is.list(c) # FALSE
is.vector(c) # TRUE

d <- c("one","two","three") # character vector
d

typeof(d) # print data type

e <- c(TRUE,TRUE,TRUE,FALSE,TRUE,FALSE) # logical vector
e

typeof(e)

# to refer to row in Python, use index
# in R, refer to object in ith row and jth column by OBJECTNAME[i,j]
# In other languages, index starts at 0; in R, it starts with 1
d[1]

# string specified by using quotes - either single or double quotes work
my_str <- "Hello World!"
my_str

typeof(my_str) # print data type

# some intrinsic functions on scalar a, and vector c:
sqrt(a)

sqrt(c) # research why this produces an error

a^2 # scalar squared

c^2 # vector squared

min(c)

max(c)

mean(c)

sum(c)

# reading CSV file (comma separated values):
# command: read.csv() reads file into data frame (similar to Python)
# requires at least one argument: name of file
# if three arguments:
  # 1) name of file
  # 2) indicates if first row are labels/headers
  # 3) indicates separator character

url = "https://raw.github.com/vincentarelbundock/Rdatasets/master/csv/Stat2Data/Titanic.csv"
titanic <- read.csv(file=url,head=TRUE,sep=',') # reads file and assigns to variable

titanic # displays all data from file

summary(titanic) # summary(): generic function used to produce result summaries

dir() # list files in current working directory

getwd() # determine current working directory

names(titanic) # print headers

# access each column using "$":
titanic$Name # prints names

titanic$Age # prints ages

attributes(titanic) # returns object's attribute list

ls() # print list of variables defines in session

# basic statistics:
mean(titanic$Age) # returns NA, due to missing values

# fix: remove missing values
mean(titanic$Age, na.rm=TRUE)
median(titanic$Age, na.rm=TRUE)
quantile(titanic$Age, na.rm=TRUE)
min(titanic$Age, na.rm=TRUE)
max(titanic$Age, na.rm=TRUE)
var(titanic$Age, na.rm=TRUE)
sd(titanic$Age, na.rm=TRUE)

# summary() function prints min, max, mean, median, and quantiles
summary(titanic$Age, na.rm=TRUE)

# complete.cases() returns logical vector indicating which cases are complete
# list rows of data with missing values
titanic[!complete.cases(titanic),]

# na.omit() returns object with listwise deletion of missing values
# create new dataset without missing data
titanic_no_missing_data <- na.omit(titanic)
titanic_no_missing_data # display new data set w/o missing values

# charting/plotting
help(stripchart) # help command

pdf(file="C:/Users/fsuma/lis4369/a5/myplotfile.pdf")
stripchart(titanic_no_missing_data$Age) # strip chart

# histogram
hist(titanic_no_missing_data$Age, main="Distribution of Titanic Passengers Ages",xlab="Ages")

# boxplot
boxplot(titanic_no_missing_data$Age)

dev.off()

# or plotted horizontally
# png(filename = "boxplot.png",
#     width = 800, height = 600, units = "px", pointsize = 12, bg = "burlywood")
boxplot(titanic_no_missing_data$Age,
        main='Distribution of Titanic Passengers Ages',
        xlab='Ages',
        horizontal=TRUE)

dev.off()

plot(titanic_no_missing_data$Age,titanic_no_missing_data$Survived,
     main="Relationship Between Ages and Survival",
     xlab="Age",
     ylab="Survived")

dev.off()

# create scatterplot png
png(filename = "scatterplot.png",
    width = 800, height = 600, units = "px", pointsize = 12, bg = "cadetblue")

plot(titanic_no_missing_data$Age, titanic_no_missing_data$Survived,
     main = "Relationship Between Ages and Survival",
     xlab = "Age",
    ylab = "Survived")

dev.off()

# stores entire workspace to file named .RData by default
# next R restart workspace will be loaded
save.image()