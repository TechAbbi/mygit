from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .form import ItemForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from rest_framework import viewsets
from .serializers import ItemSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    item_list = Item.objects.all().order_by("-item_price")

    search_query = request.GET.get("item_name")

    if search_query != "" and search_query is not None:
        item_list = item_list.filter(name__icontains=search_query).order_by("-item_price")

    paginator = Paginator(item_list, 2)
    page = request.GET.get("page")
    item_list = paginator.get_page(page)

    return render(request, "food/index.html", {"item_list": item_list})

    # return HttpResponse("Hello")


class IndexListView(ListView):
    model = Item
    template_name = "food/index.html"
    context_object_name = "item_list"
    paginate_by = 2

@login_required
def range_below_hundred(request):
    item_list = Item.objects.all().order_by("-item_price")

    item_below_100 = []
    item_value = []
    top_three_item =[]

    for item in item_list:
        if item.item_price < 100:
            item_below_100.append(item)

    for item in item_list:
        item_value.append(item.item_price)
        if item.item_price in item_value[:3]:
            top_three_item.append(item)


    return render(request, "food/range.html", {"item_list": item_below_100})


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


class ItemListViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


