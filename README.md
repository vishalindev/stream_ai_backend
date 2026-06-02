# Stream AI Backend (FastAPI)

Monolithic FastAPI backend organized by domain modules under `app/`. Each module keeps its own router/service (and repository where needed), while shared Pydantic schemas, in-memory models, Redis cache utilities, settings, security, logging, and database bootstrap code stay centralized.

## Structure

```text
app/
├── main.py
├── core/
│   ├── config.py
│   ├── database.py
│   ├── logging.py
│   ├── redis.py
│   └── security.py
├── modules/
│   ├── admin/
│   ├── camera/
│   ├── dashboard/
│   ├── identity/
│   ├── mobile/
│   ├── notification/
│   ├── platformuser/
│   ├── reports/
│   ├── rule/
│   └── zone/
├── shared/
│   ├── models/
│   ├── schemas/
│   ├── utils/
│   └── constants.py
└── tests/
```

## Features

- JWT auth: `POST /auth/token` with the seeded `admin` / `admin123` development user.
- Pydantic request models via `DomainPayload` and shared response/pagination schemas.
- Redis-backed read caching with graceful fallback when Redis is unavailable.
- Domain grouped legacy endpoints for Employee, Plant, Platform User/RBAC, Camera, Zone, Rule, Notification, Dashboard, and Reports.
- Backward-compatible `src.main:app` entrypoint that re-exports `app.main:app`.

## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Legacy Endpoint Groups

- Employee Management: `/Employee/createuser`, `/Employee/updateuser`, `/Employee/fetchusers`
- Plant Infrastructure Setup: `/Plant/createplant`, `/Plant/updateplant`, `/Plant/fetchplant`
- Platform User & RBAC Administration: `/PlatFormUser`, `/PlatFormUser/updateplatformuser`, `/PlatFormUser/fetchallplatformusers`, `/PlatFormUser/fetchroleall`, `/PlatFormUser/fetchdesignationall`
- Camera & Video Assets: `/Camera/addcamera`, `/Camera/updatecamera`, `/Camera/fetchcamerasall`, `/Camera/departmentwithcamera`
- Zones & Area Mapping: `/Zone/createzone`, `/Zone/updatezone`, `/Zone/fetchzoneall`, `/Zone/fetchzonebyid`, `/Zone/createzonecode`, `/Zone/zonecameramap`, `/Zone/zonerulemap`, `/Zone/fetchzonebytabid`
- Smart Rules Engine: `/Rule/fetchruleall`, `/Rule/addnotificationrule`, `/Rule/updaterule`, `/Rule/fetchrulebyunitid`
- Real-time Notifications & Grouping: `/NotificationGroup/addnotificationgroup`, `/NotificationGroup/updatenotificationgroup`, `/NotificationGroup/fetchnotificationgroupall`, `/Notification/fetchnotificationbycameraid`, `/Notification/fetchnotificationbyid`, `/Notification/getnotificationarray`, `/Notification/fetchnotification`, `/Notification/notificationstatusupdate`
- Live Dashboard & Workspaces: `/Dashboard/fetchanomalycameras`, `/Dashboard/fetchunitsall`, `/Dashboard/fetchusertab`, `/Dashboard/createusertab`, `/Dashboard/deleteusertab/`
- Analytical Reports: `/Reports/fetchnotificationbydate`, `/Reports/fetchnoticiationvehicle`, `/Reports/fetchnoticiationface`
