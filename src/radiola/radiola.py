from textual.app import ComposeResult, App
from textual.widgets import Label, Header, Footer


class RadiolaApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Hello, World!")
        yield Footer()


def run():
    app = RadiolaApp()
    app.run()


if __name__ == "__main__":
    run()
