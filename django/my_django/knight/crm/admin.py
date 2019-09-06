from django.contrib import admin

from .models import Customer, ClassList, Campuses, CourseRecord, PaymentRecord
# Register your models here.

admin.site.register(Customer)
admin.site.register(ClassList)
admin.site.register(Campuses)
admin.site.register(CourseRecord)
admin.site.register(PaymentRecord)
