import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from services.database import get_connection


def generate_fraud_chart(database_path, chart_path):
    with get_connection(database_path) as connection:
        rows = connection.execute("SELECT prediction FROM FraudHistory").fetchall()
    counts = {"LOW FRAUD": 0, "HIGH FRAUD": 0}
    for row in rows:
        if "HIGH" in row["prediction"].upper():
            counts["HIGH FRAUD"] += 1
        else:
            counts["LOW FRAUD"] += 1
    figure, axis = plt.subplots(figsize=(6, 4), facecolor="#1e293b")
    axis.set_facecolor("#1e293b")
    bars = axis.bar(counts.keys(), counts.values(), color=["#10b981", "#f43f5e"])
    axis.set_title("Return Risk Distribution", color="white", fontweight="bold")
    axis.tick_params(colors="white")
    for bar in bars:
        axis.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(int(bar.get_height())), ha="center", color="white")
    figure.tight_layout()
    figure.savefig(chart_path, dpi=120, facecolor="#1e293b")
    plt.close(figure)
