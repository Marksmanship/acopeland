import re
from django.conf import settings # Importing settings so that we can reference the URLs that don't require a login
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse

# If a list by this name exists in settings...
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
	# Loop through it, and recreate this list in a variable located in this file
	EXEMPT_URLS = [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequriedMiddleware:
	# By default, __init__ is passed info identifying the Sender and instance of a created model.
	# Since this isn't a model, we will have to pass it a request to identify the Sender.
	# Here, we are overwriting the __init__() and defining a parameter to reference the aforementioned info passed by default
	# Then, we are setting the value for that default info to the parameter variable so that we have a reference to it.
	def __init__(self, get_response):
		self.get_response = get_response


	# __Call__ is used to redefine existing objects (objects already created by __init__()).
	# If you were to use __init__ instead, the system would create a new instance of an existing instance
	# __Init__() is used when the class is called to create an instance, __Call__() is used when an instance is called
	def __call__(self, request):
		response = self.get_response(request)
		return response

	def process_view(self, request, view_func, view_args, view_kwargs):
		assert hasattr(request, 'user')
		path = request.path_info.lstrip('/')

		# We must log the user out in the middleware because the if-conditions
		# below redirect the user based on their logged-in status. This may\
		# not sound like a problem, but remember, this middleware is called
		# right before the view is called, so the conditional checks below
		# are done before the view logs us out, unfortunately. We rectify
		# this by logging the user out in the middelware.
		# if path == 'account/logout/':
		if path == reverse('Accounts_Namespace:Accounts_Logout').lstrip('/'):	# Remove beginning '/' for pattern match below
			logout(request)		# Request contains the user object

		# Variable indicating whether the requested url is exempt from login requirement
		url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

		# If the user is already logged in, deny them access to a login/logout/register page by redirected them
		if request.user.is_authenticated and url_is_exempt:
			return redirect(settings.LOGIN_REDIRECT_URL) 	# Redirect a logged-in user

		# Normal behavior: User is visiting non-exempt page, or user is anon and visiting login
		if request.user.is_authenticated or url_is_exempt:
			return None		# Middleware doesn't have to do anything
		else:
			return redirect(settings.LOGIN_URL)
