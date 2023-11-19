
class Television:
    """
    Class representing a Television with power, mute, channel, and volume control.
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Method to initialize a Television instance with default settings.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to toggle the power status of the television.
        """
        self.__status = not self.__status
        if not self.__status:
            self.__muted = False


    def mute(self) -> None:
        """
        Method to toggle the mute status of the television.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Method to increase the channel by 1.
        """
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """
        Method to decrease the channel by 1.
        """
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        """
        Method to increase the volume by 1.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease the volume by 1.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                if self.__volume == Television.MIN_VOLUME:
                    self.__volume = Television.MIN_VOLUME
                else:
                    self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to print the Power status, Channel number, and Volume number (television status).
        :Return: television status.
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"





