from tkinter import Frame, font, LEFT
from typing import Callable
from tkmacosx import Button


class Btn:
    def __init__(
        self,
        frame: Frame,
        text: str,
        command: Callable,
        main_color: str,
        bg_color: str,
    ):
        helv16 = font.Font(family="Helvetica", size=16, weight=font.BOLD)
        self._btn = Button(
            frame,
            text=text,
            font=helv16,
            command=command,
            bordercolor=main_color,
            foreground=main_color,
            background=bg_color,
            activeforeground=bg_color,
            activebackground=main_color,
            disabledforeground=bg_color,
            disabledbackground=bg_color,
            highlightcolor=bg_color,
            focuscolor="",
            height=50,
        )
        self._btn.pack(side=LEFT, padx=10, pady=10)
