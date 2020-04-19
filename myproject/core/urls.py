from django.urls import path
# a ideia aqui seria caso tivessemos somente um index.html
# from myproject.core import index
# mas como temos varios metodos, podemos fazer como esta abaixo
from myproject.core import views as v


app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
]
