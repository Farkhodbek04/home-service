from django.shortcuts import render
from .models import Services, Clients, Contact

def main(request):
    services = Services.objects.all()
    clients = Clients.objects.all()
    contact = Contact.objects.all()

    context = {
        'services': services,
        'clients': clients,
        'contact' : contact
    }

    return render(request, "index.html", context)

# Create your views here.
