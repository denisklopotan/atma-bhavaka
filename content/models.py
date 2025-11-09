from django.db import models
from ckeditor.fields import RichTextField

class PageContent(models.Model):
    """Model for editable page content sections"""
    
    PAGE_CHOICES = [
        ('home', 'Home'),
        ('about', 'About'),
        ('learn', 'Learn'),
        ('book', 'Book'),
    ]
    
    page = models.CharField(max_length=50, choices=PAGE_CHOICES)
    section_key = models.CharField(max_length=100, help_text="Unique identifier for this content section")
    title = models.CharField(max_length=200, blank=True)
    content = RichTextField(help_text="Main content text")
    order = models.IntegerField(default=0, help_text="Display order on the page")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['page', 'order']
        unique_together = ['page', 'section_key']
        verbose_name = "Page Content"
        verbose_name_plural = "Page Contents"
    
    def __str__(self):
        return f"{self.get_page_display()} - {self.section_key}"


class ContactInfo(models.Model):
    """Model for contact information"""
    
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    instagram_handle = models.CharField(max_length=100)
    facebook_name = models.CharField(max_length=100)
    facebook_url = models.URLField()
    instagram_url = models.URLField()
    
    workshop_address_line1 = models.CharField(max_length=200)
    workshop_address_line2 = models.CharField(max_length=200)
    
    company_name = models.CharField(max_length=200)
    company_address_line1 = models.CharField(max_length=200)
    company_address_line2 = models.CharField(max_length=200)
    company_kvk = models.CharField(max_length=50, verbose_name="KVK Number")
    
    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"
    
    def __str__(self):
        return "Contact Information"
    
    def save(self, *args, **kwargs):
        if not self.pk and ContactInfo.objects.exists():
            raise ValueError("Only one ContactInfo instance is allowed")
        return super().save(*args, **kwargs)


class PackagePrice(models.Model):
    """Model for package pricing"""
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = RichTextField()
    details = RichTextField(blank=True)
    payment_url = models.URLField(blank=True)
    qr_code_image = models.CharField(max_length=200, help_text="Filename of QR code image in static/media/")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Package Price"
        verbose_name_plural = "Package Prices"
    
    def __str__(self):
        return f"{self.name} - €{self.price}"
