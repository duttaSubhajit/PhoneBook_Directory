# phonebook/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.ContactList.as_view(), name='contact-list'),
    path('contacts/<int:pk>/', views.ContactDetail.as_view(), name='contact-detail'),
]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('add/', views.add_contact, name='add_contact'),
#     path('edit/<int:contact_id>/', views.edit_contact, name='edit_contact'),
#     path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
# ]
