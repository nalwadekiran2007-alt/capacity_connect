from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


def create_certificate(file_name, course_name):

    pdf = canvas.Canvas(file_name, pagesize=A4)

    width, height = A4

    # Border
    pdf.setLineWidth(3)
    pdf.rect(40, 40, width - 80, height - 80)

    # Title
    pdf.setFont("Helvetica-Bold", 28)
    pdf.drawCentredString(
        width / 2,
        height - 150,
        "CERTIFICATE OF COMPLETION"
    )

    # Subtitle
    pdf.setFont("Helvetica", 16)
    pdf.drawCentredString(
        width / 2,
        height - 200,
        "This certificate is proudly presented to"
    )

    # Student Name
    pdf.setFont("Helvetica-Bold", 25)
    pdf.drawCentredString(
        width / 2,
        height - 250,
        "Kiran"
    )

    # Course Text
    pdf.setFont("Helvetica", 15)
    pdf.drawCentredString(
        width / 2,
        height - 300,
        "for successfully completing"
    )

    # Course Name
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(
        width / 2,
        height - 340,
        course_name
    )

    # Platform
    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(
        width / 2,
        height - 400,
        "CAPACITY CONNECT"
    )

    # Date
    pdf.setFont("Helvetica", 12)
    pdf.drawCentredString(
        width / 2,
        height - 450,
        "Date: 26 August 2026"
    )

    # Signature
    pdf.line(100, 120, 250, 120)

    pdf.setFont("Helvetica", 12)
    pdf.drawCentredString(
        175,
        100,
        "Course Instructor"
    )

    pdf.save()

    print(file_name + " created successfully!")


# ==============================
# CREATE ALL CERTIFICATES
# ==============================

create_certificate(
    "Kiran_Python_Certificate.pdf",
    "Python Programming"
)

create_certificate(
    "Kiran_Java_Certificate.pdf",
    "Java Programming"
)

create_certificate(
    "Kiran_Web_Certificate.pdf",
    "Web Development"
)

create_certificate(
    "Kiran_Data_Certificate.pdf",
    "Data Analytics"
)

print("All 4 certificates created successfully!")