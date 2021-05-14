# PAPERTRADER v1.0

![COMPONENTINCOMPLETE]

* This is used to test strategies in real-time market scenarios after a strategy has performed well in back testing.

* It tracks and evaluates orders generated by multiple strategies in real-time market conditions and provides various performance metrics for both strategies and orders.

# TODO v1.0

---

## PAPERTRADER  WORK

---

### Tracks live orders `Runs every min` ![SAMRUDHIINCOMPLETE] ![DISHAINCOMPLETE]

- Get all paper trader orders
- Evaluate loss / profit of order according to latest company data `Update in DB`
- After order is completed, change owner `Update in DB`

---

### Genrating orders `Runs every min` ![VARUNINCOMPLETE]

- Get latest data of all companies
- Run all strategies on all relevant data `Returns orders`
- Set Profit / Loss and owner fileds of orders
- Push orders to DB

---


### REST APIs ![HRITIKINCOMPLETE]

- Get all current paper traded orders
- Filter orders according to all relevant criteria

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
