from dataclasses import dataclass
from random import sample
from generate import Generate
import checkpoints as ck
import flet


@dataclass()
class CalcMaker():
    page: flet.Page

    def __post_init__(self):
        self.page.title = "Calc Maker"
        self.page.horizontal_alignment = flet.CrossAxisAlignment.CENTER

        self.buttons()

    def buttons(self):
        checkpoints = ck.CheckPoints(self)

        self.start = flet.TextField(
            label="Minimal",
            hint_text="What's the minimal number: ",
            col=checkpoints.input(),
            keyboard_type=flet.KeyboardType.NUMBER
        )
        self.end = flet.TextField(
            label="Maximum",
            hint_text="What's the maximum number: ",
            col=checkpoints.input(),
            keyboard_type=flet.KeyboardType.NUMBER
        )

        generate = flet.IconButton(flet.icons.CREATE, on_click=self.operations)

        self.inputs = (
            flet.ResponsiveRow(
                [
                    flet.Container(
                        self.start,
                        col=checkpoints.input(),
                        bgcolor=flet.colors.BLUE_GREY_900
                    ),
                    flet.Container(
                        self.end,
                        col=checkpoints.input(),
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
                        col=checkpoints.checkbox()
                    ),
                    flet.Container(
                        content=flet.Checkbox(
                            label='Subtraction',
                            disabled=True
                        ),
                        col=checkpoints.checkbox()
                    ),
                    flet.Container(
                        content=flet.Checkbox(
                            label='Multiplication',
                            disabled=True
                        ),
                        col=checkpoints.checkbox()
                    ),
                    flet.Container(
                        content=flet.Checkbox(
                            label='Division',
                            disabled=True
                        ),
                        col=checkpoints.checkbox()
                    ),
                ],
                alignment=flet.MainAxisAlignment.SPACE_BETWEEN
            ),
            flet.Row([
                flet.Container(
                    generate,
                    col=checkpoints.input(),
                    bgcolor=flet.colors.BLUE,
                    expand=True
                )
            ])
        )

        self.results = [
            flet.ResponsiveRow(
                height=500,
                col=checkpoints.input()
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
