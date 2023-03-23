### this is for blogs 
from django.forms import ModelForm
from .models import Blog_model


#everthing i have set up in add_blog just taking care of content with django
class Blog_model_form(ModelForm):
    class Meta:
        model = Blog_model
        fields = ['content']

