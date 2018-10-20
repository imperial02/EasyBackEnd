from django.conf.urls import url

from .views import index_page

urlpatterns = [
    url('^', index_page, name="index_page")
]
