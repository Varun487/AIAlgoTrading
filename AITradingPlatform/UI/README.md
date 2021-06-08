# UI v0.1.0

![COMPONENTINCOMPLETE]

- This service is a website which provides a GUI for the user to interact with all the other services.

- It allows the user flexibility to create, back test, paper trade and deploy new strategies on real-time data from the stock market.

# TODO

## UI WORK `Vue js`

---

### Login ![HRITIKINCOMPLETE]

- Uses `Django Auth`
  - create login auth REST API
- Fix login button `CSS`
- Don't render sidebar in login page
- Don't render sidebar nav button on top-left in login page
- Redirect all other urls to login page if not logged in

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

---

### Strategies Tab ![SAMRUDHIINCOMPLETE]

- selected on default `Home page` ![DONE]
- All strategies and descriptions listed `cards` ![DONE]
- Click on a strategy
  - List all back tests made in strategy `Links` 
  - List all orders currently paper traded `Links`
  <!-- - Visualizations `Update each min` `Toggle b/w companies`
    - Company data
    - Indicators
    - Live orders
    - Visualization of past orders of strategy
    - Visualization of model predictions `if any` -->
  - Description ![DONE]
  - ML Models description `if used`

---

### Back tests Tab ![VARUNINCOMPLETE]

- Add a backtest tab in side nav bar ![DONE]
- Create a sample backtests page ![DONE]
- install axios ![DONE]
- Decide exactly how page is going to look and work ![DONE]
- Decide all REST APIs needed ![DONE]
- Build Main backtests page ![DONE]
  - Title ![DONE]
  - Info about page and intro to backtests ![DONE]
  - Filter criteria `Form` ![DONE]
  - All backtests conducted `Cards` ![DONE]
  - api call to get all backtests ![DONE]
  - set global state ![DONE]
  - display all data sourced in cards ![DONE]
  - Display multiple cards side by side ![DONE]
  - Turn cursor to pointer on hover over cards ![DONE]
  - Click on a card function - leads to backtest report page of that backtest ![DONE]
    - Make API return backtest id ![DONE]
  - Give id as key while rendering cards in v-for loop ![DONE]
    - Make an API to return backtest info given id ![DONE]
    - Set backtest id in state when clicking on backtest ![DONE]
  - Make reset button function ![DONE]
  - Empty out all fields ![DONE]
  - Reset filtered reports to reports ![DONE]
  - Filter cards function `filter by` ![DONE]
    - Start date ![DONE]
    - End Date ![DONE]
    - Max Risk ![DONE]
    - Time Period ![DONE]
    - Company ![DONE]
    - Strategy ![DONE]
    - Dimension ![DONE]
- Build backtest report page ![INCOMPLETE]
  - Go back button ![DONE]
  - Title ![DONE]
  - Backtest report info ![DONE]
    - Create section ![DONE]
    - Make API call to get report info ![DONE]
    - Set global state ![DONE]
    - create getters ![DONE]
    - Display info ![DONE]
  - Visualization of account growth ![DONE]
	- Decide data required ![DONE]
	- Create API `backtester/getordersbyreportid` ![DONE]
	- Make API call ![DONE]
	- Set global state ![DONE]
	- Create getter ![DONE]
	- Chart account size ![DONE]
  - Visualization of company data + indicators + Orders placed ![INCOMPLETE]
	- Run Multiple backtests to test data ![INCOMPLETE]
	- Title 
	- Visualize company data
		- Get company data
		- Set global state
		- Create a getter
  - Orders filter form
  - Table of orders
- Fix duplicate keys in REST API docs ![BUGFIXED]
- Account size chart size doesn't revert back after side nav is removed ![BUG]

---

### Paper trades Tab ![DISHAINCOMPLETE]

- Decide basic layout and design of paper trader tab ![DONE]
- Add a paper trader tab in side nav bar ![DONE]
- Layout (Main) ![DONE] 
  - Title ![DONE]
  - About ![DONE]
  - Mid Section ![DONE]
  - Filter Section ![DONE]
  - Live Trades Section (Cards) ![DONE]
- Layout (Report)
- List all orders being paper traded `Live update each day`
- Filter cards function `filter by` 
    - Start date 
    - End Date 
    - Order Type 
    - Company
    - Strategy
- Visualize orders `Update according to filter`

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
[meetingincomplete]: https://img.shields.io/badge/MEETING-INCOMPLETE-red
[docincomplete]: https://img.shields.io/badge/DOC-INCOMPLETE-red
[doccomplete]: https://img.shields.io/badge/DOC-COMPLETE-brightgreen
