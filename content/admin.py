from django.contrib import admin
from .models import PageContent, ContactInfo, PackagePrice


@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ['page', 'section_key', 'title', 'order', 'is_active']
    list_filter = ['page', 'is_active']
    search_fields = ['section_key', 'title', 'content']
    list_editable = ['order', 'is_active']
    ordering = ['page', 'order']
    
    class Media:
        css = {
            'all': ('admin/css/wide_editor.css',)
        }


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Contact Details', {
            'fields': ('phone', 'email')
        }),
        ('Social Media', {
            'fields': ('instagram_handle', 'instagram_url', 'facebook_name', 'facebook_url')
        }),
        ('Workshop Address', {
            'fields': ('workshop_address_line1', 'workshop_address_line2')
        }),
        ('Company Information', {
            'fields': ('company_name', 'company_address_line1', 'company_address_line2', 'company_kvk')
        }),
    )
    
    def has_add_permission(self, request):
        return not ContactInfo.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(PackagePrice)
class PackagePriceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['name', 'description']
    ordering = ['order']
    fieldsets = (
        (None, {
            'fields': ('name', 'price', 'order', 'is_active')
        }),
        ('Content', {
            'fields': ('description', 'details')
        }),
        ('Payment', {
            'fields': ('payment_url', 'qr_code_image')
        }),
    )
    
    class Media:
        css = {
            'all': ('admin/css/wide_editor.css',)
        }
