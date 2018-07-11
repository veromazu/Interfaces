from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf.urls.static import static
from .forms import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import logout

# Create your views here.
class IndexView(TemplateView):
	template_name='index.html'
	
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['pagename'] = 'index'
		return context

class LoginView(TemplateView):
	template_name='login.html'
	
	def get_context_data(self, **kwargs):
		context = super(LoginView, self).get_context_data(**kwargs)
		context['form'] = LoginForm()
		context['pagename'] = 'login'
		return context
	def post(self, request, *args, **kwargs):
		form = LoginForm(request.POST)	
		if form.is_valid():

			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(username=email,password=password)

			if user is not None :
				login(request,user)
				return HttpResponseRedirect('/home')
			else:
				form = LoginForm()	
				return render(request,'login.html',{'pagename':'login','message':'Usuario no registrado','form':form})
		return render(request,'login.html',{'form':form,'pagename':'login'})

class RegistroView(TemplateView):
	template_name='registro.html'
	
	def get_context_data(self, **kwargs):
		context = super(RegistroView, self).get_context_data(**kwargs)
		context['form'] = RegisterForm()
		#context['baseURL'] = url.baseURL()
		context['pagename'] = 'registro'
		return context

	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			form =  RegisterForm(request.POST)
			if form.is_valid():
				newUser = form.save(commit=False)
				newUser.username = request.POST['email']
				newUser.save()
				profile = UserProfile(tipo_usuario=request.POST['rol'],user=newUser)
				profile.save()
				context={}
				context['form'] = RegisterForm()
				context['pagename'] = 'registro'
				context['message'] = 'Registro exitoso'
				return render(request,'registro.html',context)
		return render(request,'registro.html',{'form':form,'pagename':'register'})

class HomeView(TemplateView):
	template_name='welcome.html'
	
	def get(self,  request, *args, **kwargs):
		user=request.user
		context = super(HomeView, self).get(request,**kwargs)
		context['pagename'] = 'home'
		context['user'] = user
		return context

class MenuView(TemplateView):
	template_name='menu.html'
	
	def get(self,  request, *args, **kwargs):
		user=request.user
		context = super(MenuView, self).get(request,**kwargs)
		context['pagename'] = 'menu'
		context['user'] = user
		return context

class FaqView(TemplateView):
	template_name='faq.html'
	
	def get(self,  request, *args, **kwargs):
		user=request.user
		context = super(FaqView, self).get(request,**kwargs)
		context['pagename'] = 'menu'
		context['user'] = user
		return context

def salir(request):
	logout(request)
	return HttpResponseRedirect('/')



class ReportView(TemplateView):
	template_name='report.html'
	
	def get(self,  request, *args, **kwargs):
		user=request.user
		context = super(ReportView, self).get(request,**kwargs)
		context['pagename'] = 'menu'
		context['user'] = user
		return context

class SearchView(TemplateView):
	template_name='busqueda.html'
	
	def get(self,  request, *args, **kwargs):
		user=request.user
		context = super(SearchView, self).get(request,**kwargs)
		context['pagename'] = 'menu'
		context['user'] = user
		return context