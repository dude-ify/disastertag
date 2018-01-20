#from seralizer import DtagSerializer
#from models import Dtag
from django.shortcuts import render
from django.views import generic

class IndexView(generic.DetailView):
    template_name = 'dtags/index.html'


class CreateView(generic.DetailView):
    #queryset = Dtag.objects.all()
    #serializer_class = DtagSerializer
    template_name = 'dtags/create.html'

    #def preform_create(self, seralizer):
    #    """Save the post data when creating a new Dtag"""
    #    seralizer.save()


class DetailsView(generic.DetailView):
    #queryset = Dtag.objects.all()
    #serializer_class = DtagSerializer
    template_name = 'dtags/details.html'