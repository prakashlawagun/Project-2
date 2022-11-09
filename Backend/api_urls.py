from django.urls import path, include

urlpatterns = [
    path('user/', include('account.urls')),
    path('notification/', include('notification.urls')),
    path('cart/', include('foodcart.urls')),
    path('order/', include('item_order.urls')),
    path('subscription/', include('subscription.urls')),
    path('menu/', include('menu.urls')),
    path('contact/', include('contact.urls')),
]
