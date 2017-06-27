import random

from django.views.generic import TemplateView
from .models import Product

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)

        ctx['products'] = random.sample(list(Product.objects.all()), 50)

        return ctx

