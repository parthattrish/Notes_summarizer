from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph


def generate_pdf(summary, output_path):

    document = SimpleDocTemplate(output_path)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph("<b>AI Notes Summary</b>", styles["Heading1"])
    )

    story.append(
        Paragraph(summary.replace("\n", "<br/>"), styles["BodyText"])
    )

    document.build(story)
