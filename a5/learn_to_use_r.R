# clear console, environment, plots, memory
rm(list = ls(envir = globalenv()), envir = globalenv())
if (!is.null(dev.list())) graphics.off()
gc(); cat("\014")

# Setting your working directory

setwd("C:/Users/fsuma/lis4369/a5")   # change if your folder differs
getwd()


# Installing and using packages (installs only if missing)

pkgs <- c("ggplot2", "psych", "modeest", "dplyr", "sqldf")
for (p in pkgs) if (!requireNamespace(p, quietly = TRUE)) install.packages(p)
library(ggplot2)
library(psych)
library(modeest)
library(dplyr)

# installed.packages()   # list installed packages (long output)
# update.packages()      # update all packages
# remove.packages("x")   # uninstall a package

# Help

?mean
help(mean)
example(mean)
args(mean)
help.search("standard deviation")
??"standard deviation"

# Getting data into R

data()          # list built-in datasets
mtcars          # print mtcars

# The tutorial's read.csv/read.table lines need a file; create one first
write.csv(mtcars, "filename.txt", row.names = FALSE)
mydata <- read.csv("filename.txt")                       # with header
mydata_nohdr <- read.csv("filename.txt", header = FALSE) # without header
write.table(mtcars, "tabfile.txt", sep = "\t", row.names = FALSE)
mydata_tab <- read.table("tabfile.txt", sep = "\t", header = TRUE)
mydata_chr <- read.table("tabfile.txt", sep = "\t", header = TRUE,
                         stringsAsFactors = FALSE)

# Clipboard versions (Windows / Mac) - only run if you've copied data:
# x <- read.table(file = "clipboard", sep = "\t", header = TRUE)  # Windows
# x <- read.table(pipe("pbpaste"), sep = "\t")                     # Mac

# Reading CSV from the web (needs internet):
# mydata <- read.csv("http://bit.ly/10ER84j")
# pew_data <- read.csv("http://bit.ly/11I3iuU")

# Stock data example (needs internet + quantmod):
# install.packages("quantmod"); library(quantmod)
# getSymbols("AAPL")
# barChart(AAPL)
# barChart(AAPL, subset = "last 14 days")
# chartSeries(AAPL, subset = "last 14 days")
# barChart(AAPL["2013-04-01::2013-04-12"])

x <- 1:5
rm(x)                         # remove object x
save(mydata, file = "mydata.rda")   # save one object
load("mydata.rda")                  # reload it

# Examining your data

head(mydata)
head(mydata, n = 10)
head(mydata, 10)
tail(mydata)
tail(mydata, 10)
str(mydata)
colnames(mydata)
rownames(mydata)

# Basic statistics

summary(mydata)
describe(mydata)              # psych package

x <- mtcars$mpg
mean(x); median(x); min(x); max(x)
sd(x); var(x); range(x)
mode(x)                       # data type, NOT the statistical mode
mfv(x)                        # most frequent value (modeest)

cor(mydata)                   # correlation matrix
myvector <- c(4, 8, NA, 15, 16, 23, 42)
mean(myvector)                # NA
mean(myvector, na.rm = TRUE)  # ignores missing value
?median

choose(15, 4)                 # ways to choose 4 from 15
mypeople <- c("Bob", "Joanne", "Sally", "Tim", "Neal")
combn(mypeople, 2)
combn(c("Bob", "Joanne", "Sally", "Tim", "Neal"), 2)

# Slicing and subsetting data

names(mtcars)
mtcars.colnames <- names(mtcars)
mtcars$mpg
mtcars[, 2:4]
mtcars[, c(2, 4)]
mtcars[, -1]

mtcars$mpg > 20
mtcars[mtcars$mpg > 20, ]
mtcars[mtcars$mpg > 20, c(1, 4)]
mtcars[mtcars$mpg > 20, c("mpg", "hp")]

mpg20 <- mtcars$mpg > 20
cols <- c("mpg", "hp")
mtcars[mpg20, cols]

attach(mtcars)
mpg20 <- mpg > 20
detach(mtcars)                # always detach when finished

subset(mtcars, mpg > 20, c("mpg", "hp"))
subset(mtcars, mpg == max(mpg))
subset(mtcars, mpg == max(mpg), mpg)
subset(mtcars, , c("mpg", "hp"))
subset(mtcars, select = c("mpg", "hp"))

# dplyr versions (the tutorial's %.% is outdated; %>% is current)
dplyr::filter(mtcars, mpg > 20)
dplyr::select(mtcars, mpg, hp)
mtcars %>% dplyr::filter(mpg > 20) %>% dplyr::select(mpg, hp)
mtcars %>% dplyr::filter(mpg > 20) %>% dplyr::select(mpg, hp) %>% arrange(desc(mpg))

table(diamonds$cut)
table(diamonds$cut, diamonds$color)

# Basic plots  (shown in Plots tab)

plot(mtcars$disp, mtcars$mpg)
plot(mtcars$disp, mtcars$mpg,
     xlab = "Engine displacement", ylab = "mpg",
     main = "MPG compared with engine displacement")
plot(mtcars$disp, mtcars$mpg,
     xlab = "Engine displacement", ylab = "mpg",
     main = "MPG vs engine displacement", las = 1)
?par

# ggplot2

