import mpv

class Player:
    def __init__(self):
        self.player = mpv.MPV()

    def play(self, url: str):
        self.player.play(url)

    def stop(self):
        self.player.stop()
