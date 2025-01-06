from textual.app import ComposeResult, App
from textual.widgets import Label


class RadiolaApp(App):
    def compose(self) -> ComposeResult:
        yield Label("Hello, World!")
