from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'pages/home.html'
    
class AboutView(TemplateView):
    template_name = 'pages/aboutus.html'
    
class MapView(TemplateView):
    template_name = 'pages/map.html'
    
class GalleryView(TemplateView):
    template_name = 'pages/gallery.html'