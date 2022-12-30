from django.urls import path
from .views import MessageList, MessageDetail, MessageCreate , MessageDelete

urlpatterns = [
    path('', MessageList.as_view(), name='msg_list'),
    path('<int:pk>/', MessageDetail.as_view(), name='msg_views'),
    path('create/', MessageCreate.as_view(), name='msg_create'),
    path('<int:pk>/delete/', MessageDelete.as_view(), name='msg_delete')
]
