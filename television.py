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
        self.__mute_volume = Television.MIN_VOLUME

    def power(self):

        if self.__status:

            self.__status = False

        else:

            self.__status = True

    def mute(self):

        if self.__status:

            if self.__muted:

                self.__muted = False

            else:

                self.__muted = True
                self.__mute_volume = 0

    def channel_up(self):

        if self.__status:

            if self.__channel == 3:

                self.__channel = 0

            else:

                self.__channel += 1

    def channel_down(self):

        if self.__status:

            if self.__channel == 0:

                self.__channel = 3

            else:

                self.__channel -= 1

    def volume_up(self):

        self.__muted = False

        if self.__status:

            if self.__volume == 2:

                self.__volume = 2

            else:

                self.__volume += 1

    def volume_down(self):

        self.__muted = False

        if self.__status:

            if self.__volume == 0:

                self.__volume = 0

            else:

                self.__volume -= 1

    def __str__(self):

        if self.__muted:

            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__mute_volume}'

        else:

            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'