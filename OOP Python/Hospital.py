class MedicalStaff:
    def __init__(self, staff_id, name, specialization):
        self.staff_id = staff_id
        self.name = name
        self.specialization = specialization

class Doctor(MedicalStaff):
    def __init__(self, staff_id, name, specialization, license_number):
        super().__init__(staff_id, name, specialization)
        self.license_number = license_number

class Nurse(MedicalStaff):
    def __init__(self, staff_id, name, specialization, certification):
        super().__init__(staff_id, name, specialization)
        self.certification = certification

class Pharmacist(MedicalStaff):
    def __init__(self, staff_id, name, specialization, license_number):
        super().__init__(staff_id, name, specialization)
        self.license_number = license_number

class Appointment:
    def __init__(self, appointment_id, patient_name, date_time):
        self.appointment_id = appointment_id
        self.patient_name = patient_name
        self.date_time = date_time
        self.medical_staff = None

class GeneralCheckup(Appointment):
    def __init__(self, appointment_id, patient_name, date_time):
        super().__init__(appointment_id, patient_name, date_time)

class SpecialistConsultation(Appointment):
    def __init__(self, appointment_id, patient_name, date_time, specialist):
        super().__init__(appointment_id, patient_name, date_time)
        self.specialist = specialist

class FollowUpAppointment(Appointment):
    def __init__(self, appointment_id, patient_name, date_time, original_appointment_id):
        super().__init__(appointment_id, patient_name, date_time)
        self.original_appointment_id = original_appointment_id


class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name


class HospitalSystem:
    def __init__(self):
        self.medical_staff_list = []
        self.appointments_list = []
        self.patients_list = []

    def add_medical_staff(self, staff):
        self.medical_staff_list.append(staff)

    def add_patient(self, patient):
        self.patients_list.append(patient)

    def schedule_appointment(self, appointment):
        self.appointments_list.append(appointment)

    def assign_medical_staff(self, appointment_id, medical_staff_id):
        appointment = None
        for app in self.appointments_list:
            if app.appointment_id == appointment_id:
                appointment = app
                break

        medical_staff = None
        for staff in self.medical_staff_list:
            if staff.staff_id == medical_staff_id:
                medical_staff = staff
                break

        if appointment and medical_staff:
            appointment.medical_staff = medical_staff
            print(f"Appointment {appointment_id} assigned to {medical_staff.name} ({medical_staff.specialization})")

    def add_new_patient(self, patient):
        self.patients_list.append(patient)
        print(f"Patient {patient.name} added to the system.")

# Create a hospital system
hospital = HospitalSystem()

# Add medical staff
doctor1 = Doctor(1, "Dr. Smith", "Cardiologist", "12345")
nurse1 = Nurse(2, "Nurse Johnson", "Registered Nurse", "RN123")
pharmacist1 = Pharmacist(3, "Pharmacist Brown", "Pharmacist", "Pharm123")

hospital.add_medical_staff(doctor1)
hospital.add_medical_staff(nurse1)
hospital.add_medical_staff(pharmacist1)

# Add patients
patient1 = Patient(1, "John Doe")
patient2 = Patient(2, "Jane Doe")

hospital.add_patient(patient1)
hospital.add_patient(patient2)

# Schedule appointments
appointment1 = GeneralCheckup(101, "John Doe", "2024-03-15 10:00 AM")
appointment2 = SpecialistConsultation(102, "Jane Doe", "2024-03-16 2:30 PM", "Cardiologist")
appointment3 = FollowUpAppointment(103, "Bob Smith", "2024-03-17 3:45 PM", 101)

hospital.schedule_appointment(appointment1)
hospital.schedule_appointment(appointment2)
hospital.schedule_appointment(appointment3)

# Assign medical staff to appointments
hospital.assign_medical_staff(101, 1)
hospital.assign_medical_staff(102, 1)
hospital.assign_medical_staff(103, 2)

# Verify the added patients, medical staff, and appointments
print("\nPatients in the system:")
for patient in hospital.patients_list:
    print(f"Patient ID: {patient.patient_id}, Name: {patient.name}")

print("\nMedical Staff in the system:")
for staff in hospital.medical_staff_list:
    print(f"Staff ID: {staff.staff_id}, Name: {staff.name}, Specialization: {staff.specialization}")

print("\nAppointments in the system:")
for appointment in hospital.appointments_list:
    print(f"Appointment ID: {appointment.appointment_id}, Patient: {appointment.patient_name}, Date: {appointment.date_time}, Medical Staff: {appointment.medical_staff.name if appointment.medical_staff else 'Not assigned'}")
 
