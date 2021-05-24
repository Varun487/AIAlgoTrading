# Capstone Project - AI Trading Platform

### What is the project?

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

## Backend 

### Development server

1. run these commands to initialize the project:
```
git clone "git@github.com:Varun487/CapstoneProject_AITradingPlatform.git"

cd CapstoneProject_AITradingPlatform

docker-compose -f docker-compose.dev.yml up --build
```
2. To start the production server and run all containers:
```
docker-compose -f docker-compose.dev.yml up
```
3. To stop all running containers:
```
docker-compose -f docker-compose.dev.yml down
```
4. Run with fresh build:
```
docker-compose -f docker-compose.dev.yml down
docker-compose -f docker-compose.dev.yml up --build
```
5. To create a super user for the database
```
docker-compose -f docker-compose.dev.yml run rest_api python3 AITradingPlatform/manage.py createsuperuser
```
6. To test the running of the periodic script (real-time data sourcing and paper trading)
```
docker-compose -f docker-compose.dev.yml run rest_api python3 cron/periodic_job.py
```

###### NOTE: To run in production, the commands are the same, but the file is changed to `docker-compose.prod.yml`


## Frontend


1. Install `npm`
2. Install `firebase-tools` npm package
```
npm install -g firebase-tools
```
2. Navigate to `ai-trading-platform-ui` folder
```
cd ./AITradingPlatform/UI/ai-trading-platform-ui
```
3. Run the following commands in `ai-trading-platform-ui` folder
2. Install required modules 
```
npm install
```
4. Start Vue js dev server
```
npm run serve
```
5. Start firebase development server
```
npm run build
firebase serve
```
6. Deploy UI to firebase
```
npm run build
firebase deploy
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
1. Final presentation ![DOCCOMPLETE]
2. FILL WEEKLY PROGRESS PAGE ![DOCCOMPLETE]
3. 2 Research papers per person ![DOCCOMPLETE]
    - __CERTIFIED__ from ma'am

__PROJECT PHASE 2__ *-> COMPLETE BY JULY END*

1. CONFIG WORK ![VARUNCOMPLETE]
    - Build all docker containers and run it locally ![DONE]
        - REST API  ![DONE]
        - DB  ![DONE]
        - Server ![DONE]
            - Setup Nginx server ![DONE]
            - Make it serve Django files ![DONE]
    - Separate development and production environments ![DONE]
	- Add custom domain to firebase for UI ![DONE]
2. DATAFEEDER WORK ![COMPONENTCOMPLETE]
	- [Link to Datafeeder README](https://github.com/Varun487/CapstoneProject_AITradingPlatform/tree/main/AITradingPlatform/DataFeeder)
3. STRATEGIES WORK ![COMPONENTCOMPLETE]
	- [Link to Strategies README](https://github.com/Varun487/CapstoneProject_AITradingPlatform/tree/main/AITradingPlatform/Strategies)
4. BACKTESTER WORK ![COMPONENTINCOMPLETE]
	- [Link to BackTester README](https://github.com/Varun487/CapstoneProject_AITradingPlatform/tree/main/AITradingPlatform/BackTester)
5. PAPER TRADER ![COMPONENTINCOMPLETE]
	- [Link to PaperTrader README](https://github.com/Varun487/CapstoneProject_AITradingPlatform/tree/main/AITradingPlatform/PaperTrader)
6. UI WORK `Vue js` ![COMPONENTINCOMPLETE]
	- [Link to UI README](https://github.com/Varun487/CapstoneProject_AITradingPlatform/tree/main/AITradingPlatform/UI)
7. Automated testing ![FEATUREINCOMPLETE]
    - Build Infra, decide and setup tools 
    - DataFeeder 
      - Complete writing tests for all functions, REST APIs
    - Strategies 
      - Complete writing tests for all functions, REST APIs 
    - BackTester 
      - Complete writing tests for all functions, REST APIs 
    - PaperTrader 
      - Complete writing tests for all functions, REST APIs 
    - UI 
      - Complete writing tests for all UI components

### VERSION 1.0 LAUNCH !

---

8. Run Django in a Production environment on the VM ![FEATUREINCOMPLETE]
    - Buy a domain ![DONE]
    - SSL certification
    - Host the REST API
    - Decide deployment workflow
    - Make a deployment script
9. Build Strategies ![FEATUREINCOMPLETE] 
    - 4 Strategies which perform better than sectoral market indices
10. Write papers, see if you can publish them ![DOCINCOMPLETE]

[DONE]: https://img.shields.io/badge/DONE-brightgreen
[INCOMPLETE]: https://img.shields.io/badge/INCOMPLETE-red

[VARUNINCOMPLETE]: https://img.shields.io/badge/VARUN-INCOMPLETE-red
[VARUNCOMPLETE]: https://img.shields.io/badge/VARUN-COMPLETE-brightgreen

[DISHAINCOMPLETE]: https://img.shields.io/badge/DISHA-INCOMPLETE-red
[DISHACOMPLETE]: https://img.shields.io/badge/DISHA-COMPLETE-brightgreen

[SAMRUDHIINCOMPLETE]: https://img.shields.io/badge/SAMRUDHI-INCOMPLETE-red
[SAMRUDHICOMPLETE]: https://img.shields.io/badge/SAMRUDHI-COMPLETE-brightgreen

[HRITIKINCOMPLETE]: https://img.shields.io/badge/HRITIK-INCOMPLETE-red
[HRITIKCOMPLETE]: https://img.shields.io/badge/HRITIK-COMPLETE-brightgreen

[BUG]: https://img.shields.io/badge/BUG-red
[BUGFIXED]: https://img.shields.io/badge/BUG-FIXED-brightgreen

[FEATUREINCOMPLETE]: https://img.shields.io/badge/FEATURE-INCOMPLETE-red
[FEATURECOMPLETE]: https://img.shields.io/badge/FEATURE-COMPLETE-brightgreen

[COMPONENTINCOMPLETE]: https://img.shields.io/badge/COMPONENT-INCOMPLETE-red
[COMPONENTCOMPLETE]: https://img.shields.io/badge/COMPONENT-COMPLETE-brightgreen

[MEETINGINCOMPLETE]: https://img.shields.io/badge/MEETING-INCOMPLETE-red

[DOCINCOMPLETE]: https://img.shields.io/badge/DOC-INCOMPLETE-red
[DOCCOMPLETE]: https://img.shields.io/badge/DOC-COMPLETE-brightgreen
