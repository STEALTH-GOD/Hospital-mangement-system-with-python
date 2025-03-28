from Doctor import Doctor
import matplotlib.pyplot as plt

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input("Enter the username: ")
        password = input("Enter the password: ")

        # check if the username and password match the registered ones
        if not (username == self.__username and password == self.__password):
            raise Exception("The username or the password is incorrect.")
        else:
            return username
        

    def find_index(self,index,doctors):
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        first_name=input("Enter the first name of the doctor: ")
        surname=input("Enter the surname of the doctor: ")
        speciality=input("Enter the specality of the doctor: ")
        return first_name,surname,speciality #returns tuple

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')
        op=input("Choice: ")
        
        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            first_name,surname,speciality = self.get_doctor_details()

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    name_exists = True
                    pass # save time and end the loop

            if not name_exists:
                new_doctor=Doctor(first_name,surname,speciality)
                doctors.append(new_doctor)
                print('Doctor registered.')

        # View  
        elif op == '2':
            print("-----List of Doctors-----")
            print('ID |          Full name           |  Speciality')
            self.view(doctors)
            

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input("Enter the ID of the doctor: "))- 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                        break
            
                    else:
                        print("Doctor not found")

                        # doctor_index is the ID mines one (-1)
                        
                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated (1-3):')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            opp = input('Choice:').lower() # make the user input lowercase
            #ToDo8
            if opp=='1':
                new_first_name = input("Enter the new first name: ")
                doctors[index].set_first_name(new_first_name)
            elif opp=='2':
                new_surname = input("Enter the new surname: ")
                doctors[index].set_surname(new_surname)
            elif opp=='3':
                new_speciality=input("Enter the new speciality: ")
                doctors[index].set_speciality(new_speciality)
            else:
                print("Invalid choice. Please choose a valid option.")
                #break or pass?

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = int(input("Enter the ID of the doctor to be deleted: ")) - 1 #doctor index is id minus 1
            # ToDo9
            if 0<=doctor_index<=len(doctors)-1:
                deleted_doctor=doctors.pop(doctor_index)
                print(f"Doctor {deleted_doctor.full_name()} deleted.")

            else:
                 print('The id entered is incorrect')

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        for index, patient in enumerate(patients):
            print(f'{index+1:3}|{patient}')
    
    
    def assign_doctor_to_patient(self,patients,doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        assign=[]
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input("Please enter the patient ID: ")

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input("Please enter the doctor ID: ")

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                # patients[patient_index].set_assigned_doctor(doctors[doctor_index])
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index])
                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')

    def discharge(self, patients, discharged_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        while True:    
            discharge_option=input("Do you want to discharge a patient? (Y/N):").lower()
            if discharge_option=='y':
                try:
                    print("-----Discharge Patient-----")    
                    self.view_patient(patients) 
                    patient_index = int(input('Please enter the patient ID: '))-1

                    if patient_index in range(len(patients)):
                        discharged_patient=patients.pop(patient_index)
                        discharged_patients.append(discharged_patient)
                        print("Patient discharged successfully.")
                    
                    else:
                        print("The entered patient ID is not found. Please try again.")

                except ValueError:
                    print("Incorrect input! Please enter a number.")
            elif discharge_option == "n":
                break
            else:
                print("Invalid option! Please enter Y or N.")
            


    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')

        for index, patient in enumerate(discharged_patients):
            print(f'{index+1:3}|{patient}')
        
    def relocate_doctor(self,patients,doctors):
        print("----Reassign doctor----")
        print("----List of Patients----")
        self.view(patients)

        if len(patients) !=0:
            try:
                patient_index=int(input("Enter the ID of the patient to relocate the doctor from:"))-1

                if patient_index>=0 and patient_index<len(patients):
                    print("----List of doctors---")
                    self.view(doctors)
                    
                    new_doctor=int(input("Enter the ID of teh new doctor: "))-1

                    if new_doctor>=0 and new_doctor<=len(doctors):
                        
                        old_doctor_full_name=patients[patient_index].get_doctor()
                        patients[patient_index].link(doctors[new_doctor].full_name())
                        doctors[new_doctor].add_patient(patients[patient_index])
                        

                        print(f'successfully relocated {old_doctor_full_name} to {doctors[new_doctor].full_name()}')
                        
                    
                    else:
                        print("invalid new doctor ID.")
                
                else: 
                    print("Invalid patient ID.")

            except ValueError:
                print('Invalid input.')

        else:
            print(f"No patients available.")
        
    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            new_username = input("Enter the new username: ")
            self.__username=new_username
            print(f'Username has been successfully changed to {new_username}.')

        elif op == 2:
            password = input("Enter the new password: ")
            # validate the password
            if password == input("Enter the new password again: "):
                self.__password = password
                print("Password has been successfully changed.")
            else:
                print("Passwords do not match. Please try again.")
            
        elif op == 3:
            new_address=input("Enter the new address.")
            self.__address=new_address
            print(f"Address has been successfully changed to {new_address}.")

        else:
            print("Invalid choice.Please choose a valid option.")

    def grouped_patients(self,patients):
        same_family=[str(patient) for patient in patients if patient.get_surname()=="Smith"]
        self.view(same_family)
  
    def get_management_report(self,patients,doctors):
        print('---Management Report---')
        print('Choose an option:')
        print('1 - Total number of doctors in the system.')
        print('2 - Total number of patients per doctor.')
        print('3 - Total number of appointments per month per doctor.')
        print('4 - Total number of patients based on illness type.')
        op = int(input ('Choose an option:'))
        
        try:
            if  op==1:
                print(f"The total number of doctors: {len(doctors)}")

            elif op==2:
                for doc in doctors:
                    total_patients=doc.get_total_patients()
                    print(f"{doc.full_name()} has {total_patients} patient." )

            elif op==3:
                for doc in doctors:
                    total_appointments=doc.get_total_appointments()
                    print(f"{doc.full_name()} has {total_appointments} per month." )

            elif op ==4:
                symptoms = list(set(tuple(patient.get_symptoms()) for patient in patients))

                for symptom in symptoms:
                    num_of_patients = sum(1 for patient in patients if tuple(patient.get_symptoms()) == symptom)
                    symptom_str = str(symptom[0]).strip("()")  # converting symptom  tuple to string and remvoing bracket
                    print(f"Number of people with {symptom_str} are {num_of_patients}")
                            
            else:
                print("Invalid option.")

        except Exception as e:
            print(f"Unexpected error: {e}")
    

    
    @staticmethod
    #for not depending on instances
    

    def generate_management_report_chart(patients, doctors):
        
        print('---Management Report Chart---')
        print('Choose an option:')
        print('1 - Total number of doctors in the system.')
        print('2 - Total number of patients per doctor.')
        print('3 - Total number of appointments per month per doctor.')
        print('4 - Total number of patients based on illness type.')
        op = int(input('Choose an option: '))

        try:
            if op == 1:
                labels = ['Total Doctors']
                data = [len(doctors)]
                title = 'Total Number of Doctors in the System'

            elif op == 2:
                labels = [doc.full_name() for doc in doctors]
                data = [doc.get_total_patients() for doc in doctors]
                title = 'Total Number of Patients per Doctor'

            elif op == 3:
                labels = [doc.full_name() for doc in doctors]
                data = [doc.get_total_appointments() for doc in doctors]
                title = 'Total Number of Appointments per Month per Doctor'

            elif op == 4:
                labels = [', '.join(symptom) for symptom in set(tuple(patient.get_symptoms()) for patient in patients)]#crates list sperated by commas
                data = [sum(1 for patient in patients if tuple(patient.get_symptoms()) == symptom) for symptom in set(tuple(patient.get_symptoms()) for patient in patients)]#creates new list of total no of patients with diff symptoms
                title = 'Total Number of Patients Based on Illness Type'

            else:
                print("Invalid option.")
                

            # Generating Bar Chart
            plt.bar(labels, data)
            plt.xlabel('Categories')
            plt.ylabel('Counts')
            plt.title(title)
            plt.show()

        except Exception as e:
            print(f"Unexpected error: {e}")

    

    
    

            





       
