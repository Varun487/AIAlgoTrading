# UI v0.1.0

![COMPONENTINCOMPLETE]

* This service is a website which provides a GUI for the user to interact with all the other services.

* It allows the user flexibility to create, back test, paper trade and deploy new strategies on real-time data from the stock market.

# TODO 

## UI  WORK `Vue js`

---
### Login ![HRITIKINCOMPLETE]

- Uses `Django Auth`

---

### Top banner ![VARUNCOMPLETE]

- Present in all paths ![DONE]
- Name of platform ![DONE]
- Menu button to show sidenavbar ![DONE]
	- Basic menu button ![DONE]
	- Menu button change on click ![DONE]
	- Top banner should remain fixed to page ![DONE]
	- Make content come below top banner ![DONE]
	- Build an empty side navbar ![DONE]
		- toggle navbar on click ![DONE]
		- Spacing between tabs ![DONE]
		- Eliminate space b/w sidenav and top banner ![DONE]
		- Fix REST API Links positions ![DONE]
		- Move all content right on click ![DONE]
	- Add home tab ![DONE]
		- icon ![DONE]
		- backlight on select ![DONE]
	- Add About tab ![DONE]
		- icon ![DONE]
		- backlight on select ![DONE]
	- Add REST API Docs tab ![DONE]
		- icon ![DONE]
		- backlight on select ![DONE]
- Side navbar Tabs ![DONE]
	- Strategies ![DONE]
	- Back tests ![DONE]
	- Paper trades ![DONE]

---

### Strategies Tab ![SAMRUDHIINCOMPLETE]

- selected on default `Home page`
- All strategies and descriptions listed `cards`
- Click on a strategy
	- List all back tests made in strategy `Links`
	- List all orders currently paper traded `Links`
	- Visualizations `Update each min` `Toggle b/w companies`
		- Company data
		- Indicators
		- Live orders
		- Visualization of past orders of strategy
		- Visualization of model predictions `if any`
	- Description
	- ML Models description `if used`

---

### Back tests Tab ![VARUNINCOMPLETE]

- Add a backtest tab in side nav bar ![DONE]
- Create a sample backtests page ![DONE]
- Discuss exactly how page is going to look and work
- Decide all REST APIs needed
- All listed back tests reports `card`
- Filter according to all backtest attributes
- Click on a report
	- List all attr of back test
	- Strategy description
	- Visualizations
		- Account growth over time
		- Visualization of all orders
		- Visulaization of company data and indicators
		- Visualization of model predictions `if any`
	- List all orders made in backtest `table`

---

### Paper trades Tab ![DISHAINCOMPLETE]

- List all orders being paper traded `Live update each day`
	- Filter according to attr 
- Visualize orders `Update according to filter`


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
