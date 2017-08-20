# Goal
Analyzing product sentiment
# File Description
- `.rar` files is data file.
  - `[amazon_baby.rar](https://github.com/SSQ/Coursera-UW-Machine-Learning-Classification/blob/master/Programming%20Assignment%201/amazon_baby.rar)` (unzip `amazon_baby.csv`) consists of 183,531 customers with `name`, `review`, `rating`.
- `.ipynb` file is the solution of Week 3 program assignment
  - `Analyzing product sentiment.ipynb`
  - `Week 3 exe.ipynb`
- `.html` file is the html version of `.ipynb` file.
  - `Analyzing+product+sentiment.html`
  - `Week+3+exe.html`
# Snapshot
open `.html` file via brower for quick look.
# Algorithm
- Logistic Regression
# Implementation
- Execute sentiment analysis code with the IPython notebook
- Load and transform real, text data
- Using the `.apply()` function to create new columns (features) for our model
- Compare results of two models, one using all words and the other using a subset of the words
- Compare learned models with majority class prediction
- Examine the predictions of a sentiment model
- Build a sentiment analysis model using a classifier
# Implementation in detail
1. Use .apply() to build a new feature with the counts for each of the selected_words
2. Create a new sentiment analysis model using only the selected_words as features
3. Comparing the accuracy of different sentiment analysis model
4. Interpreting the difference in performance between the models
