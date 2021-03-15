from django.shortcuts import render
from .forms import Image_Form

def index(request):
    if request.method == 'POST':             #if the user is trying to send data to db
        form = Image_Form(request.POST, request.FILES) #process the form with the 2 requests (name and image)
        if form.is_valid(): #if valid, ex if name and image TRUE
            form.save() # save
            rendered_form = form.instance #save the instance as the rendered form
            return render(request, 'index.html', {'form': form, 'rendered_form': rendered_form}) #render both the form and the instance, which the user has entered
    else:
        form = Image_Form
        return render(request, 'index.html', {'form' : form}) #else if no data, just render form
