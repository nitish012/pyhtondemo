from django.conf.urls import url
from rest_framework import routers,DefaultRouter
from quickstart import views

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet,'students')

urlpatterns = router.urls
