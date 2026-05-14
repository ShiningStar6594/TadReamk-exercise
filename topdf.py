from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, PageBreak
from reportlab.lib.styles import getSampleStyleSheet



def convertPDF(df1, df2, time):
    doc = SimpleDocTemplate("stock_info.pdf", pagesize=letter)
    styles = getSampleStyleSheet() #use sample style sheet
    content = [] #set up empty list for storing contents

    content.append(Paragraph("Top 10 Stocks by Market Capitalization data", styles["Title"]))
    content.append(Spacer(1, 12))
    content.append(Paragraph("Produced by Yeung Cheuk Lam Lennox", styles["Heading2"]))
    content.append(Spacer(1, 20))
    content.append(Paragraph(f"Generated: {time}", styles["Normal"]))
    content.append(Spacer(1, 20))


    columns1 = [list(df1.columns)]
    rows1 = df1.values.tolist()
    content.append(Table(columns1 + rows1))


    #Second page for more information
    content.append(PageBreak())

    columns2 = [list(df2.columns)]
    rows2 = df2.values.tolist()
    content.append(Table(columns2 + rows2))

    doc.build(content)