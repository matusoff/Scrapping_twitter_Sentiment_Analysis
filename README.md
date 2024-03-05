# Twitter Sentiment Analysis

This repository hosts a comprehensive sentiment analysis project focused on Twitter data. This project employs various natural language processing (NLP) techniques and machine learning models to understand the sentiments expressed in tweets. The goal is to analyze the common words used in tweets, preprocess data, and apply several models to predict sentiments accurately.

## Project Overview

The project involves several key steps to analyze and predict the sentiment of tweets effectively:

- **WordCloud Visualization:** Understanding the common words used in tweets through WordCloud.
- **Data Preprocessing:** Converting raw data into features suitable for model training, including Bag-of-Words and TF-IDF features.
- **Word2Vec:** Training the Word2Vec model and tokenizing tweets to create vectors that represent the semantic meaning of words.
- **Vectorization of Tweets:** Creating a vector for each tweet by averaging the vectors of the words present in the tweet.
- **Model Training:** Training Doc2Vec and SVM models to understand the context and sentiment of tweets.
- **XGBoost Integration:** Utilizing the XGBoost model in conjunction with Word2Vec for enhanced prediction accuracy.
- **Logistic Regression:** Fitting the data using Logistic Regression to obtain various scores for predicted sentiment data.

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed along with the following Python libraries:
- numpy
- pandas
- scikit-learn
- gensim
- xgboost
- matplotlib
- nltk

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
A special thanks to the open-source community and all the projects that provided the tools and libraries necessary to complete this project.
