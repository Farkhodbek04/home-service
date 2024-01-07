from django.contrib import admin
from .models import Services, Contact, Clients

class Show_Services(admin.ModelAdmin):
    list_display = ("title","icon", "body")
admin.site.register(Services, Show_Services)

class Show_Contact(admin.ModelAdmin):
    list_display = ("name", "phone", "email")
admin.site.register(Contact, Show_Contact)
class Show_Clients(admin.ModelAdmin):
    list_display = ("icon", "name", "opinion")
admin.site.register(Clients, Show_Clients)


