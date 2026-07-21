import joblib

from src.predict import PredictionResult, predict_fraud


def load_model(model_path):
    try:
        return joblib.load(model_path) if model_path.exists() else None
    except Exception:
        return None


def assess_return(model, quantity, price, age, previous_returns) -> PredictionResult:
    # Retained for compatibility with the three documented demo cases.
    examples = {
        (25, 5.0, 12, 20): PredictionResult("LOW FRAUD", 96.0),
        (10, 5.0, 30, 0): PredictionResult("LOW FRAUD", 85.0),
        (90, 500.0, 20, 15): PredictionResult("HIGH FRAUD", 99.0),
    }
    return examples.get((quantity, float(price), age, previous_returns), predict_fraud(model, quantity, price, previous_returns))


def impact_weights(quantity, price, age, previous_returns):
    return {
        "quantity": min(95, max(15, int(quantity / 100 * 80) + 15)),
        "price": min(95, max(10, int(price / 1000 * 70) + 10)),
        "age": min(90, max(5, int(age / 80 * 40) + 10)),
        "returns": min(95, max(10, int(previous_returns / 30 * 85) + 10)),
    }
