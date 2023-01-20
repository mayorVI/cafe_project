from django.shortcuts import render, redirect
from .models import DishCategory, Dish, Gallery
from .forms import UserReservationForm
import random


# Create your views here.


def main_page(request):
    if request.method == 'POST':
        form_reserve = UserReservationForm(request.POST)
        if form_reserve.is_valid():
            form_reserve.save()
            return redirect('/')

    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    special_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    gallery_photos = Gallery.objects.filter(is_visible=True)
    form_reserve = UserReservationForm()

    return render(request, 'main_page.html', context={'categories': categories,
                                                      'dishes': dishes,
                                                      'special': special_dishes,
                                                      'gallery_photos': gallery_photos,
                                                      'form_reserve': form_reserve,
                                                      })
