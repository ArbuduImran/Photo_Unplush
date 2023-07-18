from django.urls import path
from .views import PhotoSearchView

urlpatterns = [
    path('search/<str:keyword>/', PhotoSearchView.as_view()),
]
# from rest_framework.routers import DefaultRouter
#
# from image.views import PhotoSearchView
#
# router = DefaultRouter()
# router.register(r'search/<str:keyword>/', PhotoSearchView.as_view({'get': 'list'}), basename='search/<str:keyword>/')
#
#
# urlpatterns = router.urls