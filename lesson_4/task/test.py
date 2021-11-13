import task_1

class TestClassTask1:
    def test_year_work(self):
        year_start = '2000-01-02'
        start_work = int(year_start.split('-')[0])
        assert  start_work == 2000