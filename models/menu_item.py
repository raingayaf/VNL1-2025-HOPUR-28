class MenuItem:
    name: str
    type: str

    def __init__(self, name: str, type_: str) -> None:
        self.name = name
        self.type = type_

    def __str__(self) -> str:
        return f"{self.type}: {self.name}"

    def __repr__(self) -> str:
        return f"MenuItem(name={self.name!r}, type={self.type!r})"
