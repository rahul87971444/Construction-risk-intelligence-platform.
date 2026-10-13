from typing import Literal

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.risk_engine import calculate_risk, create_recommendation

app = FastAPI(
    title="BuildSafe AI - Construction Risk Intelligence",
    description=(
        "Infosys Springboard Milestone 1: "
        "Site Risk Monitoring and Hazard Detection"
    ),
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Status = Literal["Open", "In Progress", "Resolved"]


class HazardInput(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    category: str = Field(min_length=2, max_length=100)
    project: str = Field(min_length=2, max_length=150)
    severity: int = Field(ge=1, le=5)
    likelihood: int = Field(ge=1, le=5)
    description: str = Field(default="", max_length=1000)


class HazardUpdate(BaseModel):
    status: Status


# Illustrative demonstration records, not live site data.
hazards = [
    {
        "id": 1,
        "title": "Unprotected scaffold edge",
        "category": "Working at Height",
        "project": "North Tower Development",
        "severity": 5,
        "likelihood": 4,
        "description": "Edge protection needs inspection.",
        "status": "Open",
    },
    {
        "id": 2,
        "title": "Material stored in access path",
        "category": "Housekeeping",
        "project": "Metro Line Extension",
        "severity": 3,
        "likelihood": 3,
        "description": "Materials may obstruct pedestrian movement.",
        "status": "Open",
    },
    {
        "id": 3,
        "title": "Excavation barricade missing",
        "category": "Excavation",
        "project": "Harbour Logistics Hub",
        "severity": 4,
        "likelihood": 4,
        "description": "Excavation perimeter needs protection.",
        "status": "Open",
    },
    {
        "id": 4,
        "title": "Exposed temporary cable",
        "category": "Electrical",
        "project": "North Tower Development",
        "severity": 4,
        "likelihood": 3,
        "description": "Cable routing requires inspection.",
        "status": "In Progress",
    },
    {
        "id": 5,
        "title": "Forklift pedestrian conflict",
        "category": "Equipment",
        "project": "Metro Line Extension",
        "severity": 5,
        "likelihood": 4,
        "description": "Review pedestrian and vehicle separation.",
        "status": "Open",
    },
]


def enrich_hazard(hazard: dict) -> dict:
    """Add calculated risk information to a hazard record."""

    result = calculate_risk(
        hazard["severity"],
        hazard["likelihood"],
    )

    return {
        **hazard,
        **result,
        "recommendation": create_recommendation(
            hazard["title"],
            result["risk_level"],
        ),
    }


@app.get("/")
def home():
    return {
        "application": "BuildSafe AI",
        "status": "running",
        "api_docs": "/docs",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/api/risks")
def list_risks():
    return [enrich_hazard(hazard) for hazard in hazards]


@app.get("/api/risks/{hazard_id}")
def get_risk(hazard_id: int):
    for hazard in hazards:
        if hazard["id"] == hazard_id:
            return enrich_hazard(hazard)

    raise HTTPException(status_code=404, detail="Hazard not found.")


@app.post("/api/risks", status_code=201)
def add_risk(item: HazardInput):
    new_id = max((h["id"] for h in hazards), default=0) + 1

    hazard = {
        "id": new_id,
        **item.model_dump(),
        "status": "Open",
    }

    hazards.append(hazard)
    return enrich_hazard(hazard)


@app.patch("/api/risks/{hazard_id}/status")
def update_risk_status(hazard_id: int, item: HazardUpdate):
    for hazard in hazards:
        if hazard["id"] == hazard_id:
            hazard["status"] = item.status
            return enrich_hazard(hazard)

    raise HTTPException(status_code=404, detail="Hazard not found.")


@app.post("/api/analyze")
def analyze_hazard(item: HazardInput):
    risk = calculate_risk(item.severity, item.likelihood)

    return {
        **item.model_dump(),
        **risk,
        "recommendation": create_recommendation(
            item.title,
            risk["risk_level"],
        ),
    }


@app.get("/api/dashboard")
def dashboard():
    enriched = [enrich_hazard(h) for h in hazards]

    open_hazards = [
        h for h in enriched if h["status"] != "Resolved"
    ]

    critical_hazards = [
        h for h in open_hazards
        if h["risk_level"] == "Critical"
    ]

    projects = {h["project"] for h in hazards}

    return {
        "active_projects": len(projects),
        "open_hazards": len(open_hazards),
        "critical_hazards": len(critical_hazards),
        "resolved_hazards": sum(
            h["status"] == "Resolved" for h in hazards
        ),
        "risk_score_average": (
            round(
                sum(h["risk_score"] for h in open_hazards)
                / len(open_hazards),
                1,
            )
            if open_hazards else 0
        ),
        "risk_method": "Severity x Likelihood",
        "data_type": "Illustrative sample records",
    }
