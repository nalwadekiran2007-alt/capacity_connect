from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth
from datetime import date
import uuid


def create_certificate(file_name, course_name):

    pdf = canvas.Canvas(file_name, pagesize=A4)

    width, height = A4

    # =========================
    # COLORS
    # =========================
    navy = colors.HexColor("#173B67")
    gold = colors.HexColor("#C9A227")
    light_gold = colors.HexColor("#F5E7B2")
    dark_gray = colors.HexColor("#333333")

    # =========================
    # BACKGROUND
    # =========================
    pdf.setFillColor(colors.white)
    pdf.rect(0, 0, width, height, fill=1, stroke=0)

    # =========================
    # OUTER BORDER
    # =========================
    pdf.setStrokeColor(navy)
    pdf.setLineWidth(5)
    pdf.rect(28, 28, width - 56, height - 56)

    # =========================
    # INNER BORDER
    # =========================
    pdf.setStrokeColor(gold)
    pdf.setLineWidth(2)
    pdf.rect(42, 42, width - 84, height - 84)

    # =========================
    # TOP BRANDING
    # =========================
    pdf.setFillColor(navy)
    pdf.setFont("Helvetica-Bold", 24)

    pdf.drawCentredString(
        width / 2,
        height - 100,
        "CAPACITY CONNECT"
    )

    pdf.setFillColor(gold)
    pdf.setFont("Helvetica-Bold", 11)

    pdf.drawCentredString(
        width / 2,
        height - 122,
        "DIGITAL LEARNING PORTAL"
    )

    # =========================
    # DECORATIVE LINE
    # =========================
    pdf.setStrokeColor(gold)
    pdf.setLineWidth(2)

    pdf.line(
        150,
        height - 145,
        width - 150,
        height - 145
    )

    # =========================
    # CERTIFICATE TITLE
    # =========================
    pdf.setFillColor(navy)
    pdf.setFont("Helvetica-Bold", 30)

    pdf.drawCentredString(
        width / 2,
        height - 200,
        "CERTIFICATE"
    )

    pdf.setFont("Helvetica-Bold", 22)

    pdf.drawCentredString(
        width / 2,
        height - 232,
        "OF COMPLETION"
    )

    # =========================
    # PRESENTED TEXT
    # =========================
    pdf.setFillColor(dark_gray)
    pdf.setFont("Helvetica", 14)

    pdf.drawCentredString(
        width / 2,
        height - 275,
        "This certificate is proudly presented to"
    )

    # =========================
    # STUDENT NAME
    # =========================
    pdf.setFillColor(navy)
    pdf.setFont("Helvetica-Bold", 32)

    pdf.drawCentredString(
        width / 2,
        height - 325,
        "Kiran"
    )

    # Name underline
    name_width = stringWidth(
        "Kiran",
        "Helvetica-Bold",
        32
    )

    pdf.setStrokeColor(gold)
    pdf.setLineWidth(2)

    pdf.line(
        (width - name_width) / 2,
        height - 337,
        (width + name_width) / 2,
        height - 337
    )

    # =========================
    # COMPLETION TEXT
    # =========================
    pdf.setFillColor(dark_gray)
    pdf.setFont("Helvetica", 14)

    pdf.drawCentredString(
        width / 2,
        height - 375,
        "for successfully completing the course"
    )

    # =========================
    # COURSE NAME
    # =========================
    pdf.setFillColor(navy)
    pdf.setFont("Helvetica-Bold", 23)

    pdf.drawCentredString(
        width / 2,
        height - 420,
        course_name
    )

    # =========================
    # DESCRIPTION
    # =========================
    pdf.setFillColor(dark_gray)
    pdf.setFont("Helvetica", 12)

    pdf.drawCentredString(
        width / 2,
        height - 460,
        "This certificate recognizes the successful completion"
    )

    pdf.drawCentredString(
        width / 2,
        height - 478,
        "of the required learning content and assessment."
    )

    # =========================
    # GOLD SEAL
    # =========================
    seal_x = width / 2
    seal_y = 240

    pdf.setStrokeColor(gold)
    pdf.setLineWidth(3)

    pdf.circle(
        seal_x,
        seal_y,
        38,
        stroke=1,
        fill=0
    )

    pdf.setLineWidth(1)

    pdf.circle(
        seal_x,
        seal_y,
        30,
        stroke=1,
        fill=0
    )

    pdf.setFillColor(gold)
    pdf.setFont("Helvetica-Bold", 10)

    pdf.drawCentredString(
        seal_x,
        seal_y + 5,
        "CERTIFIED"
    )

    pdf.setFont("Helvetica-Bold", 8)

    pdf.drawCentredString(
        seal_x,
        seal_y - 9,
        "2026"
    )

    # =========================
    # DATE
    # =========================
    today = date.today().strftime("%d %B %Y")

    pdf.setFillColor(dark_gray)
    pdf.setFont("Helvetica", 11)

    pdf.drawString(
        90,
        145,
        "Issue Date"
    )

    pdf.setFont("Helvetica-Bold", 11)

    pdf.drawString(
        90,
        128,
        today
    )

    # =========================
    # CERTIFICATE ID
    # =========================
    certificate_id = "CC-" + str(uuid.uuid4())[:8].upper()

    pdf.setFont("Helvetica", 11)

    pdf.drawRightString(
        width - 90,
        145,
        "Certificate ID"
    )

    pdf.setFont("Helvetica-Bold", 11)

    pdf.drawRightString(
        width - 90,
        128,
        certificate_id
    )

    # =========================
    # SIGNATURE
    # =========================
    pdf.setStrokeColor(navy)
    pdf.setLineWidth(1)

    pdf.line(
        width / 2 - 80,
        95,
        width / 2 + 80,
        95
    )

    pdf.setFillColor(navy)
    pdf.setFont("Helvetica-Bold", 11)

    pdf.drawCentredString(
        width / 2,
        78,
        "Course Instructor"
    )

    # =========================
    # FOOTER
    # =========================
    pdf.setFillColor(navy)
    pdf.setFont("Helvetica-Bold", 9)

    pdf.drawCentredString(
        width / 2,
        55,
        "CAPACITY CONNECT • Learn. Build. Grow."
    )

    # =========================
    # SAVE PDF
    # =========================
    pdf.save()

    print(file_name + " created successfully!")


# =====================================
# CREATE ALL 4 CERTIFICATES
# =====================================

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

print("")
print("====================================")
print("ALL 4 CERTIFICATES CREATED!")
print("====================================")