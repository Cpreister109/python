class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:

        '''
        This function declares the initial variables of the function
        '''

        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__mute_volume = Television.MIN_VOLUME

    def power(self) -> None:

        '''
        This function sets the boolean value to True or False
        for the status variable, Turning the TV on or off.
        '''

        if self.__status:

            self.__status = False

        else:

            self.__status = True

    def mute(self) -> None:

        '''
        This function sets the mute volume to 0, and sets
        the boolean value to True or False for the muted variable.
        '''

        if self.__status:

            if self.__muted:

                self.__muted = False

            else:

                self.__muted = True
                self.__mute_volume = 0

    def channel_up(self) -> None:

        '''
        This function will increase the channel by one,
        or it will cycle back to the minimum channel if the
        maximum channel has already been reached.
        '''

        if self.__status:

            if self.__channel == 3:

                self.__channel = 0

            else:

                self.__channel += 1

    def channel_down(self) -> None:

        '''
        This function will decrease the channel by one,
        or it will cycle back to the maximum channel if the
        minimum channel has already been reached.
        '''

        if self.__status:

            if self.__channel == 0:

                self.__channel = 3

            else:

                self.__channel -= 1

    def volume_up(self) -> None:

        '''
        This function increases the volume by one, unmutes the TV,
        or won't do anything if the maximum volume has been reached.
        '''

        self.__muted = False

        if self.__status:

            if self.__volume == 2:

                self.__volume = 2

            else:

                self.__volume += 1

    def volume_down(self) -> None:

        '''
        This function decreases the volume by one, unmutes the TV,
        or won't do anything if the minimum volume has been reached.
        '''

        self.__muted = False

        if self.__status:

            if self.__volume == 0:

                self.__volume = 0

            else:

                self.__volume -= 1

    def __str__(self) -> str:

        '''
        This function formats the tv details so the user can read them.

        :return: These are the TV details
        '''

        if self.__muted:

            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__mute_volume}'

        else:

            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'