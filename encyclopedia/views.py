from django.shortcuts import render, redirect
import markdown2
import random

from . import util


def index(request):
    """
    Display list of all encyclopedia entries with clickable links.
    """
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    """
    Display the content of an encyclopedia entry.
    If the entry doesn't exist, show an error page.
    """
    content = util.get_entry(title)
    
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "title": title,
            "message": f"The requested page '{title}' was not found."
        })
    
    # Convert Markdown to HTML
    html_content = markdown2.markdown(content)
    
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })


def search(request):
    """
    Search for encyclopedia entries.
    If exact match, redirect to that entry.
    Otherwise, display list of substring matches.
    """
    query = request.GET.get('q', '').strip()
    
    if not query:
        return redirect('index')
    
    # Get all entries
    entries = util.list_entries()
    
    # Check for exact match (case-insensitive)
    for entry in entries:
        if entry.lower() == query.lower():
            return redirect('entry', title=entry)
    
    # Find substring matches
    matches = [entry for entry in entries if query.lower() in entry.lower()]
    
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "matches": matches
    })


def new_page(request):
    """
    Create a new encyclopedia entry.
    """
    if request.method == "POST":
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '')
        
        if not title:
            return render(request, "encyclopedia/new.html", {
                "error": "Title cannot be empty."
            })
        
        # Check if entry already exists
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/new.html", {
                "error": f"An entry with the title '{title}' already exists.",
                "title": title,
                "content": content
            })
        
        # Save the new entry
        util.save_entry(title, content)
        
        # Redirect to the new entry's page
        return redirect('entry', title=title)
    
    # GET request - show the form
    return render(request, "encyclopedia/new.html")


def edit_page(request, title):
    """
    Edit an existing encyclopedia entry.
    """
    content = util.get_entry(title)
    
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "title": title,
            "message": f"The page '{title}' does not exist and cannot be edited."
        })
    
    if request.method == "POST":
        new_content = request.POST.get('content', '')
        
        # Save the updated entry
        util.save_entry(title, new_content)
        
        # Redirect to the entry's page
        return redirect('entry', title=title)
    
    # GET request - show the edit form
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })


def random_page(request):
    """
    Redirect to a random encyclopedia entry.
    """
    entries = util.list_entries()
    
    if not entries:
        return redirect('index')
    
    random_title = random.choice(entries)
    return redirect('entry', title=random_title)