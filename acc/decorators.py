from django.http import HttpResponse
from django.shortcuts import redirect

# these are the decorators that are seen as @ before functions, they decide the authentication groups and levels

def unauthenticated_user(view_func):

    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
             return redirect ('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

def allowed_users(allowed_roles=[]):

    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group =  request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('you are not authorised!')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group =  request.user.groups.all()[0].name
        if group == 'Employee':
            return redirect ('user')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func