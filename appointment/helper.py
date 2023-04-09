from django.utils import timezone
from datetime import datetime
from django.utils import timezone
from django.db.models.functions import Concat
from django.db.models import F, Value
from .models import Appointment


def parse_datetime(datetime_str):
    return datetime.strptime(datetime_str, '%d/%m/%Y %H:%M').replace(tzinfo=timezone.utc)


def get_appointment_view_models(userid: int = None):
    appointments = Appointment.objects.annotate(
        dentist_full_name=Concat(
            F('user__first_name'), Value(' '), F('user__last_name'))
    ).values(
        'id',
        'start_date',
        'end_date',
        'dentist_full_name',
        'patient_name',
        'patient_surname',
        'description',
        'user__id',
        'user__color'
    )
    if userid:
        return appointments.filter(user__id=userid)
    return appointments
