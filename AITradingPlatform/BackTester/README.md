# BACKTESTER v1.0

![COMPONENTINCOMPLETE]

* This service helps in building Strategies. It allows us test how a strategy would have performed over past data over previous weeks, months and years.

* It takes a parameterised strategy and data over the period of the back test as input. It generates orders over the previous data according to the strategy's rules and outputs a detailed report on the performance of the strategy.

# TODO v1.0


## BACKTESTER WORK

---

### DB ![HRITIKINCOMPLETE]
- BackTestReport
	- Initial account size
	- Max Risk %
	- Final account size
	- Start date time
	- End date time
	- Total Profit / Loss
	- Order ids `List`
	- Strategy
	
---

### Back testing `Only for historical data` 
- Get Req data from DB ![VARUNINCOMPLETE]
	- Source data if not present
	- Calc Indicators if not present
- Call the strategy function with data ![SAMRUDHIINCOMPLETE]
- Evaluate orders `according to future` ![DISHAINCOMPLETE]
	- Order owner
	- Profit / Loss
	- Push orders to DB
- Generate report ![SAMRUDHIINCOMPLETE]
	- Eval Total Profit / Loss, final account size according to all orders performance, Initial account, Start date, etc.
	- Push report to DB
- REST API ![DISHAINCOMPLETE]
	- View all reports
	- Filter reports according to strategy, risk %, Account size, etc.

---

### Automated testing ![VARUNINCOMPLETE]



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
