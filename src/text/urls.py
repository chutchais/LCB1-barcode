from django.contrib import admin
from django.urls import path


from .views import MessageDetailView

urlpatterns = [
	# path('', CaseListView.as_view(), name='list'),
    path('<slug:pk>', MessageDetailView.as_view(), name='detail'),
 #    path('step/<int:pk>', MessageDetailView.as_view(), name='step-detail'),
]
