from dataclasses import dataclass
from main import CalcMaker
from random import sample
from app.generate import Generate
import flet


@dataclass()
class Operations():
    main: CalcMaker

    def make(self, event: flet.Event):
        self.main.results[0].clean()

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

            self.main.results[0].controls.append(
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

        self.main.page.update()
        generate = Generate('operations.pdf', operations)
        generate.create_a4_paper()

        # self.page.add(
        #     flet.Container(
        #         content=generate.canvas.)
        #     )
        # )
