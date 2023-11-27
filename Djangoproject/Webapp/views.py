from django.shortcuts import render
from django.views import View

class SampleView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'Webapp/top.html')
top_page = SampleView.as_view()
