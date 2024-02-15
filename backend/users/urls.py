from django.urls import path
from .views import current_user, UserList, upload_picture

urlpatterns = [
    path('current_user/', current_user),
    path('upload_picture/', upload_picture),
    path('', UserList.as_view()),
]