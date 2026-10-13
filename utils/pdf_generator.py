from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import datetime

def generate_pdf_report(filename, results):
    """Generates an anonymized diagnostic summary report."""
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    
    p.setFont("Helvetica-Bold", 18)
    p.drawString(50, 750, "Scolio-AI Screening Analysis Summary")
    
    p.setFont("Helvetica", 10)
    p.drawString(50, 730, f"Analysis Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    p.drawString(50, 715, f"Source File Identifier: {filename}")
    p.drawString(50, 700, "Model Version: ScolioResNet50-v1.2 (Research Engine)")
    
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, 660, f"Predicted Class: {results.get('predicted_class')}")
    p.drawString(50, 640, f"Confidence Score: {results.get('confidence')*100:.1f}%")
    
    p.setFont("Helvetica-Oblique", 9)
    p.drawString(50, 580, "CAUTION: Research prototype only. Not approved for primary diagnostic use.")
    
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer.getvalue()
