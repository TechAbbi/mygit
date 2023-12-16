from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .form import ItemForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


# Create your views here.

def index(request):
    item_list = Item.objects.all()
    return render(request, "food/index.html", {"item_list": item_list})

    # return HttpResponse("Hello")


class IndexListView(ListView):
    model = Item
    template_name = "food/index.html"
    context_object_name = "item_list"


def details(request, item_id):
    item = Item.objects.get(pk=item_id)

    return render(request, "food/details.html", {"item": item})


class FoodDetails(DetailView):
    model = Item
    template_name = "food/details.html"


def add(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food:index")

    return render(request, "food/add.html", {"form": form})


class AddView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = "food/add.html"
    success_url = reverse_lazy("food:index")


def delete(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == "POST":
        item.delete()
        return redirect("food:index")
    return render(request, "food/delete.html", {"item": item})


class DeleteItem(DeleteView):
    model = Item
    template_name = "food/delete.html"
    success_url = reverse_lazy("food:index")


def update(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect("food:index")
    return render(request, "food/add.html", {"item": item, "form": form})


class UpdateItem(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = "food/add.html"
    success_url = reverse_lazy("food:index")
