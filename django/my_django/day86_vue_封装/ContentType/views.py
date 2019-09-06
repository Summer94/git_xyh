from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views import View
from .models import Food, Fruit, Coupon


class ContentView(View):
    def get(self, request):
        # 给商品添加优惠券
        # c = Fruit.objects.get(id=1)
        # Coupon.objects.create(title='100减10', content_obj=c)
        #
        # c = Food.objects.get(id=1)
        # Coupon.objects.create(title='200减30', content_obj=c)

        # 查看优惠券绑定的所有食物
        # c = Coupon.objects.get(id=1)
        # print(c.content_obj)
        # print(c.content_obj.title)

        # 查看该商品下的所有优惠券
        # c = Food.objects.get(id=1)
        # print(c.coupon.all())
        # c2 = Food.objects.values('title', 'coupon__title')
        # print(c2)

        return HttpResponse("11111")
