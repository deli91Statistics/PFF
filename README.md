# Syllabus - Introduction to Python for Finance

In this course, we will introduce basic python concepts and explore their use in financial econometrics.

First, we demonstrate how to use python to manipulate data. Given any project, "data crunching" usually consumes most of the time hence it is essential to have a good command of the vast amount of tools python offers. In particular, we will investigate packages such as pandas and numpy.

The second part of the course introduces financial time series. Here, we will discuss their unique characteristics also known as "stylized facts" and different approaches on how to model them.


Prerequisites on programming languages:
No python knowledge is required although a basic understanding of coding principles is helpful. We will not discuss the theory of the language itself. The focus
is set on its application.

Prerequisites on theory:
A basic understanding of univeriate time series is helpful but not required. Basic statistical concepts and some linear algebra.


## Chapter 1: Collaboration Tools and Setup
- usage of Git and Github
- setup of Python development with virtual environment
- lecture notes will be done with jupyter/colab notebook

## Chapter 1: Basics in data analysis with Python
- introduction to typical software packages such as Pandas, Numpy, Scipy
- introduction to datatypes, like dataframes and dictionaries
- visualization techniques using matplotlib/seaborn
- basic python knowledge (how to structure code)

## Chapter 2: Financial Time Series Analysis with Python
- AR, MA, ARMA modelling
- stylized facts on financial time series and their implications
- volatility models: ARCH & GARCH
- combination of both: ARMA-GARCH Extensions

Literature:
- Lecture Notes: Klaus Wohlrabe and Stefan Mittnik
- Brooks(2008): Introductory Econometrics for Finance
- Tsay(2013): An Introduction to Analysis of Financial Data with R

## Chapter 3: Risk Management
- introduction to monetary risk measures: Value at Risk, Expected Shortfall
- heavy-tail phenomenom of financial time series and their implications
- back-testing methods

Literature:
- McNeil, Embrechts, Frey(2015): Quantitative Risk Management
- Selected Papers of Prof. Mittnik

## Chapter 4: Portfolio Optimization
- classical mean-variance optimization by Markowitz, including constrained optimization
- introduction to the capital asset pricing model
- introduction to convex optimization tasks
- portfolio models with downside risk

Literature: 
- Markowitz(1952): Portfolio Selection
- Joshi and Paterson (2013): Mathematical Portfolio Theory
- Elton et. al (2007): Modern Portfolio Theory and Investment Analysis

## Kapitel 5: Machine Learning Methods
- portfolio selection with neural networks
- return prediction with classification/regression methods
- analyzing high frequency/tick data
- reduction of dimension techniques (Autoencoder vs. PCA)

Literature:
- Lopez de Prado(2018): Advances in Financial Machine Learning 
- Hastie, Tibshirani(2009): The Elements of Statistical Learning: Data Mining, Inference, and Prediction 
