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
- Design paper trader services ![varuncomplete]
- Source Data ![varuncomplete]
  - Given company ticker, start date, end date ![done]
  - Sources data, returns df ![done]
- Update Company Quotes ![varuncomplete]
  - For all companies in DB (or given as input)  ![done]
    - Source latest data ![done]
    - Update company quote in DB (create quote if not present) ![done]
- Evaluate Live Paper Trades ![varuncomplete]
  - For each live paper trade ![done]
    - If stop loss or take profit limit is reached ![done]
      - Exit position ![done]
      - Evaluate closed trade ![done]
      - Remove from live trades ![done]
- Execute Live Paper Signals ![varuncomplete]
  - For each signal in live generated signals ![done]
    - Execute entry orders and create a paper trade ![done]
    - Push to everything to DB ![done]
- Generate Paper Signals ![varuncomplete]
  - For each strategy config currently paper traded ![done]
    - Generate signals ![done]
- Paper Trade ![varuncomplete]
  - Execute periodically ![done]
  - Custom Django admin command for paper trade execution ![done]
  - Synchronises and calls all services above ![done]
- Generate Visualization ![varunincomplete]
  - Input - Visualization type, DF with correct data for Visualization, image size req ![done] 
  - Generates visualization as an image ![done]
  - Visualization 1 - SIGNALS ![done]
    - Company data, Indicators, Signals ![done]
  - Visualization 2 - PER TRADE ![done]
    - Company data, Indicators, Signal, Entry order, Exit order ![done]
  - Redesign module ![done]
      - Create dataframe, taking backtest report object as input ![done]
      - complete the visualization class ![done]
  - Complete signals visualization ![done]
  - Complete per trade visualization ![done]
  - Make all visualizations strategy dependent ![done]
    - Signals ![done]
    - Per trade ![done]
  - Paper Trade Visualization Per Paper Trade (Live and Historical) ![incomplete]

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
- `GET` Backtest Signals Visualization ![varuncomplete]
  - Extract backtest report, Generate visualization ![done]
  - Given backtest id, Generates and returns signals visualization of backtest ![done]
  - Generate correct viz ![done]
  - Return a base 64 string with image data ![done]
- `GET` Backtest Trade visualization ![varuncomplete]
  - Extract trade from given id ![done]
  - Given backtest trade id, Generates and returns visualization of trade ![done]
  - Return a base 64 string ![done]
- Design paper traded REST APIs ![varuncomplete]
- `GET` All Paper Trades ![varunincomplete]
  - Input = Strategy id
  - Get all paper trades corresponding to the strategy
  - Priority to live trades
- `GET` Paper Trade data ![varunincomplete]
  - Input = Paper Trade id
  - In depth information on paper trade
- `GET` Current Quote ![varunincomplete]
  - Input = Paper Trade id
  - Get the latest company data with last updated date
  - According to paper trade id's company
- `GET` Paper Trade Visualization ![varunincomplete]
  - Input = Paper Trade id
  - Generate picture for paper trade visualizations
  - Return base 64 string

# Strategies 
- Demo 1 - Simple bollinger band strategy ![varuncomplete]
- Demo 2 - LSTM predictions strategy ![varunincomplete]
- Custom Strategy 1 ![varunincomplete]

## Automated testing ![varunincomplete]
###### Using unit tests in-built in django - each class created must have unit tests which cover all test cases of a class
- restapi
  - Auth apis
    - `POST` Authorization
  - Strategy apis
    - `GET` All Strategies
    - `GET` Strategy data
  - Backtest apis
    - `GET` All backtests of a strategy
    - `GET` Backtest data
    - `GET` All Backtest trades
    - `GET` Trade data
    - `GET` Backtest Signals Visualization
    - `GET` Backtest Trade visualization
  - Paper Trade apis
    - `GET` All Paper Trades
    - `GET` Paper Trade data
    - `GET` Current Quote
    - `GET` Paper Trade Visualization
- services
  - Utils ![done]
    - Converters ![done]
    - Pushers ![done]
    - Getters ![done]
  - Indicator calc ![done]
  - Signal generation ![done]
    - Generic Signal Generator ![done]
    - BBSignalGenerator ![done]
  - Order Execution ![done]
    - Generic Take profit stop loss ![done]
    - Take profit stop loss BB ![done]
    - Order Execution ![done]
  - Trade evaluation ![done]
  - Backtest Report Generation ![done]
  - Generate Visualization 
    - Generic visualization ![done]
    - Signals visualization ![done]
    - Per trade visualization ![done]
    - Paper trade visualization
  - Source Data ![done]
  - Update Company Quotes
  - Evaluate Live Paper Trades
  - Execute Live Paper Signals
  - Generate Paper Signals
  - Paper Trade
  - cron job execution

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
