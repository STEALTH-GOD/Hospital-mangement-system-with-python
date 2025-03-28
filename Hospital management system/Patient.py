class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode,symptoms,samefamily=False):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
        self.__first_name= first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__address= postcode
        self.__doctor = 'None'
        self.__symptoms= [symptoms]
        self.samefamily=samefamily

    def full_name(self) :
        """full name is first_name and surname"""
        return f"{self.__first_name} {self.__surname}"
    
    def get_surname(self):
        return self.__surname
       
    def get_age(self):
        return self.__age
    
    def get_mobile(self):
        return self.__mobile
    
    def get_postcode(self):
        return self.__address

    def get_doctor(self) :
        return self.__doctor
        
    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def get_symptoms(self):
        return self.__symptoms

    def print_symptoms(self):
        """prints all the symptoms"""
        for symptom in self.__symptoms:
            print(symptom)        
    
    def __str__(self):
        doctor_info = str(self.__doctor) if self.__doctor else 'None'
        return f'{self.full_name():^30}|{doctor_info:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__address:^10}'
