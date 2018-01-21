from .models import Dtag
from django.forms import ModelForm
from django.forms.widgets import HiddenInput

class DtagForm(ModelForm):
	class Meta:
		model = Dtag
		fields = ['loc_lon', 'loc_lat', 'first_name', 'last_name', 'notes', 'severity']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['loc_lat'].widget.attrs.update({'id': 'lat', 'readonly': True})
		self.fields['loc_lon'].widget.attrs.update({'id': 'lon', 'readonly': True})