# DATAFEEDER v1.0

![COMPONENTINCOMPLETE]

* Used to source real-time minute scale data from over 5000 stocks in the stock market.

* Perform very fast, basic calculations on the raw data.

# TODO v1.0


## DATAFEEDER WORK

---

### DB ![SAMRUDHICOMPLETE]

- Company ![DONE]
- Time stamp ![DONE]
- Immutable Data ![DONE]
- Calculated Candle stick Data ![DONE]
- Indicators ![DONE]

---

### REST API endpoints ![FEATUREINCOMPLETE] 

#### Company ![DISHAINCOMPLETE]

- List all companies in DB ![DONE] 
- Get a particular company's details 
- Filter company according name, sector, ticker 
- Add a company
- Delete a company
- Modify attr of a company

#### Immutable data ![HRITIKINCOMPLETE]

- List immutable data in DB
	- Filter according to open, high, low, close, volume, company, time period values

#### Indicators ![VARUNINCOMPLETE]

- List indicator data
	- Filter according to company, time period values

#### Derived candle stick data ![SAMRUDHIINCOMPLETE]

- List derived data
	- Filter according to open, high, low, close, volume, company, time period, aggregation time periods list values

---

### Sourcing functions ![VARUNINCOMPLETE]

- On demand (function) ![INCOMPLETE]
    - Parameters ![DONE]
    	- Company `List` ![DONE]
        - data collection window `Start Datetime and End Datetime` ![DONE]
        - Provider - AlphaVantage / Yahoo Finance ![DONE]
		- Candle stick time period ![DONE]
		- slice ![DONE]
    - Handle bad requests ![DONE]
	- Get data ![DONE]
		- Yahoo finance ![DONE]
			- Daily time period ![DONE]
			- Within time window ![DONE]
			- For all companies in list ![DONE]
				- Inform if company data not found ![DONE]
			- Push to DB ![DONE]
				- Resolve time stamp schema change ![DONE]
				- Check if data not in DB before inserting data ![DONE]
		- AlphaVantage ![DONE]
	  		- Modify req & check if req is correct ![DONE]
			- Source data from AlphaVantage with parameters ![DONE]
			- Push to DB ![DONE]
			  - Check if data not in DB before inserting data ![DONE]
- Real time `Only Yahoo! Finance` ![INCOMPLETE]
    - Call on demand function as a cron job every 24hrs ![INCOMPLETE]

---

### Indicators calc functions ![VARUNINCOMPLETE]

- Parameters
  - Company
  - time periods `Start data and end date`
- Push to DB
- SMA 
- Std Dev
- Call Indicator functions on sourced data ![INCOMPLETE]

---

### Derive Indicator values for different time periods ![HRITIKINCOMPLETE]

- Parameters
  - Company
  - time periods `Start data and end date`
  - aggregation time period `List`
- SMA 
- Std Dev 

---

### Derive candle sticks for different time periods ![SAMRUDHIINCOMPLETE]

- Parameters
  - Company
  - time window `Start data and end date`
  - aggregation time period `List`
- Push to DB

---

### Add all REST APIs to API docs page ![VARUNINCOMPLETE] ![DISHAINCOMPLETE]

---

### Automated testing ![VARUNINCOMPLETE] ![DISHAINCOMPLETE]

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
