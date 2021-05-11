# STRATEGIES v1.0

###### This is the heart of the project

![COMPONENTINCOMPLETE]

* Strategies read data from the database and can use multiple indicators, machine learning models, or a combination to generate orders according to the rules mentioned in the strategy.

* There may be multiple strategies created and deployed in this service.


# TODO v1.0

## STRATEGIES WORK

---

### DB ![DISHAINCOMPLETE]

- Strategy
	- Name
	- Description
	- Companies/Sector
- Orders
	- Order type `BUY/SELL`
	- Company
	- TimeStamp
	- Order category `Market/Limit`
	- Take profit `Can be Blank`
	- Stop loss
	- Strategy name
	- Order Owner
	- Profit/Loss `Blank in the beginning`

---

### Strategies ![VARUNINCOMPLETE]

- Simple Bollinger bands strategy
	- Data
		- Close price
		- SMA
		- 2 sigma above and below SMA
	- Rules
		- If stock price > 2 sigma above SMA `SHORT`
		- If stock price crosses SMA `GET OUT OF ALL POSITIONS`
		- If stock price < 2 sigma above SMA `BUY`

---

### REST API END POINTS ![FEATUREINCOMPLETE]

- View all strategies ![SAMRUDHIINCOMPLETE]
- View all orders ![HRITIKINCOMPLETE]
- Filter orders according to all orders attributes ![SAMRUDHIINCOMPLETE]

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
