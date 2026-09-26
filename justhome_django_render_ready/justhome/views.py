from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from .models import Property, ContactMessage, Newsletter
from .forms import (
    RegisterForm, LoginForm, PropertyForm,
    ContactForm, NewsletterForm, SearchForm
)


# ─── HOME ───────────────────────────────────────────────────────────────────
def home(request):
    featured_properties = Property.objects.filter(is_featured=True)[:6]
    all_properties = Property.objects.all()[:6]

    # Search
    search_query = request.GET.get('q', '')
    if search_query:
        all_properties = Property.objects.filter(
            Q(title__icontains=search_query) |
            Q(city__icontains=search_query) |
            Q(address__icontains=search_query)
        )

    # Newsletter form in footer
    newsletter_form = NewsletterForm()

    context = {
        'featured_properties': featured_properties,
        'properties': all_properties,
        'search_query': search_query,
        'newsletter_form': newsletter_form,
    }
    return render(request, 'justhome/home.html', context)


# ─── PROPERTIES ─────────────────────────────────────────────────────────────
def property_list(request):
    properties = Property.objects.all()
    form = SearchForm(request.GET)

    if form.is_valid():
        query = form.cleaned_data.get('query')
        listing_type = form.cleaned_data.get('listing_type')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        if query:
            properties = properties.filter(
                Q(title__icontains=query) |
                Q(city__icontains=query) |
                Q(address__icontains=query)
            )
        if listing_type:
            properties = properties.filter(listing_type=listing_type)
        if min_price:
            properties = properties.filter(price__gte=min_price)
        if max_price:
            properties = properties.filter(price__lte=max_price)

    return render(request, 'justhome/property_list.html', {
        'properties': properties,
        'form': form,
    })


def property_detail(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    similar = Property.objects.filter(
        city=property_obj.city
    ).exclude(pk=pk)[:3]
    return render(request, 'justhome/property_detail.html', {
        'property': property_obj,
        'similar': similar,
    })


@login_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            prop = form.save(commit=False)
            prop.owner = request.user
            prop.save()
            messages.success(request, 'Property listed successfully!')
            return redirect('property_detail', pk=prop.pk)
    else:
        form = PropertyForm()
    return render(request, 'justhome/add_property.html', {'form': form})


@login_required
def edit_property(request, pk):
    prop = get_object_or_404(Property, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=prop)
        if form.is_valid():
            form.save()
            messages.success(request, 'Property updated!')
            return redirect('property_detail', pk=prop.pk)
    else:
        form = PropertyForm(instance=prop)
    return render(request, 'justhome/add_property.html', {'form': form, 'edit': True})


@login_required
def delete_property(request, pk):
    prop = get_object_or_404(Property, pk=pk, owner=request.user)
    if request.method == 'POST':
        prop.delete()
        messages.success(request, 'Property deleted.')
        return redirect('my_properties')
    return render(request, 'justhome/confirm_delete.html', {'property': prop})


@login_required
def my_properties(request):
    properties = Property.objects.filter(owner=request.user)
    return render(request, 'justhome/my_properties.html', {'properties': properties})


# ─── AUTH ────────────────────────────────────────────────────────────────────
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.first_name}! Account created.')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'justhome/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                messages.success(request, f'Welcome back, {user.first_name or user.username}!')
                return redirect(request.GET.get('next', 'home'))
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'justhome/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


# ─── CONTACT ─────────────────────────────────────────────────────────────────
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'justhome/contact.html', {'form': form})


# ─── NEWSLETTER ──────────────────────────────────────────────────────────────
def newsletter_subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Newsletter.objects.filter(email=email).exists():
                msg = 'You are already subscribed!'
            else:
                form.save()
                msg = 'Successfully subscribed to newsletter!'
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': msg})
            messages.success(request, msg)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Invalid email.'})
            messages.error(request, 'Invalid email address.')
    return redirect(request.META.get('HTTP_REFERER', 'home'))


# ─── PROFILE ─────────────────────────────────────────────────────────────────
@login_required
def profile_view(request):
    properties = Property.objects.filter(owner=request.user)
    return render(request, 'justhome/profile.html', {
        'properties': properties,
    })
