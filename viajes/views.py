
from django.views.generic import TemplateView

class ViajesIndexViews(TemplateView):
    template_name = 'index.html'

class ViajesFormViews(TemplateView):
    template_name = 'form.html'

class ViajesFlightsViews(TemplateView):
    template_name = 'flights.html'

class ViajesAboutUsViews(TemplateView):
    template_name = 'about_us.html'