# STRATEGIES v0.1.0

###### This is the heart of the project

![COMPONENTCOMPLETE]

* Strategies read data from the database and can use multiple indicators, machine learning models, or a combination to generate orders according to the rules mentioned in the strategy.

* There may be multiple strategies created and deployed in this service.


# TODO 

## STRATEGIES WORK

---

### DB ![DISHACOMPLETE]

- Strategy ![DONE]
	- Name
	- Description
	- Companies/Sector

- Orders ![DONE]
	- Order type `BUY/SELL`
	- Company
	- TimeStamp
	- Order category `Limit order`
	- Profit/Loss `Blank in the beginning`
	- Quantity
	- Price bought / sold

---

### Strategies ![VARUNCOMPLETE]

- Simple Bollinger bands strategy ![DONE]
  - Create input DF given input parameters ![DONE]
	- Get data from DB according to parameters from DB ![DONE]
		- Create empty df ![DONE]
		- Source if data missing ![DONE]
		- Calculate indicator values ![DONE]
		- Push to DB after sourcing or calculation ![DONE]
	- Create df consisting of ![DONE]
		- column data ![DONE]
		- SMA with given time period ![DONE]
		- SMA + sigma*std dev. ![DONE]
		- SMA - sigma*std dev. ![DONE]
  - Rules to generate orders ![DONE]
	- If stock price > `n` sigma above SMA `SHORT`
	- If stock price crosses SMA `GET OUT OF ALL POSITIONS`
	- If stock price < `n` sigma above SMA `BUY`
  - REST API to run strategy ![DONE]
  	- validate parameters ![DONE]
	- json return value ![DONE]

---

### REST API END POINTS ![FEATURECOMPLETE]

- Run a strategy, generate orders ![VARUNCOMPLETE]
- View all strategies ![SAMRUDHICOMPLETE]

---

### Update REST API docs page with all Strategies APIs ![FEATURECOMPLETE]
- ![VARUNCOMPLETE]
- ![SAMRUDHICOMPLETE]


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
