from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Background
        self.set_fill_color(0, 0, 0)  # Black
        self.rect(0, 0, 210, 297, 'F')  # A4 size in mm (210 x 297)

        # Add logo image
        self.image("./shirtificate.png", 10, 70, 190)

        # Set font to Arial Bold
        self.set_font("Arial", "B", 48)
        self.set_text_color(255, 255, 255)  # White
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        self.ln(20)

def main():
    name = input("Name: ")
    shirt(name)

def shirt(s):
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")

    pdf.set_font("Arial", "B", 24)
    pdf.set_text_color(255, 255, 255)  # White

    pdf.cell(0, 213, f"{s} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
