from django.urls import path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from sevenhabits.views import RolesViewSet, GoalsViewSet

schema_view = get_swagger_view(title='Seven Habits API')

router = routers.DefaultRouter()
router.register('roles',RolesViewSet)
router.register('goals',GoalsViewSet)

urlpatterns = [
    path('docs/',schema_view)
]
urlpatterns += router.urls
