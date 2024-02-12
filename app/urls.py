from django.urls import path
from . import views
from .views import SignupView, LoginView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Movie App API",
        default_version='v1',
        description="Movie App API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="<EMAIL>"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('list/', views.movie_list, name= 'MovieList'),
    path('list/<int:pk>/', views.movie_detail, name= 'MovieDetail'),
    path('stream/', views.stream_list, name= 'StreamList'),
    path('stream/<int:pk>/', views.stream_detail, name= 'StreamDetail'),
    path('signup/', SignupView.as_view(), name= 'Signup'),
    path('login/', LoginView.as_view(), name= 'Login'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
