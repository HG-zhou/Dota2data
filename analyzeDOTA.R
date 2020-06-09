# Check if hero choices can affect the game result. R^2 is tiny. AUC is close to 0.5. 
# Check if all available predictor variables can affect the game result. R^2 is about 0.85.  AUC is close to 1.0. What are the most important predictor variables.
# Make a table to explain what V3~V57 mean.

D <- read.table('dota-data.txt', header=FALSE, check.names=FALSE) # dota-data.txt should be made available on your github account.

Y <- as.numeric(D$V2) - 1
#X <- D[,c(8,13,18,23,28)]
X <- D[,3:57]
Z <- as.data.frame(cbind(Y,X))

# Multiple linear regression  (explain it)
train_index <- sample(dim(Z)[1], 800) # choose 600 games as training data
model <- lm(Y ~ ., data=Z[train_index,])
summary(model)

test_prob = predict(model, newdata = Z[-train_index,], type = "response")


library(pROC)
test_roc = roc(Y[-train_index] ~ test_prob, plot = TRUE, print.auc = TRUE)








# logistc regression
train_index <- sample(dim(Z)[1], 1000)

model <- glm(Y ~.,family=binomial,data=Z[train_index,])
summary(model)

test_prob = predict(model, newdata = Z[-train_index,], type = "response")

library(pROC)
test_roc = roc(Y[-train_index] ~ test_prob, plot = TRUE, print.auc = TRUE)


