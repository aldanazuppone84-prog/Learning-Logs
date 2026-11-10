from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    """the main page of learning notes"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """display all the topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """display a certain topic with all of the items below it"""
    topic = get_object_or_404(Topic, id = topic_id)
    # ensure the requested schame belongs to current user
    if topic.owner != request.user:raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries }
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """add new schame"""
    if request.method != 'POST':
        """unsubmit the date, create a new form"""
        form = TopicForm()
    else:
        """the date POST has submitted: deal with the date"""
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
        # display the blank form or point out that the form is invalid
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    # add the items under certain topic
    topic = get_object_or_404(Topic, id = topic_id)
    if topic.owner != request.user: # Make sure the topic belongs to the current user
        raise Http404
    if request.method != 'POST':
        # create a blank form when on date is submitted
        form = EntryForm()
    else:
        # deal with data when data is submitted
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    # display empty form or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    # edit the exiting items
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic
    if topic.owner != request.user: raise Http404
    if request.method != 'POST':
        # inital request, fill the form with the present itme
        form = EntryForm(instance=entry)
    else:
        # deal with the data when posting
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id = topic.id)
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)    