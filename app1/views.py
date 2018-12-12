from django.shortcuts import render
from .models import My_Test_Model

# Create your views here.
def test_view(request):
    '''
    View function that displays a forms that allows users to add a city and rainfall
    '''
    new_value = My_Test_Model.objects.last()
    return render(request, 'test.html',{"new_value" : new_value})
