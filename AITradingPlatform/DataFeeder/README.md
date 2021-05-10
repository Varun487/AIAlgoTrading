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

#### Time Stamp ![SAMRUDHIINCOMPLETE]

- All time stamps in DB
- Add a time stamp
- Delete a time stamp

#### Immutable data and Calculated data![HRITIKINCOMPLETE]

- Filter according to open, high, low, close, volume, company, time period values

#### Indicators ![VARUNINCOMPLETE]

- Filter according to company, time period values

#### Sourcing data ![VARUNINCOMPLETE]

- Ondemand data api call -> List of companies, time period, provider
- Add a company to real time list
- Remove a comapny from real time list

#### Derived candle stick data ![SAMRUDHIINCOMPLETE]

- Filter according to open, high, low, close, volume, company, time period, aggregation time periods list values

---

### Sourcing functions ![VARUNINCOMPLETE]
- On demand (functions)
    - Parameters
    	- Company `List`
        - data collection window `Start Datetime and End Datetime`
        - Provider - AlphaVantage / Yahoo Finance
		- Candle stick time period
    - Calculate indicators
    - Push to DB

- Real time
    - Call on demand function in an infinite loop

---

### Indicators calc functions ![DISHAINCOMPLETE]

- Parameters
  - Company
  - time periods `Start data and end date`
  - Push to DB
    - SMA 
    - Std Dev 

---

### Indicators `derived` calc functions ![HRITIKINCOMPLETE]

- Parameters
  - Company
  - time periods `Start data and end date`
  - aggregation time period `List`
    - SMA 
    - Std Dev 

---

### Different `derived` candle stick time periods ![SAMRUDHIINCOMPLETE]

- Parameters
  - Company
  - time periods `Start data and end date`
  - aggregation time period `List`

---

### Add all REST APIs to API docs page ![VARUNINCOMPLETE]

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
