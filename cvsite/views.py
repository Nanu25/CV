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
    "content": "It all started when I was in high school, in the 9th grade, when I came across a video on YouTube about competitive programming. "
               "I was fascinated by the idea of solving complex problems using algorithms and data structures. Determined to dive deeper, I started learning C++ and practicing on online platforms like Codeforces, Pbinfo, and Infoarena.\n\n"
               
               "I participated in my first contest in the 10th grade, but my performance was far from what I had hoped for. However, I didn’t let that discourage me. "
               "I kept practicing, studying advanced algorithms, and taking part in more contests. Slowly but surely, I started improving.\n\n"
               
               "By the 11th grade, my hard work paid off—I won my first contest. From that moment, competitive programming became more than just a challenge; it became my passion. "
               "I spent most of my free time solving problems, learning new techniques, and pushing my limits.\n\n"
               
               "During the 10th grade, I was fortunate to attend the Performance Center in Informatics in Ploiești, where I met an exceptional teacher and talented colleagues. "
               "This experience not only sharpened my problem-solving skills but also taught me how to work efficiently, manage my time effectively, and collaborate with others.\n\n"
               
               "All of this effort culminated in the 11th grade when I earned a bronze medal at the National Olympiad in Informatics. "
               "This achievement reinforced my belief that perseverance and dedication always pay off.\n\n"
               
               "In the first half of the 12th grade, I successfully scored a perfect 10 in the admission contest for Babeș-Bolyai University in Cluj-Napoca—the top university in Romania for Computer Science. "
               "This accomplishment gave me the freedom to focus on personal development, helping others, and preparing for the Romanian Baccalaureate.\n\n"
               
               "Looking back, I’ve learned that success requires hard work, patience, and resilience. "
               "You must be open to new ideas, willing to learn from others, and, most importantly, passionate about what you do. "
               "It’s not just about reaching the destination—it’s about embracing the journey.\n\n"
               
               "Above all, you need to dream big and have fun along the way.\n\n"
               
               "I am deeply grateful to everyone who has supported me throughout this journey—my family, my teachers, my friends, and all the amazing people I’ve met along the way. "
               "Now, I look forward to the future and the endless opportunities it holds.\n\n",
    "date": "February 1, 2025"
    },
    2: {
        "title": "Lessons Learned from Algorithmic Contests",
        "content": "Through multiple contests, I improved my problem-solving skills...",
        "date": "February 5, 2025"
    },
    3: {
        "title": "Balancing Sports and Academics",
        "content": "Since I was in primary school, I’ve been passionate about sports. I started playing handball in the first grade, encouraged by my parents. They don’t play sports themselves, but they wanted me to stay active and pursue something I could enjoy. That’s how my journey with handball began, and it quickly became a big part of my life.\n\n"
                   "In school, I’ve worked hard to balance academics with sports. I was a strong student and, at the same time, a dedicated handball player. I took pride in excelling at both, even when it wasn’t easy. When I reached high school, I discovered a new interest: computer science. I started learning to code and tackling algorithmic problems, which opened up a whole new world for me. But I never let go of sports. Handball remained a constant, and I found a rhythm that allowed me to grow in both areas. My studies and my athletic pursuits have shaped me in different ways, teaching me discipline, focus, and how to manage my time. Looking back, I’m proud of how I’ve kept these two passions alive, and I hope to continue balancing them as I move forward.",
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
