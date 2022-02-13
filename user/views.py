from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token
from .forms import Login_Form, SignUpForm
from .models import MyUser


@login_required
def index_auth(request):
    context = {'user' : request.user}
    return render(request, 'user/index.html', context)



@login_required
def profile(request):
    context = {'user' : request.user}
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



def logout_view(request):
    logout(request)
    return redirect('user:index')


def csrf_failure(request, reason=""):
    ctx = {'message': 'some custom messages'}
    return render(request, 'home/index.html' )