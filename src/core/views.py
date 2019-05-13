from django.db.models import Q
from django.shortcuts import render

from .models import Journal, Category


def is_valid_queryparam(param):
    return param != '' and param is not None


def BootstrapFilterView(request):
    qs = Journal.objects.all()
    categories = Category.objects.all()

    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('id_exact')
    title_or_author_query = request.GET.get('title_or_author')
    view_count_min_query = request.GET.get('view_count_min')
    view_count_max_query = request.GET.get('view_count_max')
    date_min_query = request.GET.get('date_min')
    date_max_query = request.GET.get('date_max')
    category_query = request.GET.get('category')
    reviewed_query = request.GET.get('reviewed')
    not_reviewed_query = request.GET.get('notReviewed')

    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(title__icontains=title_contains_query)

    elif is_valid_queryparam(id_exact_query):
        qs = qs.filter(id=id_exact_query)

    elif is_valid_queryparam(title_or_author_query):
        qs = qs.filter( Q(title__icontains=title_or_author_query)
                        | Q(author__name__icontains=title_or_author_query)
                        ).distinct()

    if is_valid_queryparam(view_count_min_query):
        qs = qs.filter(views__gte=view_count_min_query)

    if is_valid_queryparam(view_count_max_query):
        qs = qs.filter(views__lt=view_count_max_query)

    if is_valid_queryparam(date_min_query):
        qs = qs.filter(publish_date__gte=date_min_query)

    if is_valid_queryparam(date_max_query):
        qs = qs.filter(publish_date__lt=date_max_query)

    if is_valid_queryparam(category_query) and category_query != 'Choose...':
        qs = qs.filter(categories__name=category_query)

    if reviewed_query == 'on':
        qs = qs.filter(reviewed=True)

    if not_reviewed_query == 'on':
        qs = qs.filter(reviewed=False)


    context = {
        'queryset': qs,
        'categories': categories,
    }
    return render(request, 'bootstrap_form.html', context)
