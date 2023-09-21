# phonebook/views.py

from rest_framework import generics
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_queryset(self):
        queryset = Contact.objects.all()
        name_starts_with = self.request.query_params.get('name_starts_with', None)
        if name_starts_with:
            queryset = queryset.filter(name__istartswith=name_starts_with)
        return queryset

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# from django.shortcuts import render, redirect
# from .models import Contact

# def index(request):
#     if 'q' in request.GET:
#         query = request.GET['q']
#         contacts = Contact.objects.filter(name__istartswith=query)
#     else:
#         contacts = Contact.objects.all()
    
#     return render(request, 'index.html', {'contacts': contacts})

# def add_contact(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         phone_number = request.POST['phone_number']
#         Contact.objects.create(name=name, phone_number=phone_number)
#         return redirect('/')
    
#     return render(request, 'add_contact.html')

# def edit_contact(request, contact_id):
#     contact = Contact.objects.get(id=contact_id)
    
#     if request.method == 'POST':
#         contact.name = request.POST['name']
#         contact.phone_number = request.POST['phone_number']
#         contact.save()
#         return redirect('/')
    
#     return render(request, 'edit_contact.html', {'contact': contact})

# def delete_contact(request, contact_id):
#     Contact.objects.get(id=contact_id).delete()
#     return redirect('/')

