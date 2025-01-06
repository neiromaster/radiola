from radiola.utils.check_libmpv import check_libmpv


class Player:
    def __init__(self):
        check_libmpv()
        import mpv

        self.player = mpv.MPV()

    def play(self, url: str):
        self.player.play(url)

    def stop(self):
        self.player.stop()
