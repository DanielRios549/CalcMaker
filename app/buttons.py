from dataclasses import dataclass
from main import CalcMaker
import flet


@dataclass()
class Buttons():
    main: CalcMaker

    def __post_init__(self):
        self.start = self.getStart()
        self.end = self.getEnd()
        self.operands = self.getOperands()

    def getStart(self):
        return flet.TextField(
            label="Minimal",
            hint_text="The minimal number (default: 1):",
            keyboard_type=flet.KeyboardType.NUMBER
        )

    def getEnd(self):
        return flet.TextField(
            label="Maximum",
            hint_text="The maximum number (default: 9):",
            keyboard_type=flet.KeyboardType.NUMBER
        )

    def getOperands(self):
        return (
            flet.Checkbox(
                label='Addition',
                value=True
            ),
            flet.Checkbox(
                label='Subtraction',
                disabled=False
            ),
            flet.Checkbox(
                label='Multiplication',
                disabled=False
            ),
            flet.Checkbox(
                label='Division',
                disabled=True
            )
        )

    def generate(self):
        return flet.ElevatedButton(
            text='Generate',
            icon=flet.icons.CREATE,
            on_click=self.main.operations.make,
            bgcolor=flet.colors.BLUE,
            icon_color=flet.colors.WHITE,
            color=flet.colors.WHITE
        )
