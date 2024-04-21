from django.views.generic import TemplateView 

# Create your views here.
#home page class based view
class HomePageView(TemplateView):
    template_name='home.html'

#About page class based view

class AboutPageView(TemplateView):
    template_name='about.html'

#Project page class based view

class ProjectPageView(TemplateView):
    template_name='project.html'


#About page class based view

class ContactPageView(TemplateView):
    template_name='contact.html'