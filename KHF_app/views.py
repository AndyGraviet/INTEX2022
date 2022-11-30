from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import recommendation, user, food_item, food_item_in_meal, meal

# Create your views here.

def indexPageView(request):

    return render(request, 'index.html')

@login_required
def fillAccount(request):
    recommendations = recommendation.objects.all()

    #get email of registered user
    currEmail = request.user.email 
    #check if registered email is already in the db
    data = user.objects.filter(email=currEmail)

    if data.count() > 0:
        #if the email IS in the db, render the account page
        context = {
            "auth": request.user,
            "currUser" : data
        }
        return render(request, 'dashboard.html', context)
    else:
        context = {
            'data': recommendations,
            'user': request.user,
        }
        return render(request, 'account.html', context)

    

@login_required
def viewAccount(request):
    currEmail = request.user.email 
    #check if registered email is already in the db
    data = user.objects.filter(email=currEmail)
    context = {
        'currUser': data
    }
    
    return render(request, 'viewAccount.html', context)
@login_required
def viewDashboard(request):
    currEmail = request.user.email 
    #check if registered email is already in the db
    data = user.objects.filter(email=currEmail)
    context = {
        'currUser': data
    }
    return render(request, 'dashboard.html', context)

@login_required
def logout(request):
    django_logout(request)
    domain = settings.SOCIAL_AUTH_AUTH0_DOMAIN
    client_id = settings.SOCIAL_AUTH_AUTH0_KEY
    return_to = 'http://127.0.0.1:8000'
    return redirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')

def storeUserPageView(request):
    if request.method == 'POST':

        new_user = user()

        #stores the data from each field into the specified spot in the database

        new_user.first_name = request.POST.get('first_name')

        new_user.last_name = request.POST.get('last_name')

        new_user.sex = request.POST.get('sex')

        new_user.height = request.POST.get('height')

        new_user.age = request.POST.get('age')

        new_user.weight = request.POST.get('weight')

        new_user.email = request.user.email

        new_comorbidity = recommendation.objects.get(comorbidity = request.POST.get('comorbidity'))

        new_user.comorbidity = new_comorbidity

        new_user.save()

    data = user.objects.all()

    context = {
        'users' : data
    }


    return render(request, 'dashboard.html', context)

