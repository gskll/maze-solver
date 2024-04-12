from tkinter import ACTIVE, Frame, font, LEFT, NORMAL
from typing import Callable
from tkmacosx import Button


class Btn(Frame):
    def __init__(
        self,
        frame: Frame,
        text: str,
        command: Callable,
        main_color: str,
        bg_color: str,
    ):
        super().__init__()
        self._main = main_color
        self._bg = bg_color
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

    def toggle_normal(self):
        self._btn.configure(state=NORMAL)  # type:ignore

    def toggle_active(self):
        self._btn.configure(state=ACTIVE)  # type:ignore
