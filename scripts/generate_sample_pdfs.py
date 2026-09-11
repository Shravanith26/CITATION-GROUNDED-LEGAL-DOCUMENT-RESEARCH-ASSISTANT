import os
import glob
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def txt_to_pdf(txt_path, pdf_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        text = f.read()

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=54, leftMargin=54,
        topMargin=54, bottomMargin=54
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontSize=14,
        leading=18,
        spaceAfter=12,
        textColor='#1e3a8a'
    )
    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        spaceAfter=8
    )

    story = []
    lines = text.splitlines()

    for line in lines:
        line_str = line.strip()
        if not line_str:
            story.append(Spacer(1, 6))
            continue
        if line_str.startswith("DOCUMENT TITLE:"):
            story.append(Paragraph(f"<b>{line_str}</b>", title_style))
        elif any(line_str.startswith(k) for k in ("COURT:", "CITATION:", "DATE:", "DOCUMENT TYPE:", "BENCH:")):
            story.append(Paragraph(f"<b>{line_str}</b>", body_style))
        elif line_str.startswith("[") and "]" in line_str:
            story.append(Spacer(1, 4))
            story.append(Paragraph(f"<b>{line_str}</b>", body_style))
        else:
            story.append(Paragraph(line_str, body_style))

    doc.build(story)
    print(f"Generated PDF: {pdf_path}")

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_dir = os.path.join(base_dir, "data", "documents", "raw")
    public_dir = os.path.join(base_dir, "frontend", "public", "documents")
    os.makedirs(public_dir, exist_ok=True)

    txt_files = glob.glob(os.path.join(raw_dir, "*.txt"))
    for txt_file in txt_files:
        base_name = os.path.splitext(os.path.basename(txt_file))[0]
        pdf_raw_path = os.path.join(raw_dir, f"{base_name}.pdf")
        pdf_public_path = os.path.join(public_dir, f"{base_name}.pdf")

        txt_to_pdf(txt_file, pdf_raw_path)
        # Also copy to frontend public directory for in-browser PDF viewing
        import shutil
        shutil.copy2(pdf_raw_path, pdf_public_path)

if __name__ == "__main__":
    main()
