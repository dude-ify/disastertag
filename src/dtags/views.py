from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from dtags.models import dtag

class Landing:
    def index(request):
        return render(request, 'dtags/index.html')

class Create:
    def index(request):
        if request.method == 'GET':
            return render(request, 'dtags/create.html')

        if request.method == 'POST':
            form = Dtag(request.POST)
            # Should do some validation here ...
            dtag = form.save()
            return HttpResponseRedirect(reverse('create'))


class Read:
    def index(request):
        all_patients = dtag.objects.order_by('servity', '-date_created')
        cxt = {"patients": all_patients}
        return render(request, 'dtags/read.html', cxt)

    def info(request, patient_id):
        patient = get_object_or_404(barcode_id=patient_id)
        cxt = {"patient": patient}
        return render(request, 'dtags/patient_info.html', cxt)

