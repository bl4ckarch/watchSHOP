from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
def index(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        name = request.POST.get('full name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
    
        data = {
            'message': message,
            'name'   : name,
            'email'  : email,
            'subject': subject
        }
        message = '''
        new message:{}
        from:{}

        '''.format(data['message'],data['email'])
        send_mail(data['subject'],message,'',['gwanulagabob9@gmail.com'])
        HttpResponse("thanks for submitting your form, we'll be in touch")

    return render(request, 'pages/index.html',{})