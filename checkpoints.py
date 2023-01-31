from dataclasses import dataclass
from main import CalcMaker


@dataclass()
class CheckPoints():
    main: CalcMaker

    def input(self) -> dict[str, float]:
        return {
            'sm': 6
        }

    def checkbox(self) -> dict[str, float]:
        return {
            'md': 2,
            'sm': 6
        }
