from django.urls import path
from . import views
from .views import PagesListView, PageDetailView

urlpatterns = [
    path('', PagesListView.as_view(), name='pages'),
    #path('<int:page_id>/<slug:page_slug>/', PageDetailView.as_view(), name='page'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
]