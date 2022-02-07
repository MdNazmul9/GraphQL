from django.contrib import admin
from .models import Company, Category, Product

admin.site.register([Company, Category, Product])