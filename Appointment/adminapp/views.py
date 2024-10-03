# views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm, BookingForm
from .models import ContactSubmission, Booking  # Import the Booking model

def appointmenthomepage(request):
    return render(request, 'adminapp/appointmenthomepage.html')

def Aboutpage(request):
    return render(request, 'adminapp/Aboutpage.html')

def contactpage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            ContactSubmission.objects.create(name=name, email=email, message=message)
            send_mail(
                f'Message from {name}',
                message,
                email,
                ['your_email@example.com'],
            )
            return redirect('appointmenthomepage')
    else:
        form = ContactForm()
    return render(request, 'adminapp/Contact.html', {'form': form})

def bookingpage(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            Booking.objects.create(name=name, email=email, date=date, time=time)
            return redirect('appointmenthomepage')
    else:
        form = BookingForm()
    return render(request, 'adminapp/bookingpage.html', {'form': form})