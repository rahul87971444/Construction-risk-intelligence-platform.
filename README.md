# Construction Risk Intelligence Platform

**BuildSafe AI — Infosys Springboard Intensive Program**

## Project Overview

An AI-assisted platform designed to monitor construction-site risks, analyze hazards, calculate risk scores, and provide actionable safety recommendations.

This project is being developed for **Milestone 1: Site Risk Monitoring & Hazard Detection**.

## Objectives

- Monitor construction-site information.
- Identify potential safety hazards.
- Calculate risk scores using severity and likelihood.
- Provide recommendations for corrective action.
- Display hazard information through a dashboard.
- Build toward AI-powered image-based hazard detection.

## Technology Stack

| Component | Technology |
|---|---|
| Backend API | FastAPI |
| Programming | Python |
| Object detection | YOLO |
| Image processing | OpenCV |
| Frontend | React.js |
| UI styling | Tailwind CSS |
| Agent workflow | LangGraph |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Charts | Recharts |
| Version control | Git and GitHub |

## Current Implementation

- FastAPI application.
- Health-check endpoint.
- Sample site-risk records.
- Hazard listing and individual hazard lookup.
- New hazard creation.
- Hazard status updates.
- Severity × likelihood risk scoring.
- Rule-based safety recommendations.
- Dashboard statistics endpoint.

## Risk Scoring

Risk score = Severity × Likelihood.

Both severity and likelihood use a scale from 1 to 5.

- 1–4: Low
- 5–9: Medium
- 10–16: High
- 17–25: Critical

These are initial project-defined thresholds for demonstration purposes.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Application information |
| GET | `/health` | Health check |
| GET | `/api/risks` | List hazards |
| GET | `/api/risks/{hazard_id}` | Retrieve a hazard |
| POST | `/api/risks` | Create a hazard |
| PATCH | `/api/risks/{hazard_id}/status` | Update hazard status |
| POST | `/api/analyze` | Analyze a hazard |
| GET | `/api/dashboard` | Retrieve dashboard statistics |

## Project Status

**Version 0.1 — Backend foundation**

Image-based hazard detection, database persistence, frontend dashboard, and agent orchestration are planned for subsequent development stages.
## Day 2 Progress

### Completed
- Set up the Python backend using FastAPI.
- Created the initial Site Risk Agent logic.
- Added severity and likelihood based risk scoring.
- Created API endpoints to list, add, and update construction hazards.
- Added an API endpoint for dashboard statistics.
- Started the backend locally using Uvicorn.
- Prepared the API documentation for testing.

### Next Steps
- Test all backend API endpoints.
- Build the React dashboard.
- Integrate construction-site image detection using YOLO and OpenCV.
- Add database storage for hazard records.
- Improve the Site Risk Agent and its recommendations.

### Current Status
Backend foundation created. API testing and frontend development are in progress.
## Disclaimer

This educational prototype supports risk awareness and decision-making. It does not replace professional safety inspections or official regulatory compliance assessments.
