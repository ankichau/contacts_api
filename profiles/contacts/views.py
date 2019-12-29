from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Contacts
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class create_contacts(generic.TemplateView):
    @login_required
    @require_http_methods(["POST", "GET"])
    def create(self, request):
        try:
            print(request.user.name, "===============")
            contact_data = request.data
            contacts = Contacts.object.create(**contact_data)
            contacts.save()
        except Exception as ex:
            print("Exception %s occurred while creating contacts " % ex)


class edit_contacts(generic.UpdateView):
    @login_required
    def edit(self, request):
        contact_data = request.data
        contact_id = contact_data.get('id')
        try:
            contact = Contacts.objects.get(id=contact_id)
        except Exception as ex:
            print("Exception %s occurred while editing contacts" % ex)
        contacts = Contacts.object.filter(id=contact_id).update(**contact_data)
        contacts.save()


class delete_contacts(generic.DeleteView):
    @login_required
    def delete(self, request):
        Contact_data = request.data
        Contact_id = Contact_data['id']
        try:
            contact = Contacts.objects.get(id=Contact_id)
        except Exception as ex:
            print("Exception %s occurred while editing contacts" % ex)
        contact.delete()
