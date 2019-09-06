from django.conf.urls import url, include
from . import shoppingViews, settlementViews
from .pay import PayView

urlpatterns = [
    url(r'^$', shoppingViews.ShoppingCarView.as_view()),
    url(r'settlement', settlementViews.SettlementViews.as_view()),
    url(r'^pay$', PayView.as_view()),

]
