from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Homepage(TemplateView):
    template_name = "pages/index.html"

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