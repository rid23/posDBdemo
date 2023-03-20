from django.contrib import admin
from .models import Orders , Product , Customer , Categories , Employee

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Orders)
admin.site.register(Categories)
admin.site.register(Employee)