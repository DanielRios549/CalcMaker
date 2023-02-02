from dataclasses import dataclass
import app
import flet


@dataclass()
class CalcMaker():
    page: flet.Page

    def __post_init__(self):
        self.page.title = "Calc Maker"
        self.page.horizontal_alignment = flet.CrossAxisAlignment.CENTER

        self.buttons = app.Buttons(self)
        self.operations = app.Operations(self)

        self.preLoad()

    def preLoad(self):
        self.inputs = (
            flet.ResponsiveRow(
                [
                    flet.Container(
                        content=self.buttons.start,
                        bgcolor=flet.colors.BLUE_GREY_900,
                        col=app.CheckPoints().input()
                    ),
                    flet.Container(
                        content=self.buttons.end,
                        bgcolor=flet.colors.BLUE_GREY_900,
                        col=app.CheckPoints().input()
                    )
                ],
                alignment=flet.MainAxisAlignment.CENTER,
            ),
            flet.ResponsiveRow(
                [
                    flet.Container(
                        content=self.buttons.operands[0],
                        col=app.CheckPoints().checkbox()
                    ),
                    flet.Container(
                        content=self.buttons.operands[1],
                        col=app.CheckPoints().checkbox()
                    ),
                    flet.Container(
                        content=self.buttons.operands[2],
                        col=app.CheckPoints().checkbox()
                    ),
                    flet.Container(
                        content=self.buttons.operands[3],
                        col=app.CheckPoints().checkbox()
                    ),
                ],
                alignment=flet.MainAxisAlignment.SPACE_BETWEEN
            ),
            flet.Row([
                flet.Container(
                    content=self.buttons.generate(),
                    col=app.CheckPoints().input(),
                    bgcolor=flet.colors.BLUE,
                    expand=True
                )
            ])
        )

        self.message = flet.Text(
            'Type the minimal and maximum number and click in Gererate',
            text_align=flet.TextAlign.CENTER,
            color=flet.colors.WHITE70,
        )

        self.result = flet.ResponsiveRow(spacing=80)

        self.page.add(
            *self.inputs,
            flet.ResponsiveRow(
                [
                    flet.Container(
                        content=self.message
                    )
                ]
            ),
            flet.ListView([self.result], expand=1, padding=20)
        )

        self.page.update()


if __name__ == "__main__":
    flet.app(port=5500, target=CalcMaker, view=None)
    # app(target=CalcMaker)
