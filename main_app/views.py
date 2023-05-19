from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Restaurant, Tag
from .forms import OrderForm

restaurant = [
    {'name': 'McDonald''s', 'type': 'Fast Food', 'Review': 'Very good for the heart, very bad for the body.', 'Stars': 4},
    {'name': 'Wendy''s', 'type': 'Fast Food', 'Review': 'Very good for the heart, very bad for the body.', 'Stars': 5},
    {'name': 'Cheesecake Factory', 'type': 'Dine-in', 'Review': 'Better quality food. Service is bad', 'Stars': 3}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render (request, 'about.html')

def restaurants_index(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant/index.html', {
    'restaurants': restaurants
    })

def restaurants_details(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    id_list = restaurant.tags.all().values_list('id')
    tags_restaurant_doesnt_have = Tag.objects.exclude(id__in=id_list)
    order_form = OrderForm()
    return render(request, 'restaurant/detail.html', {
        'restaurant': restaurant, 'order_form': order_form, 'tags': tags_restaurant_doesnt_have,
    })

def add_order(request, restaurant_id):
  form = OrderForm(request.POST)
  if form.is_valid():
    new_order = form.save(commit=False)
    new_order.restaurant_id = restaurant_id
    new_order.save()
  return redirect('detail', restaurant_id=restaurant_id)

def assoc_tag(request, restaurant_id, tag_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Restaurant.objects.get(id=restaurant_id).tags.add(tag_id)
  return redirect('detail', restaurant_id=restaurant_id)

def unassoc_tag(request, restaurant_id, tag_id):
  # Note that you can pass a tag's id instead of the whole tag object
  Restaurant.objects.get(id=restaurant_id).tags.remove(tag_id)
  return redirect('detail', restaurant_id=restaurant_id)

class RestaurantCreate(CreateView):
    model = Restaurant
    fields = 'name', 'type', 'review', 'stars'
    success_url = '/restaurants'
    
class RestaurantUpdate(UpdateView):
    model = Restaurant
    fields = ['name', 'type', 'review', 'stars']

class RestaurantDelete(DeleteView):
    model = Restaurant
    success_url = '/restaurants'

class TagList(ListView):
    model = Tag

class TagDetail(DetailView):
  model = Tag

class TagCreate(CreateView):
  model = Tag
  fields = '__all__'

class TagUpdate(UpdateView):
  model = Tag
  fields = ['name', 'color']

class TagDelete(DeleteView):
  model = Tag
  success_url = '/toys'