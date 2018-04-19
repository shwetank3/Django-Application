from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_new/', views.new_analysis, name='new'),
    path('pending/', views.AnalysisListView.as_view(template_name="my_nbm/pending_list.html"), name='pending'),
    path('completed/', views.AnalysisListView.as_view(template_name="my_nbm/completed_list.html"), name='completed'),
    path('analysis/<uuid:pk>', views.AnalysisDetailView.as_view(), name='analysis-detail'),
    path('analysis/create/', views.AnalysisCreate.as_view(), name='analysis_create'),
    path('analysis/<int:pk>/update/', views.AnalysisUpdate.as_view(), name='analysis_update'),
    path('analysis/<int:pk>/delete/', views.AnalysisDelete.as_view(), name='analysis_delete'),
]

