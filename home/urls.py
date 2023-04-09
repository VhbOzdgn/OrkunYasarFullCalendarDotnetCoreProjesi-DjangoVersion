from django.urls import path
from django.views.generic import TemplateView

app_name = 'home'

urlpatterns = [
    path('', view=TemplateView.as_view(
        template_name = 'pages/index.html'
    ), name='index')
]