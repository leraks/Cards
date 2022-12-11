from django.contrib import admin
from .models import *

class PurchaseAdmin(admin.ModelAdmin):
    readonly_fields = ('statuc',)

admin.site.register(Card)
admin.site.register(Purchase, PurchaseAdmin)