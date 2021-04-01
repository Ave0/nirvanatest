from django.urls import path, include
from django.conf.urls import url

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from backend import views
from rest_framework.authtoken.views import obtain_auth_token
# Serializers define the API representation.

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'movies', views.MovieIMDBserViewSet)


# Wire up our API using automatic URL routing.
urlpatterns = [
    path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    url(r'^update$', views.UpdateView, name='UpdateView'),

]