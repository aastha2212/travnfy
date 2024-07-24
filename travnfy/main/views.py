from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def create_account(request):
    return render(request, 'create_account.html')

def book_flights(request):
    if request.method == 'POST':
        departure_city = request.POST['departure_city']
        arrival_city = request.POST['arrival_city']
        trip_date = request.POST['trip_date']
        trip_type = request.POST['trip_type']
        return_date = request.POST.get('return_date', '')
        preferred_time = request.POST['preferred_time']
        name = request.POST['name']
        phone = request.POST['phone']

        subject = 'Flight Booking Request'
        message = (
            f"Name: {name}\n"
            f"Phone: {phone}\n"
            f"Departure City: {departure_city}\n"
            f"Arrival City: {arrival_city}\n"
            f"Trip Date: {trip_date}\n"
            f"Trip Type: {trip_type}\n"
            f"Return Date: {return_date}\n"
            f"Preferred Time: {preferred_time}"
        )
        recipient_list = ['aastha2212chaurasia@gmail.com']

        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
            messages.success(request, 'Email sent, we will contact you shortly.')
        except Exception as e:
            messages.error(request, 'Failed to send email. Please try again later.')

        return redirect('home')

    return render(request, 'book_flights.html')

def book_cabs(request):
    if request.method == 'POST':
        pickup_location = request.POST['pickup_location']
        dropoff_location = request.POST['dropoff_location']
        trip_date = request.POST['trip_date']
        trip_type = request.POST['trip_type']
        return_date = request.POST.get('return_date', '')
        name = request.POST['name']
        phone = request.POST['phone']

        subject = 'Cab Booking Request'
        message = (
            f"Name: {name}\n"
            f"Phone: {phone}\n"
            f"Pickup Location: {pickup_location}\n"
            f"Dropoff Location: {dropoff_location}\n"
            f"Trip Date: {trip_date}\n"
            f"Trip Type: {trip_type}\n"
            f"Return Date: {return_date}"
        )
        recipient_list = ['aastha2212chaurasia@gmail.com']

        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
            messages.success(request, 'Email sent, we will contact you shortly.')
        except Exception as e:
            messages.error(request, 'Failed to send email. Please try again later.')

        return redirect('home')

    return render(request, 'book_cabs.html')

def book_trains(request):
    if request.method == 'POST':
        from_location = request.POST['from_location']
        to_location = request.POST['to_location']
        trip_date = request.POST['trip_date']
        trip_type = request.POST['trip_type']
        return_date = request.POST.get('return_date', '')
        name = request.POST['name']
        phone = request.POST['phone']

        subject = 'Train Booking Request'
        message = (
            f"Name: {name}\n"
            f"Phone: {phone}\n"
            f"From: {from_location}\n"
            f"To: {to_location}\n"
            f"Trip Date: {trip_date}\n"
            f"Trip Type: {trip_type}\n"
            f"Return Date: {return_date}"
        )
        recipient_list = ['aastha2212chaurasia@gmail.com']

        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
            messages.success(request, 'Email sent, we will contact you shortly.')
        except Exception as e:
            messages.error(request, 'Failed to send email. Please try again later.')

        return redirect('home')

    return render(request, 'book_trains.html')

def booking_confirmation(request):
    return render(request, 'booking_confirmation.html')

def create_account(request):
    return render(request, 'create_account.html')

def login_view(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        birthdate = request.POST['birthdate']
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username, password=password)
        user.first_name = full_name
        user.save()

        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login')
    else:
        return render(request, 'create_account.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('')
    else:
        return render(request, 'home.html')
