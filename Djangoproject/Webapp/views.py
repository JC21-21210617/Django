from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template import loader

class SampleView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'Webapp/top.html')
top_page = SampleView.as_view()

def search_view(request):
        return render(request, 'Webapp/results.html')

