from django.urls import path
from proyecto import views
from django.views.generic import TemplateView

app_name = "app"

urlpatterns = [
    path("", views.index, name="index"),
    path("players", views.players, name="players"),
    path("hola_mundo", views.hola_mundo_123, name="hola_mundo"),
    path('index', TemplateView.as_view(template_name="pagina_1.html"), name="pag1"),
    path('information', TemplateView.as_view(template_name="pagina_2.html"), name="pag2"),
    path('galery', TemplateView.as_view(template_name="pagina_3.html"), name="pag3"),
    path('new', TemplateView.as_view(template_name="pagina_4.html"), name="pag4"),
]

