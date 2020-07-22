from django.shortcuts import render
from .models import Agent

def agents_list(request):
    agent_list = Agent.objects.all()
    template = 'agents/agents.html'
    context = {
        'agent_list': agent_list

    }
    return  render(request, template, context)