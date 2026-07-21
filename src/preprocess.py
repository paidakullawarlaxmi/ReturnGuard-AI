import pandas as pd


MODEL_FEATURES = ["Quantity", "UnitPrice"]


def build_feature_frame(quantity: int, price: float) -> pd.DataFrame:
    """Build the feature frame expected by the saved classifier."""
    return pd.DataFrame([{"Quantity": quantity, "UnitPrice": price}], columns=MODEL_FEATURES)
