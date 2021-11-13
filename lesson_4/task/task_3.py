class Adress:
    def __init__(self,city,street,num_build,post_num,num_phone=None,email=None):
        self.city = city
        self.street = street
        self.num_build = num_build
        self.post_num = post_num
        self.num_phone = num_phone
        self.email = email

    def __str__(self):
        return f'{self.city} {self.street} {self.num_build} {self.post_num} {self.post_num}' \
               f'{self.num_phone} {self.email}'

    def send_email(self,email,text):
        return f'Adress : {email}\nText: {text}'

class HomeAdress(Adress):
    def __init__(self,num_apartmet,num_phone_static,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.num_apartmet = num_apartmet
        self.num_phone_static = num_phone_static

    def __str__(self):
        return f'{super().__str__()}' \
               f'{self.num_apartmet} {self.num_phone_static}'

class WorkAdress(Adress):
    def __init__(self,name_corp,num_room,email_official,inside_num_room,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.name_corp = name_corp
        self.num_room = num_room
        self.email_official = email_official
        self.inside_num_room = inside_num_room

    def __str__(self):
        return f'{super().__str__()}' \
               f'{self.name_corp} {self.num_room} ' \
               f'{self.email_official} {self.inside_num_room}'

    def telephone_call(self):
        number = f'{self.num_phone}{self.inside_num_room}'
        print("Number: ",number)

    def send_email(self,official,text):
        if official:
            super().send_email(self.email_official,text)
        else:
            super().send_email(self.email,text)

class UniversityAdress(WorkAdress):
    def __init__(self,department,cathedral,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.department = department
        self.cathedral = cathedral

    def __str__(self):
        return f'{super().__str__()}' \
               f'{self.department} {self.cathedral}'

if __name__ == '__main__':
    # adress = Adress()
    # work = WorkAdress()
    university = UniversityAdress('WIETnam','Telekomunikacja','AGH','11','kondys@student.agh.edu.pl','120','Harkabuz','kościelna','22a','34-721','881432903','krzysiekkondys@gmail.com')
    print(university)