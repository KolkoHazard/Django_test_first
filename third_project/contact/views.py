from django.shortcuts import render
from contact.models import Contact

# Create your views here.
def contact(request):
    contactlist = Contact.objects.order_by('last_name')
    contact_dict={'contact_records':contactlist}
    return render(request,'contact/contact.html',context= contact_dict)
