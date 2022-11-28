from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'app/index.html')


def about(request):
    return render(request, 'app/about.html', {'name': 'Митрофанов Даннил', 'growth': '175', 'weight': '60 кг', 'age': '16'})


def contacts(request):
    context = {'list_info': ['89083087915', 'mitrfan2006@mail.ru', 'https://t.me/pishy_kommentu']}
    return render(request, 'app/contacts.html', context)


def form(request):
    return render(request, 'app/form.html')