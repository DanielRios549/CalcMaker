from dataclasses import dataclass
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas


@dataclass()
class Generate():
    file_name: str
    operations: list[str]

    def __post_init__(self):
        self.x = 30
        self.y = 720

        self.canvas = Canvas(self.file_name, pagesize=A4)
        self.canvas.setFont('Helvetica', 40)

    def create_a4_paper(self):
        for index1, operation in enumerate(self.operations):
            if index1 > 0 and index1 % 4 == 0:
                self.x += 140
                self.y = 720

            for index2, line in enumerate(operation):
                if index2 == 0:
                    self.x += 10

                self.canvas.drawString(self.x, self.y, line)

                if index2 == 0:
                    self.x -= 10

                if line.startswith('-'):
                    self.y -= 90
                else:
                    self.y -= 50

        self.canvas.showPage()
        self.canvas.save()
