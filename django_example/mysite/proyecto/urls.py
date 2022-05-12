from django.urls import path
from proyecto import views
from django.views.generic import TemplateView

app_name = "app"

urlpatterns = [
    path("", views.index, name="index"),
    path('pag1/', TemplateView.as_view(template_name="pagina_1.html"), name="pag1"),
    path('pag2/', TemplateView.as_view(template_name="pagina_2.html"), name="pag2"),
    path('pag3/', TemplateView.as_view(template_name="pagina_3.html"), name="pag3"),
]
