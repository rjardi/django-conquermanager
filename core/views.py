
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView

from core.forms import ContactForm, LoginForm, UserRegisterForm
from core.models import Contact

from django.contrib.auth import authenticate, login, logout

from django.urls import reverse
from django.shortcuts import redirect


from django.core.mail import send_mail

from django.contrib.auth.models import User
from django.views.generic import TemplateView

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

class ContactFormView(FormView):
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        name=form.cleaned_data["name"]
        email=form.cleaned_data["email"]
        message=form.cleaned_data["message"]

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
        
        return super().form_valid(form)


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

def register_view(request):
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            user=User.objects.create_user(username, email, password2)

            if user:
                user.first_name=first_name
                user.last_name=last_name
                user.save()

            context={
                'msg':'Usuario creado correctamente'
            }  
            
            return render(request, "main/register.html", context)
        else:
            context = {
                'form': form,
            }
            return render(request, "main/register.html", context)

    else:
        form = UserRegisterForm()
        context = {
            'form': form
        }
        return render(request, "main/login.html", context)
    

class Prueba(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("Hello World")
    
class PruebaTemplateView(TemplateView):
    template_name="PruebaTemplateView.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='Este es el titulo'
        return context
    
class PruebaTemplateView2(PruebaTemplateView):
    template_name='PruebaTemplateView.html'