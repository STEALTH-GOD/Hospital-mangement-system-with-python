    # Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234','stomachache'), Patient('Mike','Jones', 37,'07555551234','L2 2AB','backsprain'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC','fever')]
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- View patients')
        print(' 3- Discharge patients')
        print(' 4- View discharged patient')
        print(' 5- Assign doctor to a patient')
        print(' 6- Relocate doctor of a patient')
        print(' 7- Get managemnet report')
        print(' 8- Get managemnet report in bar chart')
        print(' 9- View patient from a same family')
        print(' 10- Update admin detais')
        print(' 11- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
          admin.doctor_management(doctors)

        elif op=='2':
            # 2- View patients
            admin.view_patient(patients)

        elif op == '3':
            # 3 discharge patient
            admin.discharge(patients,discharged_patients)
        
        elif op == '4':
            # 4 - view discharged patients
            admin.view_discharge(discharged_patients)

        elif op == '5':
            # 5- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients,doctors)

        elif op == '6':
            # 6- relocate doctor of a patient
            admin.relocate_doctor(patients,doctors)
        
        elif op == '7':
            # 7- Get management report
            admin.get_management_report(patients,doctors)
        
        elif op== '8':
            # 8- Bar Chart
            admin.generate_management_report_chart(patients,doctors)

        elif op =='9':
            # update admin details
            admin.grouped_patients(patients)

        elif op == '10':
            # 10- Update admin detais
            admin.update_details()

        elif op == '11':
            # 11 - Quit
            print("Quitting the program.")
            running=False
        
        

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
