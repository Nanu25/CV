from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "cvsite/index.html")
def about(request):
    return render(request, "cvsite/about.html")

def portfolio(request):
    return render(request, "cvsite/portfolio.html")

def contact(request):
    return render(request, "cvsite/contact.html")

# Hardcoded journal entries
JOURNAL_ENTRIES = {
    1: {
        "title": "My Journey into Competitive Programming",
        "content": "I started competitive programming in high school...",
        "date": "February 1, 2025"
    },
    2: {
        "title": "Lessons Learned from Algorithmic Contests",
        "content": "Through multiple contests, I improved my problem-solving skills...",
        "date": "February 5, 2025"
    },
    3: {
        "title": "Balancing Sports and Academics",
        "content": "Being passionate about both sports and CS, I learned how to manage time effectively...",
        "date": "February 10, 2025"
    },
    4: {
        "title": "Why I Love Teaching Competitive Programming",
        "content": "Helping others understand complex algorithms gives me great satisfaction...",
        "date": "February 15, 2025"
    },
}

def journal_entry(request, entry_id):
    entry = JOURNAL_ENTRIES.get(entry_id)
    if not entry:
        return render(request, "cvsite/404.html")  # Handle not found
    return render(request, "cvsite/journal_entry.html", {"entry": entry})
