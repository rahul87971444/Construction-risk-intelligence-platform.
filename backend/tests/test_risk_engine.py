import pytest

from app.risk_engine import calculate_risk, create_recommendation


def test_low_risk():
    result = calculate_risk(1, 2)

    assert result["risk_score"] == 2
    assert result["risk_level"] == "Low"


def test_medium_risk():
    result = calculate_risk(3, 3)

    assert result["risk_score"] == 9
    assert result["risk_level"] == "Medium"


def test_high_risk():
    result = calculate_risk(4, 3)

    assert result["risk_score"] == 12
    assert result["risk_level"] == "High"


def test_critical_risk():
    result = calculate_risk(5, 4)

    assert result["risk_score"] == 20
    assert result["risk_level"] == "Critical"


def test_invalid_severity():
    with pytest.raises(ValueError):
        calculate_risk(6, 3)


def test_invalid_likelihood():
    with pytest.raises(ValueError):
        calculate_risk(3, 0)


def test_recommendation():
    result = create_recommendation(
        "Unprotected scaffold edge",
        "Critical",
    )

    assert "Unprotected scaffold edge" in result
    assert "Escalate immediately" in result
