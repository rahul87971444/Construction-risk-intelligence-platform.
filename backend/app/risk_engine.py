"""
Site Risk Agent: construction hazard scoring and recommendations.

Risk score = severity x likelihood.
Both inputs use a scale of 1 to 5.
"""


def calculate_risk(severity: int, likelihood: int) -> dict:
    """Calculate a risk score and classify its level."""

    if not 1 <= severity <= 5:
        raise ValueError("Severity must be between 1 and 5.")

    if not 1 <= likelihood <= 5:
        raise ValueError("Likelihood must be between 1 and 5.")

    score = severity * likelihood

    if score <= 4:
        level = "Low"
    elif score <= 9:
        level = "Medium"
    elif score <= 16:
        level = "High"
    else:
        level = "Critical"

    return {
        "severity": severity,
        "likelihood": likelihood,
        "risk_score": score,
        "risk_level": level,
    }


def create_recommendation(hazard: str, risk_level: str) -> str:
    """Generate an initial rule-based safety recommendation."""

    recommendations = {
        "Low": "Continue routine monitoring.",
        "Medium": "Inspect the area and apply preventive measures.",
        "High": (
            "Prioritize corrective action and request "
            "a supervisor review."
        ),
        "Critical": (
            "Escalate immediately and have a competent "
            "person assess the hazard before the activity continues."
        ),
    }

    action = recommendations.get(
        risk_level,
        "Review the hazard and consult a qualified safety professional.",
    )

    return f"{hazard}: {action}"
