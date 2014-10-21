from django.shortcuts import render
from django.shortcuts import  render_to_response

# Create your views here.

def details_order(request):
    return render_to_response('product-details.html')

def list_order(request):
    return  render_to_response('product-details.html')