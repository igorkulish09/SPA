from django.urls import path
from comments.views import comment_list, add_comment

urlpatterns = [
    path('', comment_list, name='comment_list'),
    path('add_comment/', add_comment, name='add_comment'),
    path('add_comment/<int:parent_id>/', add_comment, name='add_reply'),
]
