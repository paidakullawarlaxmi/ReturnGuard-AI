def calculate_fraud_score(transaction):
    score = 0

    if transaction["return_count"] > 5:
        score += 40

    if transaction["order_value"] < 500 and transaction["return_count"] > 3:
        score += 30

    if transaction["order_value"] > 10000:
        score += 20

    if transaction["reason"] in ["not liked", "changed mind"]:
        score += 10

    return score


def is_fraud(transaction):
    score = calculate_fraud_score(transaction)

    if score >= 50:
        return True, score
    else:
        return False, score