# REST API v0.1.0

![componentincomplete]

- Contains the business logic of the project

- Exposes the REST API end points called by the UI

# TODO

## Services
- Utils ![incomplete]
  - Converters ![varuncomplete]
    - DF to DB Objects ![done]
    - DB Objects to DF ![done]
  - Push obj to DB ![hritikincomplete]
    - Converts from DF to list of objects 
    - Accepts list of objects / df as input 
    - For an object
      - If correct attributes given
      - Checks If data already present in DB
      - Else Pushes the data to DB
  - Get objects from DB ![dishaincomplete]
    - Filters / gets data according to parameters 
    - Convert to DF
- Indicator Calc ![samrudhiincomplete]
  - Input is column and Triples of (Indicator type, time period, Dimension)
  - Returns DF with Dimension and Indicators cols
- Signal generation ![hritikincomplete]
  - Run the strategy on given data + indicators + predictions and generate Buy / Short signals
  - Input as Strategy type, Strategy config,  data + Indicators required by strategy 
  - Pushes all signals to DB, add their ids as a column in DF
  - Returns a DF with all signals for data
- Order execution ![varunincomplete]
  - Executes all signals according to execution assumptions, notes execution candlestick
  - Closes all possible orders according to strategy config given, notes candlestick which closes order
  - Pushes all orders to DB, add their ids as a column in DF 
  - Returns DF for executed and closed orders 
- Trade evaluation ![dishaincomplete]
  - Evaluates all pairs of orders and calculates, net returns, returns %, duration, etc. 
  - Pushes all Trades to DB, add their ids as a column in DB 
  - Returns DF with All trade pairs
- Backtesting Report generation ![samrudhiincomplete]
  - Pushes the backtest report to DB with status Running / Pending 
  - Orchestrates calling of various services to run the backtest 
  - Calculates net returns across all trades, P&L trades number, P&L trades %, overall outlook, different ratios, etc. 
  - Pushes Backtest Trades to DB 
  - Pushes Final report to DB
- Generate Visualization ![varunincomplete]
  - Input - Visualization type, DF with correct data for Visualization, image size req 
  - Generates visualization as an image 
  - Returns image

## REST API endpoints
- `GET` All Strategies ![dishaincomplete]
  - Returns all strategies and their info in DB
- `GET` Strategy data ![samrudhiincomplete]
  - Returns all data pertaining to a strategy and their info in DB
- `GET` All backtests ![hritikincomplete]
  - All backtests and their info to be displayed in short form
- `GET` Backtest data ![varunincomplete]
  - input = id, img height, img width
  - Given id, returns all information about a backtest
- `GET` Backtest visualizations ![hritikincomplete]
  - Generates and returns all images for a given backtest id

## Automated testing
###### Using unit tests in-built in django-each class created must have unit tests-which cover all test cases of a class
- restapi
  - backtester apis
  - strategy apis
- services
  - Utils
    - Converters
    - Pushers
    - Getters
  - Indicator calc
  - Model predictions
  - Signal generation
  - Order Execution
  - Trade evaluation
  - Backtest Report Generation
  - Generate Visualization

[done]: https://img.shields.io/badge/DONE-brightgreen
[incomplete]: https://img.shields.io/badge/INCOMPLETE-red
[varunincomplete]: https://img.shields.io/badge/VARUN-INCOMPLETE-red
[varuncomplete]: https://img.shields.io/badge/VARUN-COMPLETE-brightgreen
[dishaincomplete]: https://img.shields.io/badge/DISHA-INCOMPLETE-red
[dishacomplete]: https://img.shields.io/badge/DISHA-COMPLETE-brightgreen
[samrudhiincomplete]: https://img.shields.io/badge/SAMRUDHI-INCOMPLETE-red
[samrudhicomplete]: https://img.shields.io/badge/SAMRUDHI-COMPLETE-brightgreen
[hritikincomplete]: https://img.shields.io/badge/HRITIK-INCOMPLETE-red
[hritikcomplete]: https://img.shields.io/badge/HRITIK-COMPLETE-brightgreen
[bug]: https://img.shields.io/badge/BUG-red
[bugfixed]: https://img.shields.io/badge/BUG-FIXED-brightgreen
[featureincomplete]: https://img.shields.io/badge/FEATURE-INCOMPLETE-red
[featurecomplete]: https://img.shields.io/badge/FEATURE-COMPLETE-brightgreen
[componentincomplete]: https://img.shields.io/badge/COMPONENT-INCOMPLETE-red
[componentcomplete]: https://img.shields.io/badge/COMPONENT-COMPLETE-brightgreen
[phasecomplete]: https://img.shields.io/badge/PHASE-COMPLETE-brightgreen
[phaseincomplete]: https://img.shields.io/badge/PHASE-INCOMPLETE-red
[meetingincomplete]: https://img.shields.io/badge/MEETING-INCOMPLETE-red
[docincomplete]: https://img.shields.io/badge/DOC-INCOMPLETE-red
[doccomplete]: https://img.shields.io/badge/DOC-COMPLETE-brightgreen