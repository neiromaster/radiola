from textual.app import ComposeResult, App
from textual.widgets import Label, Header, Footer

from radiola.services.player import Player


class RadiolaApp(App):
    def __init__(self):
        super().__init__()
        self.player = Player()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Hello, World!")
        yield Footer()

    def on_mount(self):
        self.player.play(
            "https://radio.kamchatkalive.ru:8103/rock"
        )
