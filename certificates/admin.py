from django.contrib import admin
from .models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'issuer',
        'category',
        'expiry_date',
        'is_verified',
        'user'
    )

    list_filter = (
        'category',
        'is_verified',
        'expiry_date'
    )

    search_fields = (
        'title',
        'issuer',
        'category'
    )

    list_editable = (
        'is_verified',
    )

    actions = ['mark_verified', 'mark_unverified']

    fieldsets = (
        ('Certificate Info',{
            'fields':(
                'user',
                'title',
                'issuer',
                'category',
                'issue_date',
                'expiry_date',
                'is_verified',
                'description',
                'certificate_file'
            )
        }),
    )

    def mark_verified(self, request, queryset):
        queryset.update(is_verified=True)

    mark_verified.short_description = "Verify selected certificates"


    def mark_unverified(self, request, queryset):
        queryset.update(is_verified=False)

    mark_unverified.short_description = "Unverify selected certificates"