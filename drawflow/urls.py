from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_node, name='create_node'),
    path('', views.drawflow_view, name='drawflow'),
    path('api/nodes/', views.get_nodes, name='get_nodes'),
    path('api/save/', views.save_flow, name='save_flow'),
    path('api/update/<int:flow_id>/', views.update_flow, name='update_flow'),  # Existing endpoint for updating flows
    path('api/delete/<int:flow_id>/', views.delete_flow, name='delete_flow'),  # New endpoint for deleting flows
    path('api/load/', views.load_flow, name='load_flow'),
    path('api/list/', views.list_flows, name='list_flows'),
]
