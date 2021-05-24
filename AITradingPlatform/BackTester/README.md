# BACKTESTER v1.0

![COMPONENTINCOMPLETE]

* This service helps in building Strategies. It allows us test how a strategy would have performed over past data over previous weeks, months and years.

* It takes a parameterised strategy and data over the period of the back test as input. It generates orders over the previous data according to the strategy's rules and outputs a detailed report on the performance of the strategy.

# TODO v1.0


## BACKTESTER WORK

---

### DB ![HRITIKINCOMPLETE]

- BackTestOrder
	- Order `Foreign key`
	- Backtest report `Foreign key`

- BackTestReport
	- Initial account size
	- Max Risk %
	- Risk ratio `Stoploss, Takeprofit`
	- Start date time
	- End date time
	- Companies `List`
	- Strategy
		- column
		- indicator_time_period
		- sigma
	- Final account size
	- Total Profit / Loss

---

### Back testing `Historical data` ![FEATUREINCOMPLETE]

- Get Req data from DB ![VARUNCOMPLETE]
	- Source data if not present ![DONE]
	- Calc Indicators if not present ![DONE]

- Call the strategy function with data ![SAMRUDHIINCOMPLETE]
  - get strategy name
  - get start and end date
  - call the strategy

- Evaluate orders `according to future` ![DISHAINCOMPLETE]
	- Order owner
	- Profit / Loss
	- Push orders to DB

- Generate report ![SAMRUDHIINCOMPLETE]
	- Eval Total Profit / Loss, final account size according to all orders performance, Initial account, Start date, etc.
	- Push report to DB

### REST API ![FEATUREINCOMPLETE]

- View all reports
- Filter reports according to strategy, risk %, Account size, etc.
- View all orders ![HRITIKCOMPLETE]
- Filter orders according to all orders attributes ![SAMRUDHIINCOMPLETE]

---

### Update REST API docs page with all Backtester APIs ![FEATUREINCOMPLETE]
- ![VARUNINCOMPLETE]
- ![SAMRUDHIINCOMPLETE]
- ![DISHAINCOMPLETE]
- ![HRITIKINCOMPLETE]

---

### Automated testing ![FEATUREINCOMPLETE]
- Complete writing all tests for all functions, REST APIs and UI 
  - ![VARUNINCOMPLETE]
  - ![DISHAINCOMPLETE]
  - ![HRITIKINCOMPLETE]
  - ![SAMRUDHIINCOMPLETE]


[DONE]: https://img.shields.io/badge/DONE-brightgreen
[INCOMPLETE]: https://img.shields.io/badge/INCOMPLETE-red

[ALLINCOMPLETE]: https://img.shields.io/badge/ALL-INCOMPLETE-red
[ALLCOMPLETE]: https://img.shields.io/badge/ALL-COMPLETE-brightgreen

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
