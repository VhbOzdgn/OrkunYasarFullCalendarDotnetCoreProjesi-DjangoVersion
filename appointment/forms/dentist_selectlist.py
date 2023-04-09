from django import forms
from account.models import AppUser


class DentistSelectList(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'] = forms.ChoiceField(choices=self.get_dentists(
        ), widget=forms.Select(attrs={'id': 'selectDentistId', 'class': 'form-control'}), label='Diş Hekimi')

    def get_dentists(self):
        dentists = AppUser.objects.filter(is_dentist=True)
        choices = [(d.id, d.get_full_name) for d in dentists]
        return choices
