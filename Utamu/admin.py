from django.contrib import admin

from Utamu.models import Product

# Register your models here.
admin.site.site_header = "Utamu backend"


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "price"]

    list_per_page = 25


admin.site.register(Product, ProductAdmin)
