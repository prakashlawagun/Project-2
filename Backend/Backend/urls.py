from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/',include('account.urls')),
    path('api/',include('menu.urls')),
    path('api/notification/',include('notification.urls')),
    path('api/',include('foodcart.urls')),
    path('api/',include('item_order.urls')),
    path('api/', include('subscription.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
