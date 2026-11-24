from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.platypus.flowables import HRFlowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
import sys

FONT_DIR = "/usr/share/fonts/truetype/google-fonts/ofl/firasans/"
pdfmetrics.registerFont(TTFont("Fira", FONT_DIR + "FiraSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Fira-Italic", FONT_DIR + "FiraSans-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Fira-Medium", FONT_DIR + "FiraSans-Medium.ttf"))
pdfmetrics.registerFont(TTFont("Fira-SemiBold", FONT_DIR + "FiraSans-SemiBold.ttf"))
addMapping("Fira", 0, 0, "Fira")
addMapping("Fira", 0, 1, "Fira-Italic")
addMapping("Fira", 1, 0, "Fira-SemiBold")
addMapping("Fira", 1, 1, "Fira-SemiBold")

INK = HexColor("#16181D")
MUTED = HexColor("#4B5060")
ACCENT = HexColor("#0E7A55")
RULE = HexColor("#C9CDD4")

BODY = 10.5
name_s = ParagraphStyle("name", fontName="Fira-SemiBold", fontSize=23, leading=27, textColor=INK)
role_s = ParagraphStyle("role", fontName="Fira", fontSize=11.5, leading=15, textColor=INK, spaceBefore=2)
contact_s = ParagraphStyle("contact", fontName="Fira", fontSize=9.5, leading=13, textColor=MUTED, spaceBefore=3)
h_s = ParagraphStyle("h", fontName="Fira-SemiBold", fontSize=10.5, leading=13, textColor=ACCENT, spaceBefore=9, spaceAfter=1)
body_s = ParagraphStyle("body", fontName="Fira", fontSize=BODY, leading=BODY * 1.38, textColor=INK)
muted_s = ParagraphStyle("muted", parent=body_s, textColor=MUTED)
entry_s = ParagraphStyle("entry", parent=body_s, fontName="Fira-SemiBold")
date_s = ParagraphStyle("date", parent=body_s, textColor=MUTED, alignment=TA_RIGHT)
bullet_s = ParagraphStyle("bullet", parent=body_s, leftIndent=12, bulletIndent=2, spaceBefore=1.5)

W = letter[0] - 1.3 * inch


def section(title):
    return [Paragraph(title.upper(), h_s), HRFlowable(width="100%", thickness=0.6, color=RULE, spaceBefore=0, spaceAfter=5)]


def entry(left, right, sub=None):
    rows = [[Paragraph(left, entry_s), Paragraph(right, date_s)]]
    t = Table(rows, colWidths=[(W - 12) * 0.74, (W - 12) * 0.26])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    out = [t]
    if sub:
        out.append(Paragraph(sub, muted_s))
    return out


def bullets(items):
    return [Paragraph(i, bullet_s, bulletText="•") for i in items]


story = []
story += [Paragraph("Mahdi Hasan Bhuiyan", name_s),
          Paragraph('PhD Student in Computer Science, Washington State University &nbsp;·&nbsp; <link href="https://mahdi0082.github.io"><font color="#0E7A55">mahdi0082.github.io</font></link>', role_s),
          Paragraph('Pullman, WA &nbsp;·&nbsp; <link href="mailto:mahdihasan0072@outlook.com">mahdihasan0072@outlook.com</link>'
                    ' &nbsp;·&nbsp; <link href="mailto:mahdihasan.bhuiyan@wsu.edu">mahdihasan.bhuiyan@wsu.edu</link>'
                    ' &nbsp;·&nbsp; <link href="https://www.linkedin.com/in/mahdi-hasan-bhuiyan-8470aa251/"><u>LinkedIn</u></link>'
                    ' &nbsp;·&nbsp; <link href="https://github.com/Mahdi0082?tab=repositories"><u>GitHub</u></link>'
                    ' &nbsp;·&nbsp; <link href="https://scholar.google.com/citations?user=PoWDRyIAAAAJ&amp;hl=en"><u>Scholar</u></link>', contact_s),
          Spacer(1, 6),
          Paragraph("ML researcher in federated and decentralized bilevel optimization, with applied projects in medical imaging and "
                    "recommendation. Proficient in Python; seeking a Summer 2027 internship.", body_s)]

