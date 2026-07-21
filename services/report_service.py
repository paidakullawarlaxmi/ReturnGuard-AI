from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def generate_reports(pdf_path, email_path, details):
    email_path.write_text(
        "\n".join(f"{key.replace('_', ' ').title()}: {value}" for key, value in details.items()),
        encoding="utf-8",
    )
    styles = getSampleStyleSheet()
    body = ParagraphStyle("ReportBody", parent=styles["BodyText"], leading=16, textColor=colors.HexColor("#334155"))
    story = [Paragraph("ReturnGuard AI - Investigation Report", styles["Title"]), Spacer(1, 14)]
    story.extend(Paragraph(f"<b>{key.replace('_', ' ').title()}:</b> {value}", body) for key, value in details.items())
    SimpleDocTemplate(str(pdf_path)).build(story)
