from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import os

# from dotenv import load_dotenv
from google import genai

# load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        user_input = request.POST.get("message")
        for chunk in client.models.generate_content_stream(
            model="gemini-2.0-flash",
            contents=user_input,
        ):
            return JsonResponse({"response": chunk.text})
    return render(
        request, "index.html", {"csrf_token": request.META.get("CSRF_COOKIE")}
    )
