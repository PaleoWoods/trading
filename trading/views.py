#!/usr/bin/env python
from django.shortcuts import render


def index(request):
	return render(request, "index.html")
