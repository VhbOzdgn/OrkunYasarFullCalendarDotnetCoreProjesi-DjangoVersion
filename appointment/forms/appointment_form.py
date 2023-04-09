from django import forms
from appointment.models import Appointment
from account.models import AppUser


class AppointmentForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=AppUser.objects.filter(is_dentist=True), widget=forms.Select(
        attrs={'id': 'selectDentistId', 'class': 'form-control'}), label=None, empty_label=None)

    class Meta:
        model = Appointment
        exclude = ('created_date', 'updated_date')
        widgets = {
            'start_date': forms.TextInput(attrs={'id': 'inputStartDate', 'class': 'form-control datetimepicker-input', 'data-target': '#datetimepicker1'}),
            'end_date': forms.TextInput(attrs={'id': 'inputEndDate', 'class': 'form-control datetimepicker-input', 'data-target': '#datetimepicker2'}),
            'patient_name': forms.TextInput(attrs={'id': 'inputPatientName', 'class': 'form-control'}),
            'patient_surname': forms.TextInput(attrs={'id': 'inputPatientSurname', 'class': 'form-control'}),
            'description': forms.TextInput(attrs={'id': 'inputDescription', 'class': 'form-control'}),
        }
