from dataclasses import dataclass
from random import sample
from generate import create_a4_paper
from flet import Page, Row, IconButton, TextField
import flet


@dataclass()
class CalcMaker():
    page: Page

    def __post_init__(self):
        self.page.title = "Calc Maker"
        self.page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
        self.buttons()

    def buttons(self):
        self.start = TextField(
            label="Minimal",
            hint_text="What's the minimal number: ",
            keyboard_type=flet.KeyboardType.NUMBER
        )
        self.end = TextField(
            label="Maximum",
            hint_text="What's the maximum number: ",
            keyboard_type=flet.KeyboardType.NUMBER
        )

        generate = IconButton(flet.icons.CREATE, on_click=self.operations)

        self.page.add(Row(
            [
                self.start,
                self.end,
                generate
            ]
        ))

        self.page.update()

    def operations(self, event: flet.Event):
        print(event)
        # + Plus (Addition)
        # - Minus (Subtraction)
        # ÷ Obelus (Division)
        # x Times (Multiplication)
        operators = ('+', '-', '÷', 'x')
        operations = []

        numbers = range(int(self.start.value or 2), int(self.end.value or 6))

        for number in range(0, 16):
            choose = sample(numbers, 2)
            operation = []

            operation.append(f'{choose[0]:>4}')
            operation.append(f'{operators[0]:<1} {choose[1]:>2}')
            operation.append('-' * 6)

            operations.append(operation)

            # print(f'{choose[0]:>4}')
            # print(f'{operators[0]:<1} {choose[1]:>2}')
            # print('-' * 4)

        create_a4_paper('operations.pdf', operations)
        # create_a4_paper2('operations.pdf')

        self.page.update()


if __name__ == "__main__":
    flet.app(port=5500, target=CalcMaker, view=None)
    # app(target=CalcMaker)
