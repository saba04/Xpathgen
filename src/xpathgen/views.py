# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView, CreateView


class XPathGenView(TemplateView, CreateView):

    template_name = 'xpathgen/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)

    def post(self, request, *args, **kwargs):
        request.POST['url']
        return render(request, template_name=self.template_name, context={})