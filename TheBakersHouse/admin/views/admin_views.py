from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from products.models import orders,messages
from django.http import HttpResponse , HttpResponseRedirect

# Create your views here.

def dashboard(request):
    context = dict()
    context['orders'] = orders.objects.all().order_by('-date')
    context['messages'] = messages.objects.all().order_by('-date')
    return render(request,'admin/dashboard.html',context)

def update_profile(request):
    context = dict()
    admin_users = User.objects.filter(is_superuser = True)
    if request.method == "POST":
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        admin_user = User.objects.get(username=username)
        admin_user.username = username
        admin_user.first_name = first_name
        admin_user.email = email
        admin_user.save()

        return redirect(reverse('admin:update-profile'))
        
    return render(request,'admin/update_profile.html',{"admin_user":admin_users})

def user_list(request):
    context = dict()
    user = User.objects.filter(is_superuser = True )
    context['users'] = user
    return render(request,'admin/user_list.html',context)

