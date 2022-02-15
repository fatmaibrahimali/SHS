from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import UserVitalForm
from .models import UserVital
from patient.models import Appointments
from staff.models import JobProfile
from user.models import MyUser




@login_required
def book(request):
    doctors = JobProfile.objects.filter(job = 'Dr')
    return render(request, "patient/book.html", {'doctors':doctors})



@login_required
def appoints(request):
    apps = Appointments.objects.filter(patient = request.user)
    return render(request, "patient/appoints.html", {'apps':apps})

@login_required
def reserve(request, username): #username of doctor
    doc = MyUser.objects.get(username = username)
    pat = request.user
    Appointments.objects.create(doctor = doc, patient=pat)
    return redirect('patient:appoints')


@login_required
def profile_edit(request):
    user_vital = UserVital.objects.get(user = request.user)
    
    if request.method == 'POST':
        vital_form = UserVitalForm(request.POST, instance = user_vital)
        if vital_form.is_valid() :
            vital_form.save()
            return redirect(reverse('user:profile'))
    else:
        vital_form = UserVitalForm(instance = user_vital)
    context = {'vital_form':vital_form}
    return render(request, 'user/edit.html', context)
