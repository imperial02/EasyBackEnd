from django.conf.urls import url, include
from rest_framework import routers
from restapi import views

router = routers.DefaultRouter()
router.register(r'users', views.SectionViewSet)
router.register(r'groups', views.ParkingViewSet)
router.register(r'groups', views.PlaceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]