import os
import tkinter as tk
from tkinter import ttk, messagebox
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

class HospitalGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hospital Management System")
        self.root.geometry("800x600")
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        bg_color = '#2E2E2E'
        fg_color = '#FFFFFF'
        accent_color = '#007ACC'
        
        style.configure('TFrame', background=bg_color)
        style.configure('TLabelframe', background=bg_color, foreground=fg_color)
        style.configure('TLabelframe.Label', background=bg_color, foreground=fg_color, font=('Segoe UI', 12, 'bold'))
        style.configure('TLabel', background=bg_color, foreground=fg_color, font=('Segoe UI', 11))
        style.configure('TEntry', fieldbackground='#3E3E3E', foreground=fg_color, font=('Segoe UI', 11))
        style.configure('TButton', background=accent_color, foreground=fg_color, font=('Segoe UI', 11, 'bold'))
        style.map('TButton', background=[('active', '#005999')])
        
        # Configure Treeview
        style.configure('Treeview', 
            background='#3E3E3E',
            foreground=fg_color,
            fieldbackground='#3E3E3E',
            font=('Segoe UI', 13),
            rowheight=30)
        
        style.configure('Treeview.Heading',
            background=bg_color,
            foreground=fg_color,
            font=('Segoe UI', 13, 'bold'))
            
        # Enable grid lines
        tree_style = ttk.Style()
        tree_style.configure('Treeview', show='headings', selectmode='browse')
        tree_style.layout('Treeview', [('Treeview.treearea', {'sticky': 'nswe'})])
        
        # Configure colors for grid lines
        tree_style.configure('Treeview',
            background='#3E3E3E',
            foreground=fg_color,
            fieldbackground='#3E3E3E',
            borderwidth=1,
            relief='solid')
        style.map('Treeview', background=[('selected', accent_color)])
        
        # Configure root window
        self.root.configure(bg=bg_color)
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(expand=True, fill='both')
        
        # Create login frame
        self.login_frame = ttk.LabelFrame(self.main_frame, text="Admin Login", padding="20")
        self.login_frame.pack(expand=True)
        
        # Username field
        ttk.Label(self.login_frame, text="Username:").grid(row=0, column=0, padx=5, pady=5)
        self.username_var = tk.StringVar()
        self.username_entry = ttk.Entry(self.login_frame, textvariable=self.username_var)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Password field
        ttk.Label(self.login_frame, text="Password:").grid(row=1, column=0, padx=5, pady=5)
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(self.login_frame, textvariable=self.password_var, show='*')
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Login button
        self.login_button = ttk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=20)
        
        # Create admin instance
        self.admin = Admin("admin", "123")
        
        # Load data from files
        self.doctors = self.load_doctors()
        self.patients = self.load_patients()
    
    def load_doctors(self):
        doctors = []
        try:
            doctors_file = os.path.join(os.path.dirname(__file__), 'data', 'doctors.txt')
            with open(doctors_file, 'r') as file:
                for line in file:
                    first_name, surname, speciality = line.strip().split(',')
                    doctors.append(Doctor(first_name, surname, speciality))
        except FileNotFoundError:
            messagebox.showerror("Error", f"doctors.txt file not found at {doctors_file}!")
        return doctors
    
    def load_patients(self):
        patients = []
        try:
            patients_file = os.path.join(os.path.dirname(__file__), 'data', 'patients.txt')
            with open(patients_file, 'r') as file:
                for line in file:
                    first_name, surname, age, mobile, postcode, symptoms, samefamily = line.strip().split(',')
                    patients.append(Patient(first_name, surname, int(age), mobile, postcode, symptoms, samefamily == 'true'))
        except FileNotFoundError:
            messagebox.showerror("Error", f"patients.txt file not found at {patients_file}!")
        return patients
    
    def login(self):
        try:
            username = self.username_var.get()
            password = self.password_var.get()
            if username == self.admin._Admin__username and password == self.admin._Admin__password:
                self.show_main_menu()
            else:
                raise Exception("The username or the password is incorrect.")
        except Exception as e:
            messagebox.showerror("Login Error", str(e))
    
    def show_main_menu(self):
        # Clear login frame
        self.login_frame.pack_forget()
        
        # Create menu frame
        self.menu_frame = ttk.LabelFrame(self.main_frame, text="Main Menu", padding="20")
        self.menu_frame.pack(expand=True)
        
        # Menu buttons
        ttk.Button(self.menu_frame, text="Doctor Management", 
                  command=self.show_doctor_management).pack(pady=10)
        ttk.Button(self.menu_frame, text="View Patients", 
                  command=self.show_patients).pack(pady=10)
        ttk.Button(self.menu_frame, text="Assign Doctor to Patient", 
                  command=self.show_assign_doctor).pack(pady=10)
    
    def show_doctor_management(self):
        # Create a new window for doctor management
        doctor_window = tk.Toplevel(self.root)
        doctor_window.title("Doctor Management")
        doctor_window.geometry("600x400")
        
        # Create buttons frame
        buttons_frame = ttk.Frame(doctor_window, padding="10")
        buttons_frame.pack(fill='x')
        
        # Add buttons
        ttk.Button(buttons_frame, text="Register New Doctor", command=self.register_doctor).pack(side='left', padx=5)
        ttk.Button(buttons_frame, text="Update Doctor", command=self.update_doctor).pack(side='left', padx=5)
        ttk.Button(buttons_frame, text="Delete Doctor", command=self.delete_doctor).pack(side='left', padx=5)
        
        # Create treeview for doctors list
        tree_frame = ttk.Frame(doctor_window)
        tree_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        tree = ttk.Treeview(tree_frame, columns=("ID", "Name", "Speciality"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Full Name")
        tree.heading("Speciality", text="Speciality")
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Populate tree with doctors
        for i, doctor in enumerate(self.doctors):
            tree.insert("", "end", values=(i+1, doctor.full_name(), doctor.get_speciality()))
    
    def register_doctor(self):
        # Create registration dialog
        dialog = tk.Toplevel(self.root)
        dialog.title("Register New Doctor")
        dialog.geometry("400x350")
        dialog.configure(bg='#f0f0f0')
        
        # Create entry frame
        entry_frame = ttk.Frame(dialog, padding="20")
        entry_frame.pack(fill='x', padx=10, pady=5)
        
        # Create entry fields
        ttk.Label(entry_frame, text="First Name:").pack(pady=5)
        first_name_var = tk.StringVar()
        ttk.Entry(entry_frame, textvariable=first_name_var).pack(fill='x')
        
        ttk.Label(entry_frame, text="Surname:").pack(pady=5)
        surname_var = tk.StringVar()
        ttk.Entry(entry_frame, textvariable=surname_var).pack(fill='x')
        
        ttk.Label(entry_frame, text="Speciality:").pack(pady=5)
        speciality_var = tk.StringVar()
        ttk.Entry(entry_frame, textvariable=speciality_var).pack(fill='x')
        
        # Create button frame
        button_frame = ttk.Frame(dialog, padding="10")
        button_frame.pack(fill='x', side='bottom', padx=10, pady=10)
        
        def save_doctor():
            first_name = first_name_var.get()
            surname = surname_var.get()
            speciality = speciality_var.get()
            
            if first_name and surname and speciality:
                new_doctor = Doctor(first_name, surname, speciality)
                self.doctors.append(new_doctor)
                # Save to file
                try:
                    doctors_file = os.path.join(os.path.dirname(__file__), 'data', 'doctors.txt')
                    with open(doctors_file, 'a') as file:
                        file.write(f'{first_name},{surname},{speciality}\n')
                    messagebox.showinfo("Success", "Doctor registered successfully!")
                    dialog.destroy()
                    self.show_doctor_management()
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save doctor: {str(e)}")
            else:
                messagebox.showerror("Error", "All fields are required!")
        
        ttk.Button(dialog, text="Save", command=save_doctor).pack(pady=20)
    
    def show_patients(self):
        # Create a new window for patients view
        patient_window = tk.Toplevel(self.root)
        patient_window.title("Patients List")
        patient_window.geometry("800x400")
        
        # Create treeview for patients list
        tree_frame = ttk.Frame(patient_window)
        tree_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        tree = ttk.Treeview(tree_frame, columns=("ID", "Name", "Doctor", "Age", "Mobile", "Postcode"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Full Name")
        tree.heading("Doctor", text="Doctor")
        tree.heading("Age", text="Age")
        tree.heading("Mobile", text="Mobile")
        tree.heading("Postcode", text="Postcode")
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Populate tree with patients
        for i, patient in enumerate(self.patients):
            tree.insert("", "end", values=(i+1, patient.full_name(), patient.get_doctor(), 
                                         patient.get_age(), patient.get_mobile(), patient.get_postcode()))
    
    def update_doctor(self):
        # Create update dialog
        dialog = tk.Toplevel(self.root)
        dialog.title("Update Doctor")
        dialog.geometry("400x400")
        dialog.configure(bg='#f0f0f0')
        
        # Create selection frame
        selection_frame = ttk.LabelFrame(dialog, text="Select Doctor", padding="10")
        selection_frame.pack(fill='x', padx=5, pady=5)
        
        # Doctor selection combobox
        doctor_var = tk.StringVar()
        doctor_combo = ttk.Combobox(selection_frame, textvariable=doctor_var)
        doctor_combo['values'] = [doctor.full_name() for doctor in self.doctors]
        doctor_combo.pack(pady=5)
        
        # Update fields frame
        update_frame = ttk.LabelFrame(dialog, text="Update Fields", padding="10")
        update_frame.pack(fill='x', padx=5, pady=5)
        
        # Entry fields
        ttk.Label(update_frame, text="First Name:").pack(pady=2)
        first_name_var = tk.StringVar()
        first_name_entry = ttk.Entry(update_frame, textvariable=first_name_var)
        first_name_entry.pack(pady=2)
        
        ttk.Label(update_frame, text="Surname:").pack(pady=2)
        surname_var = tk.StringVar()
        surname_entry = ttk.Entry(update_frame, textvariable=surname_var)
        surname_entry.pack(pady=2)
        
        ttk.Label(update_frame, text="Speciality:").pack(pady=2)
        speciality_var = tk.StringVar()
        speciality_entry = ttk.Entry(update_frame, textvariable=speciality_var)
        speciality_entry.pack(pady=2)
        
        def on_doctor_select(event):
            selected = doctor_combo.get()
            for doctor in self.doctors:
                if doctor.full_name() == selected:
                    first_name_var.set(doctor.get_first_name())
                    surname_var.set(doctor.get_surname())
                    speciality_var.set(doctor.get_speciality())
                    break
        
        doctor_combo.bind('<<ComboboxSelected>>', on_doctor_select)
        
        def save_updates():
            selected = doctor_combo.get()
            if not selected:
                messagebox.showerror("Error", "Please select a doctor to update")
                return
                
            first_name = first_name_var.get()
            surname = surname_var.get()
            speciality = speciality_var.get()
            
            if first_name and surname and speciality:
                # Find and update the doctor
                for doctor in self.doctors:
                    if doctor.full_name() == selected:
                        doctor.set_first_name(first_name)
                        doctor.set_surname(surname)
                        doctor.set_speciality(speciality)
                        break
                
                # Update the file
                try:
                    with open('data/doctors.txt', 'w') as file:
                        for doc in self.doctors:
                            file.write(f'{doc.get_first_name()},{doc.get_surname()},{doc.get_speciality()}\n')
                    messagebox.showinfo("Success", "Doctor updated successfully!")
                    dialog.destroy()
                    self.show_doctor_management()
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to update doctor: {str(e)}")
            else:
                messagebox.showerror("Error", "All fields are required!")
        
        ttk.Button(dialog, text="Save Updates", command=save_updates).pack(pady=20)
    
    def delete_doctor(self):
        # Create delete dialog
        dialog = tk.Toplevel(self.root)
        dialog.title("Delete Doctor")
        dialog.geometry("400x200")
        
        # Create selection frame
        selection_frame = ttk.LabelFrame(dialog, text="Select Doctor to Delete", padding="10")
        selection_frame.pack(fill='x', padx=5, pady=5)
        
        # Doctor selection combobox
        doctor_var = tk.StringVar()
        doctor_combo = ttk.Combobox(selection_frame, textvariable=doctor_var)
        doctor_combo['values'] = [doctor.full_name() for doctor in self.doctors]
        doctor_combo.pack(pady=5)
        
        def delete_selected():
            selected = doctor_combo.get()
            if not selected:
                messagebox.showerror("Error", "Please select a doctor to delete")
                return
            
            if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {selected}?"):
                # Find and delete the doctor
                for i, doctor in enumerate(self.doctors):
                    if doctor.full_name() == selected:
                        self.doctors.pop(i)
                        break
                
                # Update the file
                try:
                    with open('data/doctors.txt', 'w') as file:
                        for doc in self.doctors:
                            file.write(f'{doc.get_first_name()},{doc.get_surname()},{doc.get_speciality()}\n')
                    messagebox.showinfo("Success", "Doctor deleted successfully!")
                    dialog.destroy()
                    self.show_doctor_management()
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to delete doctor: {str(e)}")
        
        ttk.Button(dialog, text="Delete Doctor", command=delete_selected).pack(pady=20)
    
    def show_assign_doctor(self):
        # Create assignment dialog
        dialog = tk.Toplevel(self.root)
        dialog.title("Assign Doctor to Patient")
        dialog.geometry("500x500")
        dialog.configure(bg='#f0f0f0')
        
        # Create patient selection frame
        patient_frame = ttk.LabelFrame(dialog, text="Select Patient", padding="10")
        patient_frame.pack(fill='x', padx=5, pady=5)
        
        # Patient selection combobox
        patient_var = tk.StringVar()
        patient_combo = ttk.Combobox(patient_frame, textvariable=patient_var, width=40)
        patient_combo['values'] = [f"{patient.full_name()} (Age: {patient.get_age()})" for patient in self.patients]
        patient_combo.pack(pady=5)
        
        # Create doctor selection frame
        doctor_frame = ttk.LabelFrame(dialog, text="Select Doctor", padding="10")
        doctor_frame.pack(fill='x', padx=5, pady=5)
        
        # Doctor selection combobox
        doctor_var = tk.StringVar()
        doctor_combo = ttk.Combobox(doctor_frame, textvariable=doctor_var, width=40)
        doctor_combo['values'] = [f"{doctor.full_name()} ({doctor.get_speciality()})" for doctor in self.doctors]
        doctor_combo.pack(pady=5)
        
        def assign_doctor():
            selected_patient = patient_combo.get()
            selected_doctor = doctor_combo.get()
            
            if not selected_patient or not selected_doctor:
                messagebox.showerror("Error", "Please select both a patient and a doctor")
                return
            
            # Extract patient name from selection
            patient_name = selected_patient.split(' (Age:')[0]
            doctor_name = selected_doctor.split(' (')[0]
            
            # Find the selected patient and doctor
            selected_patient_obj = None
            selected_doctor_obj = None
            
            for patient in self.patients:
                if patient.full_name() == patient_name:
                    selected_patient_obj = patient
                    break
            
            for doctor in self.doctors:
                if doctor.full_name() == doctor_name:
                    selected_doctor_obj = doctor
                    break
            
            if selected_patient_obj and selected_doctor_obj:
                # Assign doctor to patient
                selected_patient_obj.set_doctor(selected_doctor_obj)
                messagebox.showinfo("Success", f"Doctor {doctor_name} has been assigned to patient {patient_name}")
                dialog.destroy()
            else:
                messagebox.showerror("Error", "Failed to assign doctor to patient")
        
        ttk.Button(dialog, text="Assign Doctor", command=assign_doctor).pack(pady=20)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = HospitalGUI()
    app.run()