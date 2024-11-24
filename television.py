class Television():
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        """
        Initializes the default values for power, mute, volume, and channel.
        Returns: None
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Turns the TV on or off
        :return: None
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mutes or unmutes the TV. Keeps current volume number.
        :return: None
        """
        if self.__status:
            if not self.__muted:
                self.__muted = True
                self.__prev_volume: int = self.__volume
                self.__volume = Television.MIN_VOLUME
            else:
                self.__muted = False
                self.__volume = self.__prev_volume

    def channel_up(self) -> None:
        """
        Increases the channel by one.
        :return: None
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decreases the channel by one.
        :return: None
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increases the volume by one. Turns off mute.
        :return: None
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Deceases the volume by one. Turns off mute.
        :return: None
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        A string that shows the current power, channel, and volume number.
        :return: Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}
        """
        return f' Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'