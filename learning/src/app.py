from data import returns
from fraud_detector import is_fraud
from utils import print_report


print("🔥 ReturnGuard AI Started\n")

for transaction in returns:
    fraud, score = is_fraud(transaction)
    print_report(transaction["user_id"], fraud, score)