story += section("Education")
story += [KeepTogether(entry("Washington State University, Pullman, WA", "2025 – 2030 (expected)",
                             "Ph.D. in Computer Science &nbsp;·&nbsp; CGPA 3.87 / 4.00 &nbsp;·&nbsp; Advisor: Dr. Xuanyu Cao")),
          Paragraph("Coursework: Computer Vision, Reinforcement Learning, Computational Optimization, Data Science", muted_s),
          Spacer(1, 5),
          KeepTogether(entry("BRAC University, Dhaka, Bangladesh", "2020 – 2024",
                             "B.Sc. in Computer Science &nbsp;·&nbsp; CGPA 3.61 / 4.00"))]

story += section("Experience")
story += entry("Graduate Research Assistant, Washington State University", "2025 – Present")
story += bullets([
    "Designed <b>FedBiC</b>, a federated bilevel method where each client’s lower-level problem has its own constraints; "
    "proved convergence under partial client participation (under review, ICLR 2027).",
    "Reformulated the nested problem as a single-level penalized one solved with gradient steps; the server receives only "
    "upper-level gradients, so client data stays local.",
    "Implemented experiments in Python, including fairness-constrained learning, against FedNest, SimFBO, FedBiOAcc "
    "and centralized BiC-GAFFA.",
    "Developing <b>DS-BiC</b>, a decentralized stochastic extension for peer-to-peer networks.",
])
story += [Spacer(1, 3)]
story += entry("Teaching Assistant, CptS 423 and CptS 484, WSU", "Fall 2026")
story += bullets([
    "Grade reports and give written feedback in Software Design Project II and Software Requirements.",
])

story += section("Publications")
story += bullets([
    "<b>FedBiC: Federated Bilevel Constrained Optimization.</b> Under review at ICLR 2027.",
    "<b>An Interpretable Diagnosis of Retinal Diseases Using Vision Transformer and Grad-CAM.</b> IEEE ECCE 2025, second author.",
])

story += section("Projects")
projects = [
    ("Diabetic Retinopathy Screening with Confidence-Based Referral", "Fall 2026",
     "Team project, CPT S 541 Computer Vision. Trained on APTOS 2019; low-confidence cases are referred to a specialist; "
     "evaluated on Messidor-2 without retraining."),
    ("H&amp;M Personalized Fashion Recommendations", "Fall 2026",
     "Team project, data science course. Predicts each customer’s next purchases from H&amp;M’s Kaggle data."),
    ("Engine Valve Design with the Nelder–Mead Simplex Method", "",
     "Course project, computational optimization. Implemented Nelder–Mead from scratch for valve design."),
    ("Stock Forecasting with News Sentiment", "",
     "Combined XGBoost and an LSTM with sentiment features from news text to forecast price movement."),
]
for title, date, desc in projects:
    block = entry(title, date) + bullets([desc]) + [Spacer(1, 3)]
    story.append(KeepTogether(block))

story += section("Skills &amp; Service")
story += [Paragraph("<b>Programming:</b> Python (proficient), LaTeX &nbsp;&nbsp;·&nbsp;&nbsp; "
                    "<b>Machine learning:</b> federated learning, bilevel and stochastic optimization, CNNs, Grad-CAM, "
                    "XGBoost, LSTMs, recommender systems", body_s),
          Paragraph("<b>Service:</b> Reviewer, ICLR 2027", body_s)]

out = sys.argv[1]
doc = SimpleDocTemplate(out, pagesize=letter, leftMargin=0.65 * inch, rightMargin=0.65 * inch,
                        topMargin=0.5 * inch, bottomMargin=0.5 * inch,
                        title="Mahdi Hasan Bhuiyan — CV", author="Mahdi Hasan Bhuiyan",
                        subject="Curriculum vitae")
doc.build(story)
