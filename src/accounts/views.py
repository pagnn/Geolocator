from django.contrib.auth.views import LogoutView as DefaultLogoutView,LoginView as DefaultLoginView
from django.shortcuts import render
from .forms import LoginForm
from analytics.signals import user_logged_in
# Create your views here.

class LoginView(DefaultLoginView):
	authentication_form=LoginForm
	def form_valid(self,form):
		done_=super(LoginView,self).form_valid(form)
		if self.request.user.is_authenticated():
			user_logged_in.send(self.request.user,request=self.request)
		return done_
class LogoutView(DefaultLogoutView):
	pass