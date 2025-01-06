from textual.app import ComposeResult, App
from textual.widgets import Label


class RadiolaApp(App):
    def compose(self) -> ComposeResult:
        yield Label("Hello, World!")


def run():
    app = RadiolaApp()
    app.run()


if __name__ == "__main__":
    run()
