from django.urls import path
from .views.profile import index_view
from .views.appointment_process import *

app_name = "appointment"

urlpatterns = [
    path("", view=index_view, name="index"),
    path("get", view=get_appointments, name="get-appointmets"),
    path("getbydentist", view=get_appointments_by_userid,
         name="get-appointmets-by-userid"),
    path('add-or-update', view=add_or_update_appointment, name='add-or-update'),
    path('delete', view=delete_appointment, name='delete-appointment'),
]
