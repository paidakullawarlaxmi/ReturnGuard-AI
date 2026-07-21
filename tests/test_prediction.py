from src.predict import predict_fraud


def test_high_return_volume_is_high_risk_without_a_model():
    result = predict_fraud(None, quantity=2, price=10.0, previous_returns=11)
    assert result.prediction == "HIGH FRAUD"


def test_ordinary_return_is_low_risk_without_a_model():
    result = predict_fraud(None, quantity=2, price=10.0, previous_returns=0)
    assert result.prediction == "LOW FRAUD"
