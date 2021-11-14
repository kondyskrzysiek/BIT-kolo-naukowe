class Clock:
    def __init__(self, hour: int, minute: int, seconds: int):
        self._check_value(hour, minute, seconds)
        self.hours = hour
        self.minute = minute
        self.seconds = seconds

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.seconds:02d}'

    def advance(self, h_delta, min_delta, s_delta):
        pass

    @staticmethod
    def _check_value(hour: int, minute: int, seconds: int):
        if not isinstance(hour, int):
            raise TypeError('Wrong hour type, should be int!')
        if not isinstance(minute, int):
            raise TypeError('Wrong minute type, should be int!')
        if not isinstance(seconds, int):
            raise TypeError('Wrong seconds type, should be int!')

        if not (0 <= hour <= 24):
            raise ValueError("Hour has to be in range [0, 24)")
        if not (0 <= minute <= 60):
            raise ValueError("Minute has to be in range [0, 60)")
        if not (0 <= seconds <= 60):
            raise ValueError("seconds has to be in range [0, 60)")


class Calendar:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    def advance(self, y_delta, m_delta, d_delta):
        pass

    def __str__(self):
        return f'{self.year:04d}:{self.month:02d}:{self.day:02d}'

    @staticmethod
    def _check_value(year: int, month: int, day: int):
        if not isinstance(year, int):
            raise TypeError('Wront year type should be int')
        if not isinstance(month, int):
            raise TypeError('Wront month type should be int')
        if not isinstance(day, int):
            raise TypeError('Wront day type should be int')

        if not (1 <= month <= 12):
            raise ValueError('Month has to be in range (1,12)')
        if not (month % 2 == 0 and (1 <= day <= 30)) or (month % 2 == 1 and (1 <= day <= 31)):
            raise ValueError('Even month , day has to be in range (1,30) .Odd month , day has to be in range (1,31)')


class ClockCalendar(Clock):
    def __init__(self, year, month, day, hour, minute, seconds):
        Calendar.__init__(self, year, month, day)
        Clock.__init__(self, hour, minute, seconds)

    def __str__(self):
        datestr = Calendar.__str__(self)
        timestr = Clock.__str__(self)
        return f'{datestr} {timestr}'


if __name__ == '__main__':
    clockcalendar = ClockCalendar(2021,11,14,13,46,15)

    print(clockcalendar)
