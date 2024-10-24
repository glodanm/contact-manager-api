from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Contact
from .serializers import ContactSerializer
from .utils import validate_region


class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        queryset = super().get_queryset()
        
        first_name = self.request.query_params.get('first_name', None)
        last_name = self.request.query_params.get('last_name', None)
        
        if first_name:
            queryset = queryset.filter(first_name__iexact=first_name)
        if last_name:
            queryset = queryset.filter(last_name__iexact=last_name) 
        
        return queryset

    def dispatch(self, *args, **kwargs):
        validate_region(self.request) 
        return super().dispatch(*args, **kwargs)


class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def dispatch(self, *args, **kwargs):
        validate_region(self.request)
        return super().dispatch(*args, **kwargs)
