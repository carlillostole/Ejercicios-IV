# encoding: utf-8
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView



admin.autodiscover()


urlpatterns = [

    url(r'^$',
        TemplateView.as_view(template_name='index.html'),
        name='index'),

    url(r'^accounts/',
        include('registration.backends.default.urls')),


    url(r'^login/',
        auth_views.login,
        name='login'),

    url(r'^admin/',
        include(admin.site.urls),
        name='admin'),

    url(r'^perfil/',
        TemplateView.as_view(template_name='perfil.html'),
        name='perfil'),

    url(r'^principal/',
        TemplateView.as_view(template_name='principal.html'),
        name='pricnipal'),

    url(r'^restaurante/', include('registration.urls', namespace="restaurantes")),


    url(r'^contacto/',
        TemplateView.as_view(template_name='contacto.html'),
        name='contacto'),

    url(r'^mapa/',
        TemplateView.as_view(template_name='mapa.html'),
        name='mapa'),
]