qplot(disp, mpg, data = mtcars)
qplot(disp, mpg, ylim = c(0, 35), data = mtcars)
qplot(cty, hwy, data = mpg)
qplot(cty, hwy, data = mpg, geom = "jitter")

ggplot(mtcars, aes(x = disp, y = mpg)) + geom_point()
ggplot(pressure, aes(x = temperature, y = pressure)) + geom_line()
ggplot(pressure, aes(x = temperature, y = pressure)) + geom_line() + ylim(0, max(pressure$pressure))
ggplot(pressure, aes(x = temperature, y = pressure)) + geom_line() + geom_point()

# Bar graphs

barplot(BOD$demand)
barplot(BOD$demand, main = "Graph of demand")
barplot(BOD$demand, main = "Graph of demand", names.arg = BOD$Time)

cylcount <- table(mtcars$cyl)
barplot(cylcount)

qplot(mtcars$cyl)
qplot(factor(mtcars$cyl))
ggplot(mtcars, aes(factor(cyl))) + geom_bar()

# Histograms and boxplots

hist(mtcars$mpg, breaks = 10)
qplot(mpg, data = mtcars, binwidth = 4)
ggplot(mtcars, aes(x = mpg)) + geom_histogram(binwidth = 4)

boxplot(mtcars$mpg)
boxplot(diamonds$x, diamonds$y, diamonds$z)

# Colors

colors()
colours()
rainbow(5)
heat.colors(5); terrain.colors(5); topo.colors(5); cm.colors(5)
?rainbow

mycolors <- rainbow(3)
mycolors <- heat.colors(3)
ggplot(mtcars, aes(x = factor(cyl))) + geom_bar(fill = mycolors)
ggplot(mtcars, aes(x = factor(cyl))) + geom_bar(fill = rainbow(3))
barplot(BOD$demand, col = rainbow(6))
barplot(BOD$demand, col = "royalblue3")

# Conditional coloring

testscores <- c(96, 71, 85, 92, 82, 78, 72, 81, 68, 61, 78, 86, 90)
barplot(testscores)
barplot(testscores, col = "blue")

testcolors <- ifelse(testscores >= 80, "blue", "red")
barplot(testscores, col = testcolors)
barplot(testscores, col = testcolors, main = "Test scores")
barplot(testscores, col = testcolors, main = "Test scores", ylim = c(0, 100))
barplot(testscores, col = testcolors, main = "Test scores", ylim = c(0, 100), las = 1)

testscores_sorted <- sort(testscores, decreasing = TRUE)

# the tutorial uses an undefined 'results' data frame, so build one
results <- data.frame(students = factor(paste0("S", seq_along(testscores))),
                      testscores = testscores)
ggplot(results, aes(x = students, y = testscores)) +
  geom_bar(fill = testcolors, stat = "identity")

qplot(factor(cyl), data = mtcars, geom = "bar", fill = factor(cyl))

# Exporting graphics  -> DELIVERABLE 3 (image files)
# Each plot: open device, draw, dev.off()

jpeg("barplot_bod.jpg", width = 350, height = 420)
barplot(BOD$demand, col = rainbow(6))
dev.off()

png("scatter_disp_mpg.png", width = 800, height = 600)
plot(mtcars$disp, mtcars$mpg,
     xlab = "Engine displacement", ylab = "mpg",
     main = "MPG vs engine displacement", las = 1)
dev.off()

png("test_scores_barplot.png", width = 800, height = 600)
barplot(testscores, col = testcolors, main = "Test scores",
        ylim = c(0, 100), las = 1)
dev.off()

p <- ggplot(mtcars, aes(x = disp, y = mpg)) + geom_point()
ggsave("ggplot_scatter.png", plot = p, width = 8, height = 6)

# png(), svg(), and pdf() work like jpeg() with a filename

# Re-draw a couple of plots so they are visible in the Plots tab
# (for the RStudio screenshot, deliverable 4). No dev.off() after these.
plot(mtcars$disp, mtcars$mpg,
     xlab = "Engine displacement", ylab = "mpg",
     main = "MPG vs engine displacement", las = 1)
barplot(testscores, col = testcolors, main = "Test scores",
        ylim = c(0, 100), las = 1)

# Syntax quirks

x <- 3
my_vector <- c(1, 1, 2, 3, 5, 8)
my_vector <- (1:10)
my_vector <- c(1:10)
my_vector <- c(1, 4, "hello", TRUE)       # coerced to character
My_list <- list(1, 4, "hello", TRUE)      # mixed types allowed

my_vector <- c(7, 9, 23, 5)
my_pct_vector <- my_vector * 0.01

my_matrix <- matrix(1:12, nrow = 3)
apply(my_matrix, 1, median)               # row medians
apply(my_matrix, 2, median)               # column medians

class(3); class(3.0); class(3L); class(as.integer(3))
dim(my_matrix)

ls()
getwd()                                   # (pwd throws an error)
my_variable <- 1
rm(my_variable)

library(sqldf)
sqldf("select * from mtcars where mpg > 20 order by mpg desc")

# edit(mtcars)                            # opens data editor window

write.table(mtcars, "testfile.txt", sep = "\t")
write.csv(mtcars, "testfile.csv")         # correct CSV export (sep = ",")

# save entire workspace to .RData
save.image()
