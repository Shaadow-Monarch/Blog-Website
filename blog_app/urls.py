from django.urls import path
from . import views

urlpatterns = [
    path("",views.index_view,name="index"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("register/",views.register_view,name="register"),
    path("add_blog/",views.add_block_view,name="add_blog"),
    path("details/<slug>",views.show_detial_view,name='details'),
    path("edit/<slug>",views.edit_blog_view,name='edit'),
    path("delete/<id>",views.delete_blog_view,name='delete'),
    path("my_blogs",views.my_blog_view,name="my_blogs"),
    path("verify/<token>",views.verify_view,name='verify'),
    path("about/",views.about_view,name='about'),
    path("contact/",views.contact_view,name='contact'),
]

