from django.shortcuts import render

# Create your views here.

# Featured journal entries for homepage (id, title, icon)
FEATURED_JOURNAL_IDS = [
    (1, "book-open"),   # My Journey into Competitive Programming
    (3, "dumbbell"),    # Balancing Sports and Academics
    (5, "briefcase"),   # Prepare for Day 1
]


def index(request):
    featured_entries = [
        {"id": eid, "title": JOURNAL_ENTRIES[eid]["title"], "icon": icon}
        for eid, icon in FEATURED_JOURNAL_IDS
        if eid in JOURNAL_ENTRIES
    ]
    return render(
        request,
        "cvsite/index.html",
        {"featured_entries": featured_entries},
    )

def about(request):
    return render(request, "cvsite/about.html")

# Hardcoded portfolio projects, grouped by year (newest first)
PROJECTS_BY_YEAR = {
    2026: [
        {
            "title": "Hough Transform - Parallel Implementation",
            "description": (
                "Parallel implementation of the Hough transform for line and circle detection in images. Offers "
                "two implementations: multi-threaded (C++11 threads) for shared-memory systems and MPI-based "
                "for distributed clusters. Both preprocessing (grayscale conversion, Canny edge detection) and "
                "the Hough transform itself are parallelized. Achieves 5–7× speedup on 8 cores (threaded) and "
                "3–4× speedup on 4 nodes (MPI). Built with C++17, OpenCV, and CMake. Generates edge maps, "
                "annotated results, and performance metrics."
            ),
            "tech_stack": ["C++17", "OpenCV", "CMake", "MPI", "Multithreading", "OpenMP"],
            "category": "systems",
            "github_url": "https://github.com/Nanu25/HoughTransform",
            "live_url": None,
            "featured": False,
        },
        {
            "title": "Recipe Organizer (Culina)",
            "description": (
                "Mobile app for cooking enthusiasts to manage and organize recipes. Add recipes with ingredients "
                "and steps, track nutritional info (protein, carbs, fat) with automatic calorie calculation. "
                "Search by name/ingredients/steps, filter by nutritional range, and mark favorites. Built with "
                "Jetpack Compose (Material 3) for a modern UI; legacy XML views also in the codebase. Uses Room "
                "for local storage and offline access, with cloud sync for backup and cross-device use."
            ),
            "tech_stack": ["Kotlin", "Jetpack Compose", "Material 3", "Room", "Android", "XML"],
            "category": "mobile",
            "github_url": "https://github.com/Nanu25/Culina",
            "live_url": None,
            "featured": False,
        },
    ],
    2025: [
        {
            "title": "Event Ticket Platform",
            "description": (
                "RESTful API backend for an event ticketing system. Organizers create events and ticket types; "
                "attendees purchase tickets and receive QR codes; staff validate tickets at entry. Built with "
                "Spring Boot 3.5 / Java 21, PostgreSQL (Neon DB), JWT auth, Flyway migrations. Features multi-role "
                "access (Organizer, Staff, Attendee), QR code generation (ZXing), PDF ticket downloads (iText), "
                "analytics, and layered architecture. Frontend built with Next.js 15, TypeScript, Tailwind. "
                "I worked mainly on the backend."
            ),
            "tech_stack": ["Spring Boot", "Java 21", "PostgreSQL", "JWT", "Flyway", "MapStruct", "Next.js", "TypeScript"],
            "category": "fullstack",
            "github_url": "https://github.com/alextm0/event-ticket-platform-backend",
            "live_url": None,
            "featured": False,
        },
        {
            "title": "Gym Journal",
            "description": (
                "A full-stack workout intelligence platform with custom session analytics, interactive progress "
                "charting, and an integrated Gemini API assistant delivering tailored training insights."
            ),
            "tech_stack": ["React", "Node.js", "Express", "PostgreSQL", "Gemini API"],
            "category": "fullstack",
            "github_url": "https://github.com/Nanu25/GymJournal/tree/Heroku",
            "live_url": "https://gym-journal-eta.vercel.app/login",
            "featured": True,
        },
        {
            "title": "Toy Language Interpreter",
            "description": (
                "A complete programming language interpreter with lexer, parser, and execution engine. "
                "Supports variables, conditionals, loops, functions, and concurrent execution with "
                "thread synchronization. Includes a type system and garbage collection."
            ),
            "tech_stack": ["Java", "OOP", "Design Patterns", "Multithreading"],
            "category": "systems",
            "github_url": "https://github.com/Nanu25/ToyLanguage",
            "live_url": None,
            "featured": False,
        },

    ],
    2024: [

        {
            "title": "Habit Tracker",
            "description": (
                "A habit tracking application that helps users build and maintain healthy routines. "
                "Features include habit creation, progress tracking with visual statistics, streak counting, "
                "and a clean, intuitive dashboard. Built as my CS50 final project."
            ),
            "tech_stack": ["Django", "Python", "SQLite", "HTML/CSS", "JavaScript"],
            "category": "web",
            "github_url": "https://github.com/Nanu25/Habits",
            "live_url": None,
            "featured": False,
        },
        {
            "title": "Our Social Network",
            "description": (
                "A Twitter-like social network built with Django. Users can create posts, follow and unfollow others, "
                "like posts, edit their own content, and view personalized feeds. Features pagination, user profiles, "
                "and a clean, responsive interface. My first deployed web application—hosted on Heroku—and an early "
                "step into full-stack web development."
            ),
            "tech_stack": ["Django", "Python", "SQLite", "HTML", "CSS", "JavaScript"],
            "category": "web",
            "github_url": "https://github.com/Nanu25/Our-Social-Network",
            "live_url": None,
            "featured": False,
        },
        {
            "title": "Connect Four AI",
            "description": (
                "An intelligent Connect Four game with an unbeatable AI opponent. Implements Minimax "
                "algorithm with Alpha-Beta pruning for optimal move selection. Features adjustable "
                "difficulty levels and a polished graphical interface."
            ),
            "tech_stack": ["Python", "Pygame", "Minimax", "Alpha-Beta Pruning"],
            "category": "ai",
            "github_url": "https://github.com/Nanu25/Connect-Four",
            "live_url": None,
            "featured": False,
        },
    ],
}

