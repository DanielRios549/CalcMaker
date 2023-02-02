from dataclasses import dataclass
from main import CalcMaker
from random import sample
import app
import flet


@dataclass()
class Operations():
    main: CalcMaker

    def make(self, event: flet.Event):
        self.main.result.clean()

        options = [
            int(self.main.buttons.start.value or 1),
            int(self.main.buttons.end.value or 8)
        ]

        if options[0] == options[1]:
            self.main.message.value = 'You need to choose different numbers.'
            self.main.page.update()

        else:
            self.main.message.value = ''

            if options[0] > options[1]:
                options.sort()

            numbers = range(options[0], options[1] + 1)

            # + Plus (Addition)
            # - Minus (Subtraction)
            # ÷ Obelus (Division)
            # x Times (Multiplication)
            signals = ('+', '-', 'x', '÷')
            operators: list[str] = []
            operations: list[list[str]] = []

            for index, selection in enumerate(self.main.buttons.operands):
                if selection.value is True:
                    operators.append(signals[index])

            for index in range(0, 16):
                operands = sample(numbers, 2)
                operator = sample(operators, 1)

                if '-' in operator or '÷' in operator:
                    operands.sort()
                    operands.reverse()

                operations.append([])
                operations[index].append(f'{operands[0]:>4}')
                operations[index].append(f'{operator[0]:<1} {operands[1]:>2}')
                operations[index].append('-' * 6)

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
