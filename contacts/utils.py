import requests
import logging
from rest_framework.exceptions import PermissionDenied
from django.conf import settings

logger = logging.getLogger(__name__)

ALLOWED_COUNTRIES = ['UA', 'PL']

def get_client_ip(request):
    if settings.DEBUG:
        return '195.114.96.170'
        # return '8.8.8.8'

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    logger.info(f"Client IP: {ip}") 
    return ip

def get_client_country(ip):
    try:
        response = requests.get(f'http://ipinfo.io/{ip}/json')
        data = response.json()
        logger.info(f"Geolocation response for IP {ip}: {data}")
        return data.get('country')
    except requests.RequestException as e:
        logger.error(f"Error retrieving country for IP {ip}: {e}")
        return None

def validate_region(request):
    ip = get_client_ip(request)
    country = get_client_country(ip)

    if not country:
        raise PermissionDenied("Could not determine the country from the IP address.")

    if country not in ALLOWED_COUNTRIES:
        raise PermissionDenied(f"Access restricted to users from Ukraine and Poland. Your country: {country}")
