from django.shortcuts import render

def main_view(request):
    if not request.user.is_authenticated:
        return render(request, 'landing_page.html', {})
    return render(request, 'home.html', {})
