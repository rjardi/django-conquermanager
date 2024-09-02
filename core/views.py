
from django.conf import settings
from django.shortcuts import render

from core.forms import ContactForm, LoginForm
from core.models import Contact

from django.contrib.auth import authenticate, login, logout

from django.urls import reverse
from django.shortcuts import redirect


from django.core.mail import send_mail

# Create your views here.
def contact_view(request):

    if request.POST:
        
        contact_form=ContactForm(request.POST)

        if contact_form.is_valid():

            name=contact_form.cleaned_data["name"]
            email=contact_form.cleaned_data["email"]
            message=contact_form.cleaned_data["message"]

            message_content=f"Se ha enviado correctamente de {name} con el correo {email} el mensaje: {message}"
            print(message_content)

            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )

            subject = 'Test Email'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['martagilserra@gmail.com']

            success=send_mail(subject, message, email_from, recipient_list, fail_silently=False)

            context={
                "contact_form": contact_form,
                'success': success
            }

            return render(request,'main/contact.html', context)

    
    contact_form=ContactForm()
    context={
        "contact_form": contact_form
    }

    return render(request,'main/contact.html', context)


def login_view(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
            else:
                context = {
                  'form': form,
                  'error': True,
                  'error_message': 'Usuario no válido' 
                }
                return render(request, "main/login.html", context)
        else:
            context = {
                'form': form,
                'error': True
            }
            return render(request, "main/login.html", context)
    else:
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, "main/login.html", context)
    
def logout_view(request):
    logout(request)
    return redirect(reverse('home'))