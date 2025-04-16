from django.shortcuts import render


def index(request):
    """
    Display the home page.
    :param request: The HTTP request
    :return: A rendered HTML page displaying the home page.
    """
    return render(request, 'index.html')
