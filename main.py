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
        self.start = self.buttons.start()
        self.end = self.buttons.end()
        self.operations = app.Operations(self)

        self.preLoad()

    def preLoad(self):
        self.inputs = (
            flet.ResponsiveRow(
                [
                    flet.Container(
                        self.start,
                        bgcolor=flet.colors.BLUE_GREY_900,
                        col=app.CheckPoints().input()
                    ),
                    flet.Container(
                        self.end,
                        bgcolor=flet.colors.BLUE_GREY_900,
                        col=app.CheckPoints().input()
                    )
                    # self.start,
                    # self.end
                ],
                alignment=flet.MainAxisAlignment.CENTER,
                # run_spacing={"xs": 10},
            ),
            flet.ResponsiveRow(
                [
                    flet.Container(
                        content=flet.Checkbox(
                            label='Addition',
                            value=True,
                            disabled=True
                        ),
                        col=app.CheckPoints().checkbox()
                    ),
                    flet.Container(
                        content=flet.Checkbox(
                            label='Subtraction',
                            disabled=True
                        ),
                        col=app.CheckPoints().checkbox()
                    ),
                    flet.Container(
                        content=flet.Checkbox(
                            label='Multiplication',
                            disabled=True
                        ),
                        col=app.CheckPoints().checkbox()
                    ),
                    flet.Container(
                        content=flet.Checkbox(
                            label='Division',
                            disabled=True
                        ),
                        col=app.CheckPoints().checkbox()
                    ),
                ],
                alignment=flet.MainAxisAlignment.SPACE_BETWEEN
            ),
            flet.Row([
                flet.Container(
                    self.buttons.generate(),
                    col=app.CheckPoints().input(),
                    bgcolor=flet.colors.BLUE,
                    expand=True
                )
            ])
        )

        self.results = [
            flet.ResponsiveRow(
                [
                    flet.Container(
                        flet.Text(
                            'Type the minimal and maximum number and click in Gererate',
                            text_align=flet.TextAlign.CENTER
                        ),
                        col=app.CheckPoints().preview()
                    )
                ]
            )
        ]

        self.page.add(
            *self.inputs,
            *self.results
        )

        self.page.update()


if __name__ == "__main__":
    flet.app(port=5500, target=CalcMaker, view=None)
    # app(target=CalcMaker)
