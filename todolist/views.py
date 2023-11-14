from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from todolist.models import atasks, ftasks

def update(request):
	if (request.method == 'POST'):
		if (request.POST.get("form_type") == 'add'):
			ntask = request.POST['task']
			if (request.POST['pri'] == '1'):
				prio = 'High'
			elif (request.POST['pri'] == '2'):
				prio = 'Middle'
			elif (request.POST['pri'] == '3'):
				prio = 'Low'
			ndate = request.POST['date']

			newtask = atasks(task=ntask, pri=prio, date=ndate)
			newtask.save()

		elif (request.POST.get("form_type") == 'del'):
			idnum = request.POST['index']
			item = atasks.objects.get(id=int(idnum))
			fdate = request.POST['fdate']
			newitem = ftasks(task=item.task, pri=item.pri, date=fdate)
			newitem.save()
			item.delete()

		elif (request.POST.get("form_type") == 'rem'):
			idnum = request.POST['index']
			item = atasks.objects.get(id=int(idnum))
			item.delete()

	return render(request, 'index.html', {})


def display(request):
	aitems = atasks.objects.all().values()
	fitems = ftasks.objects.all().values()
	context = {
		'aitems': aitems,
		'fitems': fitems,
	}
	template = loader.get_template('landing.html')
	return HttpResponse(template.render(context, request))