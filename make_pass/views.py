from django.shortcuts import render
import random


# Create your views here
def home(request):
	return render(request, 'make_pass/home.html', {'email':'fakemail@mail.com'} )

def password(request):
	chars = "abcdefghijklmnopqrstuvwxyz"
	length = int(request.GET.get('len'))
	if request.GET.get('uppercase'):
		chars = chars + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	if request.GET.get('numbers'):
		chars = chars + '0123456789'
	if request.GET.get('special'):
		chars = chars + '!@#$%^&*()_+='
	my_pass = ""
	for x in range(length):
		my_pass += random.choice(chars)
	return render(request, 'make_pass/pass.html', {'my_pass':my_pass})
