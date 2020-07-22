from django.shortcuts import render, redirect
from .models import ContactDetails
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


def send_email(request):
    contactdetails = ContactDetails.objects.last()
    template = 'contact/contact.html'
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['from_email']
            message = contact_form.cleaned_data['message']

            try:
                send_mail(subject, message, from_email, ['test@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header')
            return redirect('contact:success')
    else:
        contact_form = ContactForm()
    context = {
        'contact_form': contact_form,
        'contactdetails': contactdetails
    }
    return render(request, template, context)

def success(request):
    return HttpResponse('Message Sent Succesfully!')