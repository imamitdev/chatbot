from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)


@csrf_exempt  # For testing only, remove in production
def ChatView(request):
    if request.method == "POST":
        user_input = request.POST.get("message")
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(user_input)
        return JsonResponse({"response": response.text})
    return render(
        request, "index.html", {"csrf_token": request.META.get("CSRF_COOKIE")}
    )
