from dataclasses import dataclass
from main import CalcMaker
from random import sample
import app
import flet


@dataclass()
class Operations():
    main: CalcMaker

    def make(self, event: flet.Event):
        self.main.message.clean()
        self.main.result.clean()

        # + Plus (Addition)
        # - Minus (Subtraction)
        # ÷ Obelus (Division)
        # x Times (Multiplication)
        operators = ('+', '-', '÷', 'x')
        operations = []

        numbers = range(int(self.main.start.value or 1), int(self.main.end.value or 1) + 1 or 3)

        for number in range(0, 16):
            choose = sample(numbers, 2)
            operation = []

            operation.append(f'{choose[0]:>4}')
            operation.append(f'{operators[0]:<1} {choose[1]:>2}')
            operation.append('-' * 6)

            self.main.result.controls.append(
                flet.Container(
                    flet.Column(
                        [
                            flet.Row(
                                [
                                    flet.Text(
                                        f'{choose[0]}',
                                        size=20
                                    ),
                                ],
                                alignment=flet.MainAxisAlignment.END,
                                height=30
                            ),
                            flet.Row(
                                [
                                    flet.Text(
                                        f'{operators[0]}   {choose[1]}',
                                        size=20,
                                    ),
                                ],
                                alignment=flet.MainAxisAlignment.END,
                                height=30
                            )
                        ]
                    ),
                    margin=flet.margin.only(bottom=50),
                    border=flet.border.only(
                        bottom=flet.border.BorderSide(1, flet.colors.WHITE)
                    ),
                    alignment=flet.alignment.center,
                    col=app.CheckPoints().preview(),
                    expand=False,
                    width=30,
                    height=70
                )
            )

        self.main.page.update()
        generate = app.Generate('operations.pdf', operations)
        generate.create_a4_paper()

        # self.page.add(
        #     flet.Container(
        #         content=generate.canvas.)
        #     )
        # )
