from django.urls import path
from . import views
app_name = "page"
urlpatterns = [
    path("", views.Homepage.as_view(), name="home"),
    path("about/", views.AboutUs.as_view(), name="about"),
    path("about/the-people/", views.OurPeople.as_view(), name="people"),
    path("contact-us/", views.Contact.as_view(), name="contact"),
    path("service/dtt-academy/", views.DttAcademyView.as_view(), name="academy"),
    path("service/portfolio-management/", views.PorfolioManagement.as_view(), name="portfolio"),

]
