from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token
)
from rest_framework_swagger.views import get_swagger_view
from .core.views import AccountViewSet

# drf
router = DefaultRouter()
router.register(r'accounts', AccountViewSet)

# swagger
schema_view = get_swagger_view(title='Worksheet API')

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),
    # drf
    path('api/', include(router.urls)),
    # token
    path('api/token/get/', obtain_jwt_token),
    path('api/token/update/', refresh_jwt_token),
    path('api/token/check/', verify_jwt_token),
    # api docs (swagger)
    path('api/docs/', schema_view),
]
