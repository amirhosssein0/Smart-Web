from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('predict/', include('predict.urls', namespace='predict')),
    path('', include('pages.urls', namespace='pages'))
]
