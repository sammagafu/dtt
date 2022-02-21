from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Blog

# Create your views here.

class Homepage(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog"] = Blog.objects.all().order_by('-published_date')[:3]
        return context
    

class AboutUs(TemplateView):
    template_name = "pages/about.html"

class Contact(TemplateView):
    template_name = "pages/contact.html"

class OurPeople(TemplateView):
    template_name = "pages/team.html"

class DttAcademyView(TemplateView):
    template_name = "pages/academy.html"

class PorfolioManagement(TemplateView):
    template_name = "pages/portfolio.html"