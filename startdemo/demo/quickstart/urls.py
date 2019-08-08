from django.conf.urls import url
from django.urls import path
# from rest_framework import routers
from quickstart import views

# router = routers.DefaultRouter()
# router.register(r'students', views.StudentViewSet)

# urlpatterns = [
#     path('', include(router.urls))
# ]


urlpatterns = [
    path('students/',views.StudentviewSet.as_view({'get':'list'})),
    path('student/<int:pk>/',views.StudentviewSet.as_view({'get':'retrieve'})),
    path('student/update/<int:pk>/',views.StudentviewSet.as_view({'post':'create'})),

    path('student/insert/',views.StudentInsert.as_view()),
    path('student/update/<int:pk>/',views.StudentList.as_view()),
    # path('student/',views.StudentviewSet.as_view({'get':'create'})),
]
