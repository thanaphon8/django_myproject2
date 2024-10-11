from django.shortcuts import render

# Create your views here.


def indexPage(request):
    return render(request, 'index.html')


def aboutUs(request):
    return render(request, 'about.html')


def loginPage(request):
    return render(request, 'login.html')


def contactUs(request):
    return render(request, 'contact.html')


def forPage(request):
    context = {}
    lt = list(range(0, 100))
    context["list"] = lt
    return render(request, 'for_test.html', context)


def cardView(request):
    context = {}
    lt = list(range(0, 100))
    context["list"] = lt
    return render(request, 'card.html', context)


def cardColor(request):
    context = {
        'color': 'all',
    }

    if request.method == "GET":
        color = request.GET.get('color')
        if color is not None:
            context['color'] = color

    return render(request, 'card_color.html', context)


def forGGG(request):
    email = ''
    password = ''

    context = {}

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('my-password')

    context['email'] = email
    context['password'] = password

    return render(request, 'for_ggg.html', context)
