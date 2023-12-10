from django.urls import path
from .views import comment_list, add_comment, add_reply

urlpatterns = [
    path('', comment_list, name='comment_list'),
    path('add_comment/', add_comment, name='add_comment'),
    path('add_reply/<int:parent_comment_id>/', add_reply, name='add_reply'),
]
