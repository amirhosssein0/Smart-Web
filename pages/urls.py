from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('about-us/', AboutView.as_view(), name='aboutus'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('map/', MapView.as_view(), name='map'),
    path('', HomeView.as_view(), name='home')
]
