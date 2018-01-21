from django.db import models
from django.forms import ModelForm
from django.forms.widgets import HiddenInput

class Dtag(models.Model):
	barcode_id = models.PositiveIntegerField(default=1, unique=True)
	first_name = models.CharField(max_length=225, blank=True)
	last_name = models.CharField(max_length=225, blank=True)
	notes = models.TextField(blank=True)
	loc_lat = models.FloatField(default=0, blank=False)
	loc_lon = models.FloatField(default=0, blank=False)
	image = models.ImageField(upload_to='media/', default='media/None/default.jpeg')
	SEVERITY_CHOICES = (
			('SR', 'Severe'),
			('MO', 'Moderate'),
			('MD', 'Mild'),
			)
	severity = models.CharField(
			max_length=2,
			choices=SEVERITY_CHOICES,
			default='SR',
			)

	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		"""Return a human readable rep of the model instance"""
		return "{}".format(self.first_name)

class DtagForm(ModelForm):
	class Meta:
		model = Dtag
		fields = ['barcode_id', 'loc_lon', 'loc_lat', 'first_name', 'last_name', 'notes', 'severity']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['loc_lat'].widget = HiddenInput()
		self.fields['loc_lat'].widget.attrs.update({'id': 'lat'})
		self.fields['loc_lon'].widget = HiddenInput()
		self.fields['loc_lon'].widget.attrs.update({'id': 'lon'})

