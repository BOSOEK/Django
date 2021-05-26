from django.urls import path

from . import views

"""
config/urls에서 pybo/에 대한 처리를 한 상태라 pybo/를 제외하고 코드를 짠다.
"""

urlpatterns = [
    path('', views.index),  #
]