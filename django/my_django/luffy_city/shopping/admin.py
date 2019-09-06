from django.contrib import admin

# Register your models here.
from .models import Coupon, CouponRecord

admin.site.register(CouponRecord)
admin.site.register(Coupon)
