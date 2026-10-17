
# BuildSafe AI — Construction Risk Intelligence Platform

## 1. Project Overview

BuildSafe AI is a prototype construction safety platform that combines computer vision and rule-based risk scoring to support construction-site hazard monitoring.

The application allows users to:
- View a construction hazard dashboard.
- Upload construction-site images for AI object detection.
- View detected objects, bounding boxes and confidence scores.
- Review recorded hazards and their risk levels.
- View recommendations based on the calculated risk level.
- Update hazard statuses.

## 2. Main Features

### AI Image Inspection
Uses a trained YOLO object-detection model to identify supported classes in uploaded images and display annotated results.

### Hazard Risk Assessment
Calculates a risk score using:

`Risk Score = Severity × Likelihood`

Severity and likelihood are each rated from 1 to 5.

The current risk categories are:
- Low
- Medium
- High
- Critical

### Hazard Register
Displays sample hazard records with their category, project, severity, likelihood, status, score and recommended action.

### Dashboard API
Provides summary information such as open hazards, critical hazards, resolved hazards and average risk score.

## 3. Technology Stack

- **Frontend:** HTML, CSS and JavaScript
- **Backend:** Python and FastAPI
- **AI / Computer Vision:** Ultralytics YOLO and Pillow
- **API Documentation:** FastAPI Swagger UI
- **Testing:** pytest
- **Training Environment:** Google Colab
- **Version Control:** Git and GitHub

## 4. Project Structure

```text
Construction-risk-intelligence-platform/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── risk_engine.py
│   │   ├── image_detector.py
│   │   └── database_schema.sql
│   ├── models/
│   │   └── best.pt
│   ├── tests/
│   └── requirements.txt
├── data/
│   └── sample_inspections.csv
├── frontend/
│   └── index.html
├── .gitignore
└── README.md
```

## 5. Setup on Windows

Install Python first, then download and extract the repository.

Open Command Prompt in the project folder and run:

```bash
cd backend
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Keep this terminal running.

Open a second terminal in the project folder and run:

```bash
python -m http.server 5173 --directory frontend
```

Open the dashboard:

`http://localhost:5173`

Open the API documentation:

`http://127.0.0.1:8000/docs`

## 6. Main API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Basic API information |
| GET | `/health` | Health check |
| GET | `/api/risks` | List recorded hazards |
| GET | `/api/risks/{hazard_id}` | Retrieve a hazard |
| POST | `/api/risks` | Create a hazard |
| PATCH | `/api/risks/{hazard_id}/status` | Update hazard status |
| POST | `/api/analyze` | Calculate risk and recommendation |
| POST | `/api/analyze-image` | Analyze an uploaded image |
| GET | `/api/dashboard` | Retrieve dashboard statistics |

## 7. Model Evaluation

The trained model was evaluated on a held-out test split.

- Test images: 82
- Test instances: 806
- Precision: 61.4%
- Recall: 38.8%
- mAP@50: 43.0%
- mAP@50–95: 29.5%

These results indicate that the prototype can detect some supported objects but may miss objects or produce incorrect detections.

## 8. Current Limitations

- The recorded hazard list uses illustrative in-memory sample records.
- Hazard status changes may be lost when the backend restarts.
- Image detection is limited to the classes learned by the model.
- Object detections do not automatically confirm every construction hazard.
- Risk scores are calculated from supplied severity and likelihood values.
- The model is not certified for safety-critical decisions.

All AI results require human verification. No detection does not mean a site is safe.

## 9. Future Improvements

- Integrate a persistent database for hazard records.
- Improve model accuracy with additional representative training data.
- Connect image detections to a reviewed hazard-reporting workflow.
- Add user authentication and role-based permissions.
- Add inspection history, reporting and deployment support.

## 10. Conclusion

BuildSafe AI demonstrates a prototype workflow for construction hazard recording, rule-based risk assessment, and AI-assisted image inspection. It provides a foundation for further development and must be validated before any real-world safety use.
