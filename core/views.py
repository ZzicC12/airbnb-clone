from django.shortcuts import render


def view_practice(request):
    return render(request, "rooms/home.html")
