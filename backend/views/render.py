from django.shortcuts import render


def render_base_template(request, *args, **kwargs):
    return render(request, 'index.html', {})