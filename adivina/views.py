from django.shortcuts import render
import random

def home(request):
    return render(request, 'adivina/home.html')

def guess(request):
    ramdom_number = random.randint(1, 100)
    number_user = int(request.POST['guess'])
    if number_user == ramdom_number:
        message = 'Congratulations, you guessed the number'
    elif number_user > ramdom_number:
        message = 'Your guess is too high. Try again'
    else:
        message = 'Your guess is too low. Try again'
    return render(request, 'adivina/guess.html', {'message':message})