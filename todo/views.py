from django.shortcuts import render, redirect
from .models import TodoList, TodoList_files, TodoList_images
from django.views import generic
from .forms import TodoCreateForm
from datetime import date


# Create your views here.


class IndexView(generic.ListView):
    context_object_name = 'to_do_list'

    def get_queryset(self):
        return TodoList.objects.all()


class DetailView(generic.DetailView):
    model = TodoList
    context_object_name = 'todolist'

    def get_queryset(self):
        return TodoList.objects.all()


class DeleteView(generic.DeleteView):
    model = TodoList
    success_url = '/'
    template_name = 'todo/delete.html'


class UpdateView(generic.UpdateView):
    model = TodoList
    fields = ['name', 'description', 'date_deadline']
    template_name = 'todo/update.html'
    success_url = "/"


def TodoCreate(request):
    if request.method == "POST":
        form = TodoCreateForm(request.POST)

        name = request.POST['name']
        description = request.POST['description']
        date_deadline = request.POST['date_deadline']
        images = request.FILES.getlist('images')
        files = request.FILES.getlist('files')
        date_created = date.today()

        t = TodoList.objects.create(
            name=name,
            description=description,
            date_created=date_created,
            date_deadline=date_deadline,
        )

        t.save()

        for image in images:
            TodoList_images.objects.create(todo=t, image=image)

        for file_in_list in files:
            TodoList_files.objects.create(todo=t, files=file_in_list)

        return redirect('/')

    else:
        form = TodoCreateForm()
        return render(request, 'todo/create.html', {'form': form})
