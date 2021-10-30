from django.shortcuts import render
from .forms import SigninForm
# Create your views here.
def index(request):

	new_form = SigninForm()

	return render(request, 'app/index.html', dict(form=new_form))


