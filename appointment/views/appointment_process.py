from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required, user_passes_test
from account.models import AppUser
from appointment.helper import get_appointment_view_models
from appointment.forms import AppointmentForm
from appointment.models import Appointment


@login_required(login_url='login')
@require_http_methods(['GET'])
def get_appointments(request):
    appointments = get_appointment_view_models()
    return JsonResponse({'model': list(appointments)})


@login_required(login_url='login')
@require_http_methods(['GET'])
def get_appointments_by_userid(request):
    userid = request.GET.get('userId')
    appointments = get_appointment_view_models(userid=int(userid))
    return JsonResponse({'model': list(appointments)})


@login_required(login_url='login')
@user_passes_test(lambda u: u.role == AppUser.Roles.SECRETARY)
@require_http_methods(['POST'])
def add_or_update_appointment(request):
    if not (request.POST.get('id')) or int(request.POST.get('id')) <= 0:
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': 200})
        else:
            return JsonResponse({'error': form.errors})
    else:
        appointment = Appointment.objects.get(id=request.POST.get('id'))
        if appointment:
            form = AppointmentForm(request.POST, instance=appointment)
            if form.is_valid():
                form.save()
                return JsonResponse({'success': 200})
            else:
                return JsonResponse({'error': form.errors})
    return JsonResponse({'error': 400})


@login_required(login_url='login')
@user_passes_test(lambda u: u.role == AppUser.Roles.SECRETARY)
@require_http_methods(['POST'])
def delete_appointment(request):
    id = request.POST.get('id')
    if id:
        appointment = Appointment.objects.get(pk=id)
        if not appointment:
            return JsonResponse({'error': 400})
        appointment.delete()
        return JsonResponse({'success': 200})
    return JsonResponse({'error': 400})
