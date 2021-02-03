# Capstone Project - AI Trading Platform

### What is the project ?

To build a platform for creating, backtesting and paper trading new automated strategies on real-time, minute scale data with the help of AI models.

# Components in the project

## Data Feeder

* Used to source real-time minute scale data from over 5000 stocks in the stock market.

* Perform very fast, basic calculations on the raw data.

## Database

* We use a database to store the data from the data feeder. 

* We also use it to perform more complex calculations (such as indicators) very quickly at a large scale for all stocks whose data has been sent from the data feeder.

## Strategies
###### This is the heart of the project

* Strategies read data from the database and can use multiple indicators, machine learning models or a combination to generate orders according to the rules mentioned in the strategy.

* There may be multiple strategies created and deployed in this service.

## Backtester

* This service helps in building Strategies. It allows us test how a strategy would have performed over past data over previous weeks, months and years.

* It takes a parameterised strategy and data over the period of the back test as input. It generates orders over the previous data according to the strategy's rules and outputs a detailed report on the performance of the strategy.

## Paper Trader

* This is used to test strategies in real-time market scenarios after a strategy has performed well in back testing.

* It tracks and evaluates orders generated by multiple strategies in real-time market conditions and provides various performance metrics for both strategies and orders.

## UI

* This service is a website which provides a GUI for the user to interact with all the other services.

* It allows the user flexibility to create, back test, paper trade and deploy new strategies on real-time data from the stock market.


# To replicate this project on your computer

1. Make a new directory.
2. cd into the directory via `cd <directory_name>` 
3. run these commands to initialize the project: 
```
git init

git remote add origin "git@github.com:Varun487/CapstoneProject_AITradingPlatform.git"

git pull origin main
```

# Project members
###### All members are from Semester 6  Pes University EC Campus
1. Varun Seshu - PES2201800074
2. Hritik Shanbhag - PES2201800082
3. Disha Venkatesh - PES2201800109
4. Samrudhi R Rao - PES2201800126

# Future prospects

This project can be pursued in the future to build a fully integrated trading system with a broker to place orders generated by the strategies in the live market and generate consistent profits.
