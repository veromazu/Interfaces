from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomeView(TemplateView):
	template_name='index.html'
	
	#  Allows getting the context necessary to render the view
    #
    #  @date [13/08/2017]
    #
    #  @author [Veronica Mazutiel]
    #
    #  @returns Dict containing the form to login
    #
	
	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		#context['form'] = LoginForm()
		#context['baseURL'] = url.baseURL()
		#context['pagename'] = 'home'
		return context