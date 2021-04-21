from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("clientes", views.ClienteViewSet)
router.register("telefones", views.TelefoneViewSet)
router.register("emails", views.EmailViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
