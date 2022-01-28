
from django.contrib import admin
from django.urls import path
from app.views import PlanListAPIView,GetPlan
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', PlanListAPIView.as_view()),
    path('todo/<int:pk>/', GetPlan.as_view()),
    # path('get-token/', obtain_auth_token),
    path('get-token/', TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),
    # path('todo_post/', PlanCreateAPIView.as_view()),
]
