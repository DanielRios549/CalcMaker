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
        signals = ('+', '-', 'x', '÷')
        operators = []
        operations = []

        for index, selection in enumerate(self.main.buttons.operands):
            if selection.value is True:
                operators.append(signals[index])

        numbers = range(int(self.main.buttons.start.value or 1), int(self.main.buttons.end.value or 1) + 1)

        for number in range(0, 16):
            operands = sample(numbers, 2)
            operator = sample(operators, 1)

            if '-' in operator or '÷' in operator:
                operands.sort()
                operands.reverse()

            operations.append(f'{operands[0]:>4}')
            operations.append(f'{operator[0]:<1} {operands[1]:>2}')
            operations.append('-' * 6)

            self.main.result.controls.append(
                flet.Container(
                    flet.Column(
                        [
                            flet.Row(
                                [
                                    flet.Text(
                                        f'{operands[0]}',
                                        size=20
                                    ),
                                ],
                                alignment=flet.MainAxisAlignment.END,
                                height=30
                            ),
                            flet.Row(
                                [
                                    flet.Text(
                                        f'{operator[0]}   {operands[1]}',
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
