from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . models import Page ,Books
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail,get_connection
from django.urls import reverse_lazy

class BooksView(ListView):
	model=Books
	template_name='pages/books.html'
	#success_url=reverse_lazy('books')
	def get_context_data(self, **kwargs):
	    context = super(BooksView, self).get_context_data(**kwargs)
	    context['books']=Books.objects.all()
	    return context





class HomeView(TemplateView):
	template_name='pages/home.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'



def contact(request):
	submitted=False
	if request.method=='POST':
		form=ContactForm(request.POST)
		
		if form.is_valid():
			cd=form.cleaned_data
			con = get_connection('django.core.mail.backends.console.EmailBackend')
			send_mail(
				cd['yoursubject'],
				cd['yourmessage'],
				cd.get('youremail', 'noreply@example.com'),
				['siteowner@example.com'],
				#data['yoursubject'],
				#data['yourmessage'],
				#data.get('email', 'noreply@example.com'),
				#['siteowner@example.com'],
				connection=con
				)
			return HttpResponseRedirect('/contact?submitted=True')
	else:
		form=ContactForm()
		if 'submitted' in request.GET:
			submitted=True

	context ={
		'form':form,
		'page_list':Page.objects.all(),
		"submitted":submitted,
	}

	return render(request, 'pages/contact.html',context)