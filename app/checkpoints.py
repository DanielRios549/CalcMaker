from dataclasses import dataclass


@dataclass()
class CheckPoints():
    def input(self) -> dict[str, float]:
        return {
            'sm': 6
        }

    def checkbox(self) -> dict[str, float]:
        return {
            'md': 2,
            'sm': 6
        }

    def preview(self) -> dict[str, float]:
        return {
            'md': 2,
            'sm': 3,
            'xs': 6
        }
