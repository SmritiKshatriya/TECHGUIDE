import os
import django

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techguide.settings')
django.setup()

from quiz.models import TechDomain, Question, Choice, Resource, UserResult

def populate():
    print("⚠️  Wiping old data...")
    UserResult.objects.all().delete()
    Resource.objects.all().delete()
    Choice.objects.all().delete()
    Question.objects.all().delete()
    TechDomain.objects.all().delete()

    print("🚀 Creating Career Paths...")
    # IDs must match the AI Target IDs: 1=Frontend, 2=Backend, 3=DS, 4=DevOps
    frontend = TechDomain.objects.create(id=1, name="Frontend Development", description="You build what users see. You love design and instant visual feedback.")
    backend = TechDomain.objects.create(id=2, name="Backend Development", description="You build the engine. You care about databases, servers, and logic.")
    ds = TechDomain.objects.create(id=3, name="Data Science", description="You find patterns in data. You love math, statistics, and predictions.")
    devops = TechDomain.objects.create(id=4, name="DevOps & Cloud", description="You keep the servers running. You love automation and infrastructure.")

    print("❓ Creating Smart Questions...")
    # Q1
    q1 = Question.objects.create(text="Do you prefer working on visual designs or logical problems?")
    Choice.objects.create(question=q1, text="Visual Designs (Colors, Layouts)", related_domain=frontend) # Visual=1
    Choice.objects.create(question=q1, text="Logical Problems (Algorithms, Data)", related_domain=backend) # Visual=0

    # Q2
    q2 = Question.objects.create(text="How do you feel about Mathematics and Statistics?")
    Choice.objects.create(question=q2, text="I love it! Give me the numbers.", related_domain=ds) # Math=1
    Choice.objects.create(question=q2, text="I prefer building things, not calculating.", related_domain=frontend) # Math=0

    # Q3
    q3 = Question.objects.create(text="What sounds more exciting?")
    Choice.objects.create(question=q3, text="Automating server tasks to save time.", related_domain=devops) # Logic=1
    Choice.objects.create(question=q3, text="Creating a beautiful user interface.", related_domain=frontend) # Logic=0

    print("📚 Adding Detailed Roadmaps...")
    
    # --- FRONTEND RESOURCES ---
    resources_fe = [
        (1, "HTML & CSS Full Course", "https://youtu.be/G3e-cpL7ofc", "Video", "Free"),
        (2, "Modern JavaScript Tutorial", "https://javascript.info/", "Article", "Free"),
        (3, "React - The Complete Guide", "https://www.udemy.com/course/react-the-complete-guide-incl-redux/", "Course", "Paid"),
        (4, "Tailwind CSS Documentation", "https://tailwindcss.com/docs", "Article", "Free"),
    ]
    for step, title, link, rtype, cost in resources_fe:
        Resource.objects.create(domain=frontend, step_number=step, title=title, link=link, resource_type=rtype, cost=cost)

    # --- DATA SCIENCE RESOURCES ---
    resources_ds = [
        (1, "Python for Data Science", "https://www.freecodecamp.org/learn/data-analysis-with-python/", "Course", "Free"),
        (2, "Intro to Statistics (Khan Academy)", "https://www.khanacademy.org/math/statistics-probability", "Video", "Free"),
        (3, "Machine Learning by Andrew Ng", "https://www.coursera.org/learn/machine-learning", "Course", "Paid"),
        (4, "Kaggle Datasets & Competitions", "https://www.kaggle.com/", "Article", "Free"),
    ]
    for step, title, link, rtype, cost in resources_ds:
        Resource.objects.create(domain=ds, step_number=step, title=title, link=link, resource_type=rtype, cost=cost)

    print("✅ Database Populated Successfully!")

if __name__ == '__main__':
    populate()