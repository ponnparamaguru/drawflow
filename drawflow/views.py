from django.shortcuts import render, redirect
from .forms import NodeForm
from .models import Node, Flow
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import FlowSerializer
import json

def create_node(request):
    if request.method == 'POST':
        form = NodeForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            return redirect('drawflow')  # Redirect to the appropriate page
    else:
        form = NodeForm()
    return render(request, 'create_node.html', {'form': form})

def drawflow_view(request):
    nodes = Node.objects.all()
    return render(request, 'drawflow.html', {'nodes': nodes})

def get_nodes(request):
    nodes = Node.objects.all()
    data = list(nodes.values('id', 'name', 'image', 'no_of_inputs', 'no_of_outputs'))
    return JsonResponse(data, safe=False)

@api_view(['POST'])
def save_flow(request):
    serializer = FlowSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Flow saved successfully.'}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_flow(request, flow_id):
    try:
        flow = Flow.objects.get(id=flow_id)
    except Flow.DoesNotExist:
        return Response({'error': 'Flow not found.'}, status=404)

    serializer = FlowSerializer(flow, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Flow updated successfully.'}, status=200)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_flow(request, flow_id):
    try:
        flow = Flow.objects.get(id=flow_id)
        flow.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)  # Ensure an empty JSON response for successful deletion
    except Flow.DoesNotExist:
        return Response({'error': 'Flow not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def load_flow(request):
    flow_id = request.query_params.get('id')
    if flow_id:
        try:
            flow = Flow.objects.get(id=flow_id)
            serializer = FlowSerializer(flow)
            return Response(serializer.data)
        except Flow.DoesNotExist:
            return Response({'error': 'Flow not found.'}, status=404)
    return Response({'error': 'ID parameter missing.'}, status=400)

@api_view(['GET'])
def list_flows(request):
    flows = Flow.objects.all()
    serializer = FlowSerializer(flows, many=True)
    return Response(serializer.data)
