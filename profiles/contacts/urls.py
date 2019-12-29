from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/', views.create_contacts.as_view(), name='create_contacts'),
    url(r'^edit/', views.edit_contacts.as_view(), name='edit_contacts'),
    url(r'^delete/', views.delete_contacts.as_view(), name='delete_contacts'),
    # url(r'^login/', views.login, name='login'),
    url(r'^signup/', views.SignUp.as_view(), name='signup'),  # sign up
]
