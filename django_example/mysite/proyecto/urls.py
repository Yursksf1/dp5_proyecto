from django.urls import path
from proyecto import views
from django.views.generic import TemplateView


urlpatterns = [
    path("", views.index),
    path('pag1/', TemplateView.as_view(template_name="pagina_1.html")),
    path('pag2/', TemplateView.as_view(template_name="pagina_2.html")),
    path('pag3/', TemplateView.as_view(template_name="pagina_3.html")),
]
