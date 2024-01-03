from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserSession
import openai

openai.api_key = "your_openai_api_key"

@csrf_exempt
def create_session(request, user_id):
    UserSession.objects.create(user_id=user_id)
    return JsonResponse({"message": f"Session created for user {user_id}"})

@csrf_exempt
def generate_response(request, user_id):
    try:
        session = UserSession.objects.get(user_id=user_id)
    except UserSession.DoesNotExist:
        return JsonResponse({"error": f"No session found for user {user_id}"}, status=400)

    prompt = request.POST.get("prompt", "")
    response = openai.Completion.create(
        engine=session.model,
        prompt=prompt,
        temperature=0.7,
        max_tokens=150
    )

    response_text = response.choices[0].text.strip()
    return JsonResponse({"response": response_text})
