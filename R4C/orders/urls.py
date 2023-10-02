from django.urls import path

from orders.views import OrderCreationView


urlpatterns = [
    path('buy_robot/', OrderCreationView.as_view(), name='buy_robot')
]