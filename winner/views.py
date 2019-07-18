from django.shortcuts import render
from django.http import HttpResponse
data = {}

def win_Mercedes(request):
    if request.method == 'GET':
        return render(request, 'winMercedes.html')
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        file = open('namenomer.txt', 'a')
        file.write(name + ' ' + number + ',')
        file.close()
        return render(request, 'thank you.html')

