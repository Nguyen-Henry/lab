class Television:
    '''
    A class representing details for a Television object
    '''
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create the initial state of the Television object
        self.__channel - A private variable that stores the TV's Channel with the default being MIN_CHANNEL
        self.__volume - A private variable that stores the TV's volume with the default being MIN_VOLUME
        self.__status - A private variable that stores the TV's status. Initially, it starts as off
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False

    def power(self) -> None:
        """
        Method to change the status of the TV.
        - If the TV object is off, it should be turned on.
        - If the TV object is on, it should be turned off.
        self.__status - A private variable that stores the TV's status.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def channel_up(self) -> None:
        """
        Method to increase the channel of the TV by incrementing the value by one.
        - This only works if the TV is on
        - If this method is called when the self.__channel is on the MAX_CHANNEL, it should change the channel to the MIN_CHANNEL
        self.__channel - A private variable that stores the TV's Channel with the default being MIN_CHANNEL
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Method to decrease the channel of the TV by decrementing the value by one.
        - This only works if the TV is on
        - If this method is called when the self.__channel is on the MIN_CHANNEL, it should change the channel to the MAX_CHANNEL
        self.__channel - A private variable that stores the TV's Channel with the default being MIN_CHANNEL
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method to increase the volume of the TV by incrementing the value by one.
        - This only works if the TV is on
        - If this method is called when the self.__channel is on the MAX_VOLUME, it should not be adjusted
        self.__volume - A private variable that stores the TV's volume with the default being MIN_VOLUME
        """
        if self.__status:
            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to increase the volume of the TV by decrementing the value by one.
        - This only works if the TV is on
        - If this method is called when the self.__channel is on the MIN_VOLUME, it should not be adjusted
        self.__volume - A private variable that stores the TV's volume with the default being MIN_VOLUME
        """
        if self.__status:
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        String method to return the TV's status in a format
        :return: TV's status, channel, and volume.
        """
        return f"TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
