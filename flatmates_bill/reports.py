import webbrowser
from pathlib import Path
from filestack import Client

from fpdf import FPDF

base_dir = Path(__file__).resolve().parent


class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates
    such as their names, their due amount and the period of the bill.
    """

    def __init__(self, filename) -> None:
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation="P", unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image(str(base_dir.joinpath("files/house.png")), w=30, h=30)

        # Add text
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatemates Bill', border=0, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=25, txt="Period:", border=0)
        pdf.cell(w=150, h=25, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount of second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        # Change directory to files, generate and open the PDF
        pdf.output(str(base_dir.joinpath(f"files/{self.filename}")))

        # webbrowser.open('file://'+ os.path.realpath(f"flatmates_bill/{self.filename}"))
        webbrowser.open('file://' + str(base_dir.joinpath(f"files/{self.filename}")))


class FileSharar:

    def __init__(self, filepath, api_key="") -> None:
        self.filepath = filepath
        self.api_key = api_key
        
    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url