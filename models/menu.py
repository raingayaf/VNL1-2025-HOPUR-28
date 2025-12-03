from typing import Dict


class Menu:
    id: int
    main_course: str
    vegan_course: str
    soup: str
    created_at: str

    def __init__(
        self,
        id: int,
        main_course: str,
        vegan_course: str,
        soup: str,
        created_at: str,
    ) -> None:
        self.id = id
        self.main_course = main_course
        self.vegan_course = vegan_course
        self.soup = soup
        self.created_at = created_at

    def to_dict(self) -> Dict[str, str]:
        return {
            "id": str(self.id),
            "main_course": self.main_course,
            "vegan_course": self.vegan_course,
            "soup": self.soup,
            "created_at": self.created_at,
        }

    def __str__(self) -> str:
        # User-facing pretty print
        return (
            f"[{self.id}] "
            f"Aðal: {self.main_course} | "
            f"Vegan: {self.vegan_course} | "
            f"Súpa: {self.soup} | "
            f"Stofnað: {self.created_at}"
        )

    def __repr__(self) -> str:
        # Dev/debug print
        return (
            f"Menu(id={self.id}, main_course={self.main_course!r}, "
            f"vegan_course={self.vegan_course!r}, soup={self.soup!r}, "
            f"created_at={self.created_at!r})"
        )
