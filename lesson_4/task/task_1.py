import datetime

class Employee:
    def __init__(self,name,surname,birthdate,reqruitment_date,gross_salary):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate                    #YYYY-MM-DD
        self.reqruitment_date = reqruitment_date      #YYYY-MM-DD
        self.gross_salary = gross_salary

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_net_pay(self):
        return round(0.82*self.gross_salary,2)

    @property
    def work_years(self):
        start_year = int(self.reqruitment_date.split('-')[0])
        now_year = datetime.datetime.now().year
        return now_year - start_year

# def work_years(start_work):
#     start = int(start_work.split('-')[0])
#     print(start)

if __name__ == '__main__':
    emp = Employee('krzysie','kondys','2001-04-04','2019-01-01','4500')
    print(emp.work_years)