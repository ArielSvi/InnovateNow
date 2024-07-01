from django.contrib import admin
from .models import NavbarItem, Service, AboutUs, HelpedCompany

admin.site.register(NavbarItem)
admin.site.register(Service)
admin.site.register(HelpedCompany)

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    filter_horizontal = ('helped_companies',)
