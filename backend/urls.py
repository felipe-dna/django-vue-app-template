from django.contrib import admin
from django.urls import path

from backend.views.render import render_base_template

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_base_template, name='base')
]
