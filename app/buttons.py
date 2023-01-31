from dataclasses import dataclass
from main import CalcMaker
import flet


@dataclass()
class Buttons():
    main: CalcMaker

    def start(self):
        return flet.TextField(
            label="Minimal",
            hint_text="What's the minimal number: ",
            keyboard_type=flet.KeyboardType.NUMBER
        )

    def end(self):
        return flet.TextField(
            label="Maximum",
            hint_text="What's the maximum number: ",
            keyboard_type=flet.KeyboardType.NUMBER
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
