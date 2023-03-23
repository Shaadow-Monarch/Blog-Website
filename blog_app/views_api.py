
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Blog_model,Profile_model
from .helpers import *
from django.contrib.auth import authenticate, login


class Login_api_view(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')

            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')

            check_user = User.objects.filter(
                username=data.get('username')).first()

            if check_user is None: 
                response['message'] = 'invalid username , user not found'
                raise Exception('invalid username not found')
            
            print(check_user)
            if not Profile_model.objects.filter(user=check_user).first().is_varified:
                response['message'] = 'your profile is not verified'
                raise Exception('profile not verified')

            # before loginn is_varified hass to be true
            user_obj = authenticate(username=data.get('username'),
                                    password=data.get('password'))
            if user_obj:
                login(request, user_obj) #to login into system
                response['status'] = 200 
                response['message'] = 'Welcome'
            else:
                response['message'] = 'invalid password'
                raise Exception('invalid password')


        except Exception as e:
            print(e)

        return Response(response)


Login_api_view = Login_api_view.as_view()

from .helpers import *

class Register_api_view(APIView):

    def post(self, request):
        response = {'status': 500, 'message': 'Something went wrong'}
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')

            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')
            
            check_user = User.objects.filter(
                username=data.get('username')).first()
            
            if check_user:
                response['message'] = 'username  already taken'
                raise Exception('username  already taken')

            user_obj = User.objects.create(email=data.get('username'),
                                           username=data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            token = generating_random_string(20)
            # # set verified user
            Profile_model.objects.create(user=user_obj, token=token)
            
            send_mail_to_user(token , data.get('username'))

            response['message'] = 'User created '
            response['status'] = 200
        except Exception as e:
            print(e)

        return Response(response)


Register_api_view = Register_api_view.as_view()
















