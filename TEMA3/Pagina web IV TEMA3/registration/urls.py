"""
Backwards-compatible URLconf for existing django-registration
installs; this allows the standard ``include('registration.urls')`` to
continue working, but that usage is deprecated and will be removed for
django-registration 1.0. For new installs, use
``include('registration.backends.default.urls')``.

"""

import warnings

warnings.warn("include('registration.urls') is deprecated; use include('registration.backends.default.urls') instead.",
              DeprecationWarning)

from .backends.default.urls import *  # NOQA


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/$', views.RestauranteList.as_view(), name='rlist'),
    url(r'^add/$', views.add_restaurante, name='radd'),
]
