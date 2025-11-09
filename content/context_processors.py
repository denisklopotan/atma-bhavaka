from .models import ContactInfo

def contact_info(request):
    """Make contact info available in all templates"""
    contact = ContactInfo.objects.first()
    return {
        'contact_info': contact
    }
