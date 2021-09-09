# UI v0.1.0

![componentincomplete]

- This service is a website which provides a GUI for the user to interact with all the other services.

- It allows the user flexibility to create, back test, paper trade and deploy new strategies on real-time data from the stock market.

# TODO

## Common ![dishacomplete]
- Header ![DONE]
- Footer ![DONE]
  - To use: import FooterBase from "relative path"
- Add and configure all the pages with header ![DONE]
- Add and configure the logout button for all pages ![DONE]
- Logically connected the Landing and Login pages ![DONE]
- Adjustments to the framework to incorporate uniform design ![DONE]
      
## All strategies page ![dishacomplete]
- design ![DONE]
- content ![DONE]
- implementation - frontend (VueJS) ![DONE]
  - Add scaled layout designs ![DONE]
  - Minor modification to render uniform dynamic layout ![DONE]
- implementation - backend (Vuex and REST API) ![DONE]
  - Re-adjust to accomodate new strategy 
  - Implement backend logic for lstm strategy
  - Implement common logic for rendering uniform design
  

## Strategy page ![samrudhiincomplete]
- design ![DONE]
- Per Strategy Info ![DONE]
  - frontend (VueJS)
  - backend (Vuex and REST API)
- Backtester Section ![DONE]
  - frontend (VueJS)
  - backend (Vuex and REST API)
  - Linking backtester page to the specific backtester report page
- Paper Trade Section
  - frontend (VueJS)
  - backend (Vuex and REST API)
  - Linking backtester page to the specific backtester report page

## REST API Documentation page ![dishacomplete]
- design ![DONE]
- implementation ![DONE]
  - frontend (VueJS) ![DONE]
  - backend (Vuex and REST API)

## Backtest report page ![hritikincomplete]
- design ![DONE]
- implementation
  - frontend (VueJS)
  - backend (Vuex and REST API)

## Login page ![featureincomplete]
- design ![DONE] ![dishacomplete]
- implementation
  - frontend (VueJS) ![DONE] ![dishacomplete]
  - backend (Vuex and REST API) ![hritikincomplete]

## Landing page ![samrudhiincomplete]
- design 
- implementation
  - frontend (VueJS)
  - backend (Vuex and REST API)
  - Cookie for persistent login

## Paper trading page ![dishaincomplete]
- design ![DONE]
- implementation - frontend (VueJS) ![DONE]
   - Redo design ![DONE]
   - Fix front-end layout ![DONE]
   - Implemenet final elements ![DONE]
- implementation - backend (Vuex and REST API)

## 404 Not Found Error page ![hritikcomplete]
- design ![hritikcomplete]
- Implementation ![hritikcomplete]


## Automated testing
- All strategies page
- Strategy page
- REST API docs
- Backtest report page
- Login page
- Landing page
- Paper trading page
- 404 Not Found error page

## Remaining work
- BACK BUTTON
- Both strategies need to be displayed
- When clicking `go` on a strategy, id of both strategies must be updated in state 
- In strategy data page
  - Limit backtests displayed 
  - Display live paper trades
  - Id of backtest for backtest report should be updated 
- Backtest report trades -> DEBUG
- Paper Trade page -> NOT COMPLETE
- Filter button and navigation of backtests and paper trades `LOW Priority`
- Trade data Page
- Intimate user in case of wrong User id, password
- Cookie for persistent login
- HTML and CSS work
- Change the picture in Landing Page





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