# Portfolio stats for hero section
PORTFOLIO_STATS = {
    "total_projects": sum(len(projects) for projects in PROJECTS_BY_YEAR.values()),
    "years_coding": 4,
    "technologies": 20,
}


def portfolio(request):
    # Years descending (newest first) for template
    years = sorted(PROJECTS_BY_YEAR.keys(), reverse=True)
    portfolio_years = [(y, PROJECTS_BY_YEAR[y]) for y in years]
    return render(
        request,
        "cvsite/portfolio.html",
        {
            "portfolio_years": portfolio_years,
            "stats": PORTFOLIO_STATS,
        },
    )

# Hardcoded journal entries
JOURNAL_ENTRIES = {
    1: {
        "title": "My Journey into Competitive Programming",
        "content": (
            "It all started when I was in high school, in the 9th grade, when I came across a video on YouTube about competitive programming. "
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
            "Now, I look forward to the future and the endless opportunities it holds.\n\n"
        ),
        "date": "February 1, 2025"
    },
    2: {
        "title": "Lessons Learned from Algorithmic Contests",
        "content": "Through multiple contests, I improved my problem-solving skills...",
        "date": "February 5, 2025"
    },
    3: {
        "title": "Balancing Sports and Academics",
        "content": (
            "Since I was in primary school, I’ve been passionate about sports. I started playing handball in the first grade, encouraged by my parents. They don’t play sports themselves, but they wanted me to stay active and pursue something I could enjoy. That’s how my journey with handball began, and it quickly became a big part of my life.\n\n"
            "In school, I’ve worked hard to balance academics with sports. I was a good student and, at the same time, a dedicated handball player. I took pride in excelling at both, even when it wasn’t easy. When I reached high school, I discovered a new interest: computer science. I started learning to code and 'tackling' algorithmic problems, which opened up a whole new world for me. But I never let go of sports. Handball remained a constant, and I found a rhythm that allowed me to grow in both areas. My studies and my athletic pursuits have shaped me in different ways, teaching me discipline, focus, and how to manage my time. Looking back, I’m proud of how I’ve kept these two passions alive, and I hope to continue balancing them as I move forward."
        ),
        "date": "February 10, 2025"
    },
    4: {
        "title": "Why I Love Teaching Competitive Programming",
        "content": "Helping others understand complex algorithms gives me great satisfaction...",
        "date": "February 15, 2025"
    },
    5: {
        "title": "Prepare for Day 1",
        "content": (
            "Prepare for 'Day One'\n"
            "True success isn't measured by how others are doing — it's measured by the distance between who you were and who you’ve become.\n\n"
            "Here it is — my first day as a Software Development Engineer.\n"
            "Since high school, I’ve dreamed of succeeding in the Olympiad in Informatics, getting into the best university in Romania, and landing a job at a big company during college. I did it.\n"
            "Thanks to God, I achieved all of these things — and most importantly, I didn’t lose my soul in the process. I’ve always tried to help others and be a good person along the way.\n\n"
            "But what was the cost?\n"
            "I’ve worked like hell these past years. In high school, I solved so many algorithmic problems that, by the time I had to prepare for university, I barely needed to learn anything new.\n"
            "In the last year, I can count on my fingers the number of nights I stayed up past midnight, and the mornings I woke up later than 8:30.\n"
            "During university, I also dedicated my time to teaching students informatics. I became a workaholic — when I wasn’t at university, I was probably learning something new. When I wasn’t learning, I was at the gym. And when I wasn’t at the gym, I was working my part-time job.\n\n"
            "Of course, I also need breaks — to spend quality time with my girlfriend and family, hang out with friends, or just relax and watch a movie.\n\n"
            "Over the past year, I’ve learned to calibrate things — to find balance between work and rest.\n"
            "Maybe that’s one of the most important lessons I’ve learned recently.\n"
            "Now, I try not to push myself more than 8 hours a day on hard tasks.\n"
            "In the morning, while preparing breakfast, I like to listen to podcasts — it helps me get focused for the day ahead.\n"
            "After a study or work session, I like going to the gym to unwind.\n"
            "All these small habits helped me reach this point.\n\n"
            "I know I can afford the luxury of doing these things. Many people don’t have the same opportunities — some have to do even more just to survive.\n"
            "That’s why I choose to stay humble, take a step back, and be thankful for everything I have.\n"
            "Every time I feel frustrated that I can’t do something, I remind myself that there are people who can only dream of having what I have. And that thought helps all the anger disappear.\n\n"
            "That’s a big difference between the 2025 version of me and the high school version.\n"
            "Now I realize I need to be wiser, more aware, more grateful for everything I have.\n\n"
            "So, here is my Day One.\n"
            "Not the high school version of me, who only believed in non-stop working and focusing on one subject.\n"
            "Not the primary school version of me, who just wanted to finish homework quickly to go have fun.\n"
            "This is a mature version of me — one who learned from past mistakes, one who knows how to live in a big city after growing up in a small one, one who can come home after 10 hours of work and still cook a healthy meal instead of ordering junk food, one who knows how to live alone, and also how to live with a partner.\n\n"
            "I can honestly say I’ve been preparing for this Day One for a long time.\n"
            "All the work, the people I’ve met, the books I’ve read, the experiences, the podcasts — everything brought me here.\n"
            "I’m very excited to do a great job in this internship, and I look forward to writing my impressions once it’s over."
        ),
        "date": "July 7, 2025"
    }
}

def journal_entry(request, entry_id):
    entry = JOURNAL_ENTRIES.get(entry_id)
    if not entry:
        return render(request, "cvsite/404.html")  # Handle not found
    return render(request, "cvsite/journal_entry.html", {"entry": entry})