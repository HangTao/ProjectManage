from django import forms
class FeasibilityEvalutionForm(forms.Form):
    is_feasibility = forms.BooleanField(label='是否可行')
    difficult = forms.IntegerField(label='难度评分')
    difficult_description = forms.CharField(label='评分原因',max_length=1000,widget=forms.Textarea)
