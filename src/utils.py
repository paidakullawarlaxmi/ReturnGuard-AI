def print_report(user_id, is_fraud, score):
    """Print a compact terminal report for a prediction."""
    status = "Fraud" if is_fraud else "Safe"
    print("=" * 40)
    print("RETURNGUARD AI REPORT")
    print("=" * 40)
    print(f"User ID : {user_id}")
    print(f"Status  : {status}")
    print(f"Score   : {score}")
    print("=" * 40)
