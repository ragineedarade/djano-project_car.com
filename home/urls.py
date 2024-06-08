from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),

    path("index/contact/", views.contact, name='contact'),
    path("index/contact/index", views.index, name="home"),
    # path('contact/', views.contact_view, name='contact')
    path("contacts/", views.contact),

    # urls.py




]
