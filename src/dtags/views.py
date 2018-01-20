from django.http import Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from dtags.models import Dtag, DtagForm
from django.views.generic import DeleteView
#from django.core.exceptions import PermissionDenied

class Landing:
	def index(request):
		return render(request, 'dtags/index.html')

class Create:
	def index(request):
		if request.method == 'POST':
			form = DtagForm(request.POST)
			if form.is_valid():
				# Should do some validation here ...
				form.save()
				return HttpResponseRedirect(reverse('read'))
		else:
			form = DtagForm()
		return render(request, 'dtags/create.html', {'DtagForm': form})



class Read:
	def index(request):
		all_patients = Dtag.objects.order_by('severity', '-date_created')
		cxt = {"patients": all_patients}
		return render(request, 'dtags/read.html', cxt)

	def info(request, patient_id):
		patient = get_object_or_404(barcode_id=patient_id)
		cxt = {"patient": patient}
		return render(request, 'dtags/patient_info.html', cxt)


#class PermissionMixin(object):
#	def get_object(self, *args, **kwargs):
#		obj = super(PermissionMixin, self).get_object(*args, **kwargs)
#		if not obj.created_by == self.request.user:
#			raise PermissionDenied()
#		else:
#			return obj


class DtagDelete(DeleteView):
	model = Dtag
	success_url = reverse_lazy('read')

#	def get_success_url(self):
#		return reverse('read')
#
#	def delete(self, request, patient_id):
#		Dtag.objects.filter(pk=patient_id).delete()
#		return HttpResponseRedirect(reverse('read'))
