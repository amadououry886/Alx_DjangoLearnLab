from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    user.userprofile.role == 'Admin'

@user_passes_test(is_admin, login_url="login")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")
