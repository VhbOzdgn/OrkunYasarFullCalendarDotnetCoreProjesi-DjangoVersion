from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.middleware import csrf
from account.models import AppUser
from appointment.forms import AppointmentForm


@login_required(login_url='login')
def index_view(request):
    # csrf_token = csrf.get_token(request)
    if request.user.role:
        if request.user.role == AppUser.Roles.SECRETARY:
            return render(request, 'pages/secretary.html', context={
                "dentists": AppUser.objects.filter(is_dentist=True),
                # "dentist_select_list": DentistSelectList(),
                'form':AppointmentForm()
                # 'csrf_token': csrf_token
            })
        elif request.user.role == AppUser.Roles.DENTIST:
            return render(request, 'pages/dentist.html', context={'form':AppointmentForm()})
    return HttpResponseNotFound()
