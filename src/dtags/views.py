from django.shortcuts import render

class Landing:
    def index(request):
        return render(request, 'dtags/index.html')

class Create:
    def index(request):
        return render(request, 'dtags/create.html')

class Read:
    def index(request):
        return render(request, 'dtags/read.html')

    def info(request, patient_id):
        cxt = {"patient_id": patient_id}
        return render(request, 'dtags/patient_info.html', cxt)

