import re
from rest_framework import serializers

from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email']

    def validate_phone_number(self, value):
        if not re.match(r'^\+?\d{10,15}$', value):
            raise serializers.ValidationError("Phone number must be between 10 and 15 digits and may start with +")
        return value
    
    def validate_email(self, value):
        if Contact.objects.filter(email=value).exists():
            raise serializers.ValidationError("A contact with this email already exists")
        return value
