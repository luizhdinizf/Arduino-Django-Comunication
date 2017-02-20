from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^atualiza/$', views.atualiza, name='atualiza'),
    url(r'^escreve/$', views.escreve, name='escreve'),
]
