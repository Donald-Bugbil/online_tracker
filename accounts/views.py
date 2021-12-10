from django.shortcuts import render
from django.views.generic import View



# Create your views here.

class VerifyPage(View):
    template = 'accounts/verification_sent.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template)

    


