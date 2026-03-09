from django.shortcuts import render
from .forms import ChatForm
from .utils import get_ai_answer

def home(request):
    if request.method == "POST":
        form = ChatForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            question = instance.question

            answer = get_ai_answer(question)

            instance.answer = answer
            instance.save()

            return render(request, "result.html", {
                "question": question,
                "answer": answer
            })
    else:
        form = ChatForm()

    return render(request, "home.html", {"form": form})