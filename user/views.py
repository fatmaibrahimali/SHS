from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token
from .forms import Login_Form, SignUpForm, UserProfileForm, UserVitalForm
from .models import MyUser, UserProfile, UserVital
from datetime import date
 
 
 
def get_age(BD):  #BD = DateField
    today = date.today()
    delta = today - BD
    yy    = delta.days//365
    mm    = (delta.days%365)//30
    dd    = (delta.days%365)%30
    return yy,mm



def index(request):
    context = {}
    perm = False
    
    user = request.user
    if user.is_authenticated: 
        return redirect("user:profile")
    
    if request.POST:
        form = Login_Form(request.POST)
        if form.is_valid() :
            username = request.POST['username']
            password = request.POST['password']
            try:
                username = MyUser.objects.get(email=username)
            except:
                username = username
            user = authenticate(username=username, password=password)
            if user :
                login(request, user)
                return redirect("user:profile")
            else :
                perm = True   #invalid login -- not allowed
    else :
        form = Login_Form()
        
    context['form'] = form
    context['perm'] = perm
    return render(request, "user/index.html", context)



@login_required
def index_auth(request):
    context = {'user' : request.user}
    return render(request, 'user/index.html', context)



@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user = request.user)
    context = {
        'user'        : request.user,
        'user_profile': user_profile,
        'user_vital'  : UserVital.objects.get(user = request.user),
        'user_age'    : get_age(user_profile.birth_date),
        }
    return render(request, 'user/profile.html', context)



@requires_csrf_token
@csrf_exempt
@csrf_protect
def signup(request):
    context = {}
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            account = authenticate(username = username, password = password)
            login(request, account)
            return redirect('user:profile')  
        else :
            context['form'] = form
    else : # GET request
        form = SignUpForm()
        context['form'] = form
    return render(request, 'user/register.html', context)



@login_required
def profile_edit(request):
    
    user_profile = UserProfile.objects.get(user = request.user)
    user_vital = UserVital.objects.get(user = request.user)
    
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance = user_profile)
        vital_form = UserVitalForm(request.POST, instance = user_vital)
        if profile_form.is_valid() and vital_form.is_valid() :
            profile_form.save()
            vital_form.save()
            return redirect(reverse('user:profile'))
    else:
        profile_form = UserProfileForm(instance = user_profile)
        vital_form = UserVitalForm(instance = user_vital)
    context = {'profile_form':profile_form, 'vital_form':vital_form}
    return render(request, 'user/edit.html', context)




def logout_view(request):
    logout(request)
    return redirect('user:index')


def csrf_failure(request, reason=""):
    ctx = {'message': 'some custom messages'}
    return render(request, 'home/index.html' )