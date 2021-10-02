# DEV OPS v0.1.0

![componentcomplete]

- Building the development and production environments

- Automated deployment to a VM

- Initialization and deployment scripts

# TODO

## Development ![varuncomplete]
- Containers ![done]
  - db ![done]
  - rest api ![done]
  - ui ![done]
- Hot restart functionality for ui and restapi ![done]
- rebuild from scratch test ![done]
- Update READMEs ![done]
- UI unable to call restapis ![bugfixed]
- Unable to see /admin from UI ![bugfixed]

## Production ![varuncomplete]
- Containers ![done]
  - db ![done]
  - rest api ![done]
  - ui ![done]
  - nginx ![done]
- Make nginx serve both ui and rest api ![done]
- Buy a domain ![done]
- Run paper trade script, test paper trade APIs ![done]
- Serve ui from static files ![done]
- Get Django ready for production ![done]
  - Checklist on website ![done]
  - Check command ![done]
  - Settings.py changes ![done]
  - Different settings for production and development ![done]
- deploy on VM ![done]
  - Check for all data to be sent to vm not in git ![done]
    - Push db data ![done]
    - Push Models data ![done]
  - Install docker ![done]
  - Install docker compose ![done]
  - Build images ![done]
  - Run the server ![done]
  - Change allowed hosts variable ![done]
  - Run docker process in background ![done]
  - test ![done]

## Deployment scripts ![varuncomplete]
- Automated deployment to VM from local machine `firebase` ![done]

## Remaining
- SSL certification for server
  - Take care of ssl checks in django
  - Testing
- Host updated restapi

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
