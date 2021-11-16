import task_1

class TestClassTask1:
    def test(self):
        day = 31
        month = 4
        odp = (month % 2 == 0 and (1 <= day <= 30)) or (month % 2 == 1 and (1 <= day <= 31))
        assert not odp

    def test_ClockCalendar(self):
        assert task_1.ClockCalendar(2021,11,14,13,46,15)

    def test_calendar(self):
        pass