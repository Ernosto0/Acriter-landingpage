from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def landing_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Here you would typically save the email to your database
        # For now, we'll just add a success message
        messages.success(request, 'Thank you for your interest! We\'ll be in touch soon.')
        return HttpResponseRedirect(reverse('landing_page'))
    
    return render(request, 'funnel/landing.html')
