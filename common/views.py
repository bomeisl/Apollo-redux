from django.shortcuts import redirect
from django.views.generic import TemplateView

from .models import Navbar, NavBarItem


class IndexView(TemplateView):
    template_name = 'index.html'
    navbar = None

    def __init__(self, **kwargs):
        # check if the core Navbar is defined already, create one if it doesn't
        super().__init__(**kwargs)
        try:
            self.navbar = Navbar.objects.get(page='home')
        except:
            self.navbar = Navbar(page='home')
            self.navbar.save()

    def get_context_data(self, **kwargs):
        links = NavBarItem.objects.filter(nav_bar__page='home')
        context = {
            'links': links
        }
        return context

    def snake_redirect(request):
        return redirect('http://www.lifeofanya.com/snakes/', permanent=True)


from django.shortcuts import render

# Create your views here.
