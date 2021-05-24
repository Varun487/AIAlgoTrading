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

#### Immutable data ![HRITIKCOMPLETE]

- List immutable data in DB ![DONE] 
	- Filter according to open, high, low, close, volume, company, time period values ![DONE] 

#### Indicators ![VARUNCOMPLETE]

- List indicator data ![DONE]
  - Create an endpoint `indicatorsdata/` ![DONE]
  - Handle edge cases ![DONE]
  	- Return `Invalid request` message if wrong parameters passed to req ![DONE]
	- Return `No data present that fits all conditions` message if no data found ![DONE]
  - Validate request parameters ![DONE]
  - Filter according all attr ![DONE]
	- Name ![DONE]
	- Value `Range` ![DONE]
	- Column ![DONE]
	- indicator time period ![DONE]
	- Candle Stick ![DONE]
	  - company `ticker` ![DONE]
	  - time_stamp `range` ![DONE]
	  - time_period ![DONE]

#### Derived candle stick data ![SAMRUDHICOMPLETE]

- List derived data
  - Create an endpoint `getcandlestick/` ![DONE]
  - Validate the req_body ![DONE]
  - Filter according to ![DONE]
	- company ![DONE]
	- time period ![DONE]
	- aggregation time periods list values ![DONE]
	
---

### Sourcing historical data on demand ![VARUNCOMPLETE]

- On demand (function) ![DONE]
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
	- Calculate indicators on sourced data ![DONE]
		- Separate `ondemand` function and api ![DONE]
		  - Remove naive datetimes ![DONE]
		  - Suppress pandas warning ![DONE]
		  - Make sure df is in ascending order of dates ![DONE]
		- Make functions which take a dataframe as input and calculate indicators ![DONE]
		  - SMA ![DONE]
		  - Standard dev. ![DONE]
		- Push indicators calculated to DB ![DONE]
	- Cannot uniquely identify indicator data ![BUGFIXED]

---

### Sourcing data real time ![VARUNCOMPLETE]
`Only Yahoo! Finance`

- Create a test cron job ![DONE]
	- Runs every 24 hrs ![DONE]
- Refactor files ![DONE]
- Create a python script to get the latest data on all companies present in DB through Yahoo finance ![DONE]
  - Get all companies from DB ![DONE]
  - Filter to get all companies from Yahoo! finance ![DONE]
  - Get data from last collected till today for each company ![DONE]
    - Collect immutable data ![DONE]
  - Calculate Indicators ![DONE]
	- Default indicators after sourcing ![DONE]
  - Push data + indicators to DB ![DONE]
- Run the script as a cron job every 24hrs ![DONE]

---

### Derive Indicator values for different time periods ![HRITIKCOMPLETE]

- Parameters ![DONE]
  - Company  ![DONE]
  - time periods `Start data and end date` ![DONE]
  - aggregation time period `List` ![DONE]
  - indicator name ![DONE]

-	Validate the req_body ![DONE]
- Calculating indicator SMA ![DONE]
- Calculating indicator Std Dev ![DONE] 
- Push to DB ![DONE]



---

### Derive candle sticks for different time periods ![SAMRUDHICOMPLETE]

- Parameters ![DONE]
  - Company  ![DONE]
  - time window `Start data and end date` ![DONE]
  - aggregation time period `List` ![DONE]

- Validate the req_body ![DONE]
- Call ondemand func ![DONE]
- get immutable data from db  ![DONE]
  - filter acc to company, start date, end date, original_time_period ![DONE]
- tumbling window on calculate_time_period ![DONE]
  - oldest open price ![DONE]
  - latest close price ![DONE]
  - maximum of high price ![DONE]
  - minimum of low price ![DONE]
  - addition of volume ![DONE]

- Push to DB ![DONE]
  - if not already present ![DONE]

---

### Create REST API docs page ![VARUNCOMPLETE] 

- Setup website ![DONE]
	- Change title ![DONE]
	- Add a different favicon ![DONE]
	- Refactor webapp, decide organization of componets, routers and views ![DONE]
	- Add Vuex ![DONE]
	- Fix navbar ![DONE]
		- Add a title ![DONE]
		- Sepaprate links component ![DONE]
		- CSS and format for all links + navbar ![DONE]
	- Make the favicon have a transparent background ![DONE]
- Create API Docs page ![DONE]
	- Decide format for page and each API ![DONE]
	- Build components for api page ![DONE]
		- REST API title ![DONE]
		- Note ![DONE]
		- List of endpoints overview ![DONE]
		- SITE NOT RENDERING PROPERLY IN PRODUCTION!!! ![BUGFIXED]
	- Endpoint Description ![DONE]
		- Get / Post, endpoint link ![DONE]
		- Descripiton of endpoint function ![DONE]
		- Descripiton of endpoint parameters ![DONE]
		- Sample correct request url ![DONE]
		- Sample correct request body ![DONE]
		- Sample correct output ![DONE]
		- Sample failed output ![DONE]
		- Fix all endpoints description items ![DONE]
	- Fix links in endpoints overview list ![DONE]

---

### Update REST API docs page with all DataFeeder APIs
- ![VARUNCOMPLETE]
- ![DISHAINCOMPLETE]
- ![HRITIKINCOMPLETE]
- ![SAMRUDHIINCOMPLETE]

---

### Automated testing ![ALLINCOMPLETE]
- Build infra for UI, REST API and code block testing ![VARUNINCOMPLETE] 
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
