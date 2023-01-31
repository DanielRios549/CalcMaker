from dataclasses import dataclass
from random import sample
from generate import Generate
import app
import flet


@dataclass()
class CalcMaker():
    page: flet.Page

    def __post_init__(self):
        self.page.title = "Calc Maker"
        self.page.horizontal_alignment = flet.CrossAxisAlignment.CENTER

        self.buttons()

    def buttons(self):
        buttons = app.Buttons(self)

        self.inputs = (
            flet.ResponsiveRow(
                [
                    flet.Container(
                        buttons.start(),
                        bgcolor=flet.colors.BLUE_GREY_900
                    ),
                    flet.Container(
                        buttons.end(),
                        bgcolor=flet.colors.BLUE_GREY_900
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
                    buttons.generate(),
                    col=app.CheckPoints().input(),
                    bgcolor=flet.colors.BLUE,
                    expand=True
                )
            ])
        )

        self.results = [
            flet.ResponsiveRow(
                height=500,
                col=app.CheckPoints().input()
            )
        ]

        self.page.add(
            *self.inputs,
            *self.results
        )

    def operations(self, event: flet.Event):
        self.results[0].clean()

        # + Plus (Addition)
        # - Minus (Subtraction)
        # ÷ Obelus (Division)
        # x Times (Multiplication)
        operators = ('+', '-', '÷', 'x')
        operations = []

        numbers = range(int(self.start.value or 1), int(self.end.value or 1) + 1 or 3)

        for number in range(0, 16):
            choose = sample(numbers, 2)
            operation = []

            operation.append(f'{choose[0]:>4}')
            operation.append(f'{operators[0]:<1} {choose[1]:>2}')
            operation.append('-' * 6)

            self.results[0].controls.append(
                flet.Row(
                    controls=[
                        flet.Column(
                            alignment=flet.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                flet.Text(f'{choose[0]:>5}'),
                                flet.Text(f'{operators[0]:<1} {choose[1]:>2}'),
                                flet.Text('-' * 6)
                            ]
                        )
                    ]
                )
            )

        self.page.update()
        # generate = Generate('operations.pdf', operations)
        # generate.create_a4_paper()

        # self.page.add(
        #     flet.Container(
        #         content=generate.canvas.)
        #     )
        # )

        self.page.update()


if __name__ == "__main__":
    flet.app(port=5500, target=CalcMaker, view=None)
    # app(target=CalcMaker)
