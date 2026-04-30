from django.contrib import admin
from .models import User
from certificates.models import Certificate


class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'total_certs', 'verified_certs')

    search_fields = ('username', 'email')

    def total_certs(self, obj):
        return Certificate.objects.filter(user=obj).count()

    def verified_certs(self, obj):
        return Certificate.objects.filter(user=obj, is_verified=True).count()


admin.site.register(User, UserAdmin)