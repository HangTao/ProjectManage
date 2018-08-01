from django.views.generic import FormView

from ProjectManage.PMForms.feasibility import FeasibilityEvalutionForm


class EvaluationView(FormView):
    template_name = 'ProjectManage/feasibility_evaluation.html'
    form_class = FeasibilityEvalutionForm
    success_url = '/thanks/'

    def form_valid(self, form):
        return super().form_valid(self)
