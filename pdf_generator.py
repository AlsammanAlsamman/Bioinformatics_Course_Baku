from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class PdfGenerator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.canvas = canvas.Canvas(file_path, pagesize=letter)

    def add_header(self):
        # Define the logo path relative to the project root
        logo_path = "assets/icarda_logo.png"
        page_width, page_height = letter  # or self.canvas._pagesize if set differently
        # Draw the logo in the top-left corner; adjust x, y, width, height as necessary
        self.canvas.drawImage(logo_path, 10, page_height - 50, width=100, height=40)
        # Optionally, add header text next to the logo
        self.canvas.setFont("Helvetica-Bold", 12)
        self.canvas.drawString(120, page_height - 30, "ICARDA Bioinformatics Course")
    
    def generate_page(self, content_callback):
        self.add_header()  # call the header method for each new page
        content_callback(self.canvas)
        self.canvas.showPage()

    def save(self):
        self.canvas.save()