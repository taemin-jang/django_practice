from django import forms
from .models import Question  #pybo.models와 똑같음


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question    # 사용할 모델
        fields = ['subject', 'content']     # QuestionForm에서 사용할 Question 속성