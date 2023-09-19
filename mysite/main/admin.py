from django.contrib import admin

from .models import Shops, Staff, Books, Orders


admin.site.register(Shops)
admin.site.register(Staff)
admin.site.register(Books)
admin.site.register(Orders)
