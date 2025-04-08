from django.http import JsonResponse

def api_root(request):
    return JsonResponse({"message": "Welcome to the Octofit API!", "url": "https://miniature-yodel-69ww57rpjqjx35w99-8000.app.github.dev"})