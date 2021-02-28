from django.contrib import admin

# Register your models here.
from .models import Grocery, Refrigerator, Category, Housekeeping_Book

admin.site.register(Grocery)
admin.site.register(Refrigerator)
admin.site.register(Category)
admin.site.register(Housekeeping_Book)
