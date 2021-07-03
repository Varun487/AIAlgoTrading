# REST API v0.1.0

![componentincomplete]

- Contains the business logic of the project

- Exposes the REST API end points called by the UI

# TODO

## Services
- Utils ![done]
  - Converters ![varuncomplete]
    - DF to DB Objects ![done]
    - DB Objects to DF ![done]
  - Push obj to DB ![hritikcomplete]
    - Converts from DF to list of objects ![done]
    - Accepts list of objects / df as input ![done]
    - For an object ![done]
      - If correct attributes given ![done]
      - Checks If data already present in DB ![done]
      - Else Pushes the data to DB ![done]
    - Tests ![varuncomplete]
    - Push multiple objects not working ![bugfixed] ![varuncomplete]
  - Get objects from DB ![dishacomplete]
    - Filters / gets data according to parameters ![done]
    - Convert to DF ![done]
    - Testing ![varuncomplete]
- Indicator Calc ![samrudhicomplete]
  - Input is column and Triples of (time period, Dimension) ![done]
  - Returns DF with Dimension and Indicators cols ![done]
- Signal generation ![varuncomplete]
  - Run the strategy on given data + indicators + predictions and generate Buy / Sell / Flat signals ![done]
  - Input as Strategy config ![done] 
  - Returns a DF with all signals for data ![done]
- Order execution ![hritikcomplete] ![varuncomplete]
  - Input = SignalGenerator, take_profit(method and factors), stop_loss(method and factors), max_holding_period ![done]
  - Take Profit and stop loss criteria - Classes which put 2 columns per order on where to take profit and stop loss ![done]
  - Executes all signals according to execution assumptions, notes execution candlestick ![done]
  - Closes all possible orders according to strategy config given, notes candlestick which closes order ![done]
  - Returns DF for executed and closed orders ![done]
- Trade evaluation ![dishacomplete]
   - Input ![done]
      - df with columns 'order_entry_price', 'order_exit_price', 'order_entry_index', 'order_exit_index' ![done]
   - Evaluates all pairs of orders (entry and exit orders) and calculates, net returns, returns % and duration of trade. ![done]
   - Returns DF with columns 'trade_net_return', 'trade_return_percentage' and 'trade_duration' ![done]
   - Merge all code ![varuncomplete]
- Backtesting Report generation ![samrudhicomplete] ![varuncomplete]
  - Orchestrates calling of various services to run the backtest ![done]
  - Calculates net returns across all trades, net return % across all trades, number of profit trades, number of loss trades, total trades, % of profitable trades, % of loss trades. ![done]
  - Rebuild the backtestreportgenerator class with new inputs and validators ![done]
  - Pushes all signals to DB, gets their ids ![done]
  - Pushes all orders to DB, gets their ids ![done]
  - Pushes all Trades to DB, gets their ids ![done]
  - Pushes Backtest report to DB, gets its id ![done]
  - Pushes Backtest Trades to DB ![done]
  - Testing ![done]
- User Auth ![varuncomplete]
  - Token returned on signin ![done]
  - Authorization to access all APIs ![done]
- Generate Visualization ![varunincomplete]
  - Input - Visualization type, DF with correct data for Visualization, image size req ![done] 
  - Generates visualization as an image ![done]
  - Visualization 1 - SIGNALS ![done]
    - Company data, Indicators, Signals ![done]
  - Visualization 2 - PER TRADE ![done]
    - Company data, Indicators, Signal, Entry order, Exit order ![done]
  - Redesign module ![incomplete]
      - Create dataframe, taking backtest report object as input ![incomplete]
      - complete the visualization class
  - Complete signals visualization
  - Complete per trade visualization
  - Testing
- Sourcing Data real-time ![varunincomplete]
  - design **To be done later**
- Paper trading ![varunincomplete]
  - design **To be done later**

## REST API endpoints
- `POST` Authorization ![varuncomplete]
  - Token returned on signin ![done]
- `GET` All Strategies ![varuncomplete]
  - Returns all strategies and their info in DB ![done]
- `GET` Strategy data ![varuncomplete]
  - Returns all data pertaining to a strategy in DB ![done]
- `GET` All backtests of a strategy ![varuncomplete]
  - All backtests pertaining to a strategy and their info to be displayed in short form ![done]
- `GET` Backtest data ![varuncomplete]
  - Given backtest id, returns all information about a backtest ![done]
- `GET` All Backtest trades ![varuncomplete]
  - Given backtest id, returns all backtest trades pertaining to BT ![done]
- `GET` Trade data ![varuncomplete]
  - Given trade id, get in depth data for a trade ![done]
- `GET` Backtest Signals Visualization ![varunincomplete]
  - Extract backtest report, Generate visualization
  - Given backtest id, Generates and returns signals visualization of backtest
  - Generate correct viz 
  - Return a base 64 string with image data
- `GET` Backtest Trade visualization ![varunincomplete]
  - Extract trade from given id
  - Given backtest trade id, Generates and returns visualization of trade
  - Return a base 64 string
- `GET` Paper trades ![varunincomplete]
  - design **To be done later**
- `GET` Current Quote ![varunincomplete]
  - design **To be done later**

# Strategies 
- Demo 1 - Simple bollinger band strategy ![varuncomplete]
- Demo 2 - LSTM predictions strategy ![varunincomplete]
  - **To be done later**
- Custom Strategy 1 
  - **To be done later**
- Custom Strategy 2
  - **To be done later**

## Automated testing
###### Using unit tests in-built in django - each class created must have unit tests which cover all test cases of a class
- restapi
  - backtest apis
  - strategy apis
- services
  - Utils
    - Converters
    - Pushers
    - Getters
  - Indicator calc
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
