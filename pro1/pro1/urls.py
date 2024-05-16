from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import token_refresh, token_obtain_pair, TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('app1.urls')),
    path('auth/', include('app2.urls'))
]
