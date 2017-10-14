from __future__ import unicode_literals

import json
from datetime import timedelta

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.utils.crypto import get_random_string
from django.conf import settings
from django.utils import timezone
from django.db.models import Q
from django.db import IntegrityError

from eveauth.tasks import get_server


@login_required
@user_passes_test(lambda x: x.groups.filter(name="admin").exists())
def registeredusers_index(request, page=1):
    users = User.objects.prefetch_related(
        "profile",
        "profile__character",
        "profile__corporation",
        "profile__alliance"
    ).order_by(
        "-last_login"
    ).all()
    paginator = Paginator(users, 25)

    context = {
        "users": paginator.page(page)
    }

    return render(request, "eveauth/registeredusers_index.html", context)



@login_required
@user_passes_test(lambda x: x.groups.filter(name="admin").exists())
def view_user(request, id):
    user = User.objects.get(id=id)

    context = {
        "user": user,
        "forum_address": settings.FORUM_ADDRESS
    }

    return render(request, "eveauth/user_view.html", context)



@login_required
@user_passes_test(lambda x: x.groups.filter(name="admin").exists())
def mumbleadmin_index(request):
    server = get_server()

    context = {
        "server": server,
        "users": map(lambda x: x[1], server.getUsers().items())
    }

    o = render(request, "eveauth/mumbleadmin_index.html", context)
    server.ice_getCommunicator().destroy()
    return o



@login_required
@user_passes_test(lambda x: x.groups.filter(name="admin").exists())
def mumbleadmin_kick(request, session_id):
    server = get_server()
    user = server.getUsers()[int(session_id)]
    server.kickUser(int(session_id), "Kicked via web admin")
    messages.success(request, 'Kicked %s from mumble' % user.name)

    server.ice_getCommunicator().destroy()
    return redirect(mumbleadmin_index)