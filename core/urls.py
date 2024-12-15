from django.urls import path
from .views import SubjectListAPIView, TestListAPIView, SubmitTestAPIView

urlpatterns = [
    path('subjects/', SubjectListAPIView.as_view(), name='subject-list'),
    path('tests/<str:subject_id>/', TestListAPIView.as_view(), name='test-list'),
    path('submit-test/', SubmitTestAPIView.as_view(), name='submit-test'),
]
