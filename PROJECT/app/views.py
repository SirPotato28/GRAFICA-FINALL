
from django.shortcuts import render
from .models import Score

def score_list(request):
    scores = Score.objects.all()
    total_students = scores.count()  # Agregamos la variable total_students
    context = {'scores': scores, 'total_students': total_students}
    return render(request, 'score_list.html', context)
