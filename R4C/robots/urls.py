from django.urls import path

from robots.views import RobotCreationView, ExcelReportView

urlpatterns = [
    path('create_robot/', RobotCreationView.as_view(), name='create_robot')
]