from django.urls import path
from .views import SensorsList, MeasurementList, SensorDetail

urlpatterns = [
    path('sensors/', SensorsList.as_view(), name='sensor-list'),
    path('measurements/', MeasurementList.as_view(), name='Measurement-list'),
    path('sensors/<int:pk>', SensorDetail.as_view(), name='sensor-detail')
]
