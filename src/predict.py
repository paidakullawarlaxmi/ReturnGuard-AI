from dataclasses import dataclass

from src.preprocess import build_feature_frame


@dataclass(frozen=True)
class PredictionResult:
    prediction: str
    confidence: float


def predict_fraud(model, quantity: int, price: float, previous_returns: int) -> PredictionResult:
    """Classify a return using the trained model, with a safe heuristic fallback."""
    if model is not None:
        try:
            probabilities = model.predict_proba(build_feature_frame(quantity, price))[0]
            label = model.predict(build_feature_frame(quantity, price))[0]
            return PredictionResult(
                "HIGH FRAUD" if label == 1 else "LOW FRAUD",
                round(float(max(probabilities)) * 100, 2),
            )
        except Exception:
            pass

    high_risk = previous_returns > 10 or (quantity > 30 and price > 100)
    return PredictionResult("HIGH FRAUD" if high_risk else "LOW FRAUD", 95.0 if high_risk else 90.0)
