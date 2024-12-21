from django.urls import path
from .views import (
    ClassroomListView, SubjectListView, TestListView, StudentResultListView,
    LoginView, LogoutView
)

urlpatterns = [
    path('classrooms/', ClassroomListView.as_view(), name='classroom-list'),
    path('subjects/', SubjectListView.as_view(), name='subject-list'),
    path('tests/', TestListView.as_view(), name='test-list'),
    path('student-results/', StudentResultListView.as_view(), name='student-result-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
