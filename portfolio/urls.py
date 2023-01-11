from django.urls import path

from portfolio.views import ResumeAPIView

urlpatterns = [
    path('', ResumeAPIView.as_view(), name='resume')
]