
class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        self.__status = not self.__status
        if not self.__status:
            self.__muted = False


    def mute(self):
        if self.__status:
            self.__muted = not self.__muted


    def channel_up(self):
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self):
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self):
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                if self.__volume == Television.MIN_VOLUME:
                    self.__volume = Television.MIN_VOLUME
                else:
                    self.__volume -= 1

    def __str__(self):
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"




