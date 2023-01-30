from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas


def create_a4_paper(file_name: str, operations: list[str]):
    canvas = Canvas(file_name, pagesize=A4)
    canvas.setFont('Helvetica', 40)

    x = 30
    y = 720

    for index1, operation in enumerate(operations):
        if index1 > 0 and index1 % 4 == 0:
            x += 140
            y = 720

        for index2, line in enumerate(operation):
            if index2 == 0:
                x += 10

            canvas.drawString(x, y, line)

            if index2 == 0:
                x -= 10

            if line.startswith('-'):
                y -= 90
            else:
                y -= 50

    canvas.showPage()
    canvas.save()
