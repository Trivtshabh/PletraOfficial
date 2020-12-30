from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        #SENDING mail
        send_mail(subject, message, email, ['satadevlabsofficial@gmail.com'], fail_silently=False)
        return render(request, 'index.html',{'name':name})

    else:
        return render(request, 'index.html',{})

def services(request):
    return render(request, 'services.html',{})

def pp(request):
    return render(request, 'pp.html',{})

def tc(request):
    return render(request, 'tc.html',{})
