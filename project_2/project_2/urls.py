from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from project_2_app.views import ChargerViewSet

router = DefaultRouter()
router.register('charger', ChargerViewSet, basename='charger')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls))
]
