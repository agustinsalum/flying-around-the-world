
from django.views.generic import TemplateView

class FlyIndexViews(TemplateView):
    template_name = 'index.html'

class FlyFormViews(TemplateView):
    template_name = 'form.html'

class FlyFlightsViews(TemplateView):
    template_name = 'flights.html'

class FlyAboutUsViews(TemplateView):
    template_name = 'about_us.html'