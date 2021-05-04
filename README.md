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

* Strategies read data from the database and can use multiple indicators, machine learning models, or a combination to generate orders according to the rules mentioned in the strategy.

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
git init -b main

git remote add origin "git@github.com:Varun487/CapstoneProject_AITradingPlatform.git"

git pull origin main

docker-compose up
```
4. To start the project run and all containers:
```
docker-compose up -d
```
5. To stop all running containers in project:
```
docker-compose down
```
5. To create a super user for the database
```
docker-compose run rest_api python AITradingPlatform/manage.py createsuperuser
```

# Project members
###### All members are from Semester 6 Pes University EC Campus
1. Varun Seshu - PES2201800074
2. Hritik Shanbhag - PES2201800082
3. Disha Venkatesh - PES2201800109
4. Samrudhi R Rao - PES2201800126

# Future prospects

This project can be pursued in the future to build a fully integrated trading system with a broker to place orders generated by the strategies in the live market and generate consistent profits.

# TODO
__PROJECT PHASE 1__ *-> COMPLETE BEFORE ESA BEGINS*
1. Final presentation ![DOCINCOMPLETE]
2. FILL WEEKLY PROGRESS PAGE ![DOCINCOMPLETE]
    - Physical printout ??
3. 2 Research papers per person ![DOCINCOMPLETE]
    - __CERTIFIED__ from ma'am

__PROJECT PHASE 2__ *-> COMPLETE BY JULY END*
1. CONFIG WORK ![FEATURECOMPLETE] 
    - Build all docker containers and run it locally ![DONE]
        - REST API  ![DONE]
        - DB  ![DONE]
        - Server ![DONE]
            - Setup Nginx server ![DONE]
            - Make it serve Django files ![DONE]
2. DATAFEEDER WORK ![FEATUREINCOMPLETE]
    - DB ![INCOMPLETE]
        - Company ![INCOMPLETE]
          - Name
          - Ticker
          - Sector
        - Time stamp ![INCOMPLETE]
          - Minute 
          - Hour
          - Date
          - Month
          - Year
        - Immutable Data ![INCOMPLETE]
          - Open
          - High
          - Low
          - Close
          - Volume
          - Company id
          - Time Stamp id
        - Calculated Candle stick Data ![INCOMPLETE]
          - Open
          - High
          - Low
          - Close
          - Volume
          - Company id
          - Time Stamp id
        - Indicators ![INCOMPLETE]
          - SMA 
          - Std. Dev 
          - Company id
          - Time Stamp id
    - Sourcing functions ![INCOMPLETE]
        - On demand (functions) ![INCOMPLETE]
          - Parameters
            - Company `List`
            - time period for data collection 
            - Provider - AlphaVantage / Yahoo Finance
          - Calculate indicators
          - Push to DB
        - Real time ![INCOMPLETE]
          - Call on demand function in an infinite loop
    - Indicators calc functions ![INCOMPLETE]
        - Parameters
          - Company
          - time periods `List`
        - SMA ![INCOMPLETE]
        - Std Dev ![INCOMPLETE]
        - Different candle stick time periods ![INCOMPLETE]
3. MODELS WORK ![FEATUREINCOMPLETE]
4. BACKTESTER WORK ![FEATUREINCOMPLETE]
5. PAPER TRADER ![FEATUREINCOMPLETE]
6. UI WORK ![FEATUREINCOMPLETE]
7. Build a simple BB test strategy ![FEATUREINCOMPLETE]
8. Run Django in a Production environment on the VM ![FEATUREINCOMPLETE]
    - Buy a domain ![DONE]
    - SSL certification
    - Host the REST API
    - Decide deployment workflow
    - Make a deployment script
9. Build a simple LSTM predictions test strategy ![FEATUREINCOMPLETE]
10. Build Strategies ![FEATUREINCOMPLETE]
    - 4 Strategies which perform better than sectoral market indices
11. Write papers, see if you can publish them ![DOCINCOMPLETE]

[DONE]: https://img.shields.io/badge/DONE-brightgreen
[INCOMPLETE]: https://img.shields.io/badge/INCOMPLETE-red
[BUG]: https://img.shields.io/badge/BUG-red
[BUGFIXED]: https://img.shields.io/badge/BUG-FIXED-brightgreen
[FEATUREINCOMPLETE]: https://img.shields.io/badge/FEATURE-INCOMPLETE-red
[FEATURECOMPLETE]: https://img.shields.io/badge/FEATURE-COMPLETE-brightgreen
[MEETINGINCOMPLETE]: https://img.shields.io/badge/MEETING-INCOMPLETE-red
[DOCINCOMPLETE]: https://img.shields.io/badge/DOC-INCOMPLETE-red
[DOCCOMPLETE]: https://img.shields.io/badge/DOC-COMPLETE-brightgreen
