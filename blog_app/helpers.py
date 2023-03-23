from django.utils.text import slugify

## generating string
import string
import random
def generating_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k=N))
    return str(res)


def generating_slug(text):
    new_slug = slugify(text) #slugify convert any text to url format text
    from .models import Blog_model

    if Blog_model.objects.filter(slug=new_slug).exists():
        return generating_slug(text+generating_random_string(4))

    return new_slug

from django.conf import settings
from django.core.mail import send_mail

def send_mail_to_user(token,email):
    subjects = "Your  account needs to be verified"
    message =  "hi paste this link to url to verify acount localhost:8000/verify/{}".format(token)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
     
    #inbuilt send mail function
    send_mail(subjects,message,email_from,recipient_list,fail_silently=False)
    return True