from django.urls import path
from . import views

app_name = "food"
urlpatterns = [
    path("", views.index, name="index"),
    # path("", views.IndexListView.as_view(), name="index"),
    # path("details/<int:item_id>/", views.details, name="details"),
    path("details/<pk>/", views.FoodDetails.as_view(), name="details"),
    # path("add/", views.add, name="add"),
    path("add/", views.AddView.as_view(), name="add"),
    # path("delete/<int:item_id>/", views.delete, name="delete"),
    path("delete/<pk>/", views.DeleteItem.as_view(), name="delete"),
    # path("update/<int:item_id>/", views.update, name="update"),
    path("update/<pk>/", views.UpdateItem.as_view(), name="update"),
    path("range/", views.range_below_hundred, name="below_hundred")
]
