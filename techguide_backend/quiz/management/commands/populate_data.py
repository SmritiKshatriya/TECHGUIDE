from django.core.management.base import BaseCommand
from quiz.models import Domain
from roadmaps.models import RoadmapStep
from resources.models import Resource


class Command(BaseCommand):
    help = 'Populate roadmap steps and resources for all domains'

    def handle(self, *args, **kwargs):
        self.populate_web_development()
        self.populate_data_science()
        self.populate_cybersecurity()
        self.populate_ai_ml()
        self.populate_mobile_development()
        self.populate_cloud_devops()
        self.stdout.write(self.style.SUCCESS('All roadmaps populated!'))

    def add_step(self, domain_slug, title, description, level, order, weeks, milestone=False):
        domain = Domain.objects.get(slug=domain_slug)
        step, created = RoadmapStep.objects.get_or_create(
            domain=domain, title=title,
            defaults={
                'description': description,
                'level': level,
                'order': order,
                'estimated_weeks': weeks,
                'is_milestone': milestone
            }
        )
        if created:
            self.stdout.write(f'  + {title}')
        return step

    def add_resource(self, step, title, url, rtype, platform, is_free, difficulty, hours=1.0, desc=''):
        Resource.objects.get_or_create(
            step=step, title=title,
            defaults={
                'url': url,
                'resource_type': rtype,
                'platform': platform,
                'is_free': is_free,
                'difficulty': difficulty,
                'estimated_hours': hours,
                'description': desc
            }
        )

    def populate_web_development(self):
        self.stdout.write('Creating Web Development roadmap...')
        slug = 'web-development'

        # Level 1 - Foundations
        s = self.add_step(slug, 'How the Web Works', 'HTTP, DNS, browsers, servers and clients.', 1, 1, 1)
        self.add_resource(s, 'How the Web Works - MDN', 'https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works', 'ARTICLE', 'MDN', True, 'BEGINNER', 1)
        self.add_resource(s, 'CS50 Web - Lecture 1', 'https://www.youtube.com/watch?v=4rNYAvsSkwk', 'VIDEO', 'YouTube', True, 'BEGINNER', 2)

        s = self.add_step(slug, 'HTML Fundamentals', 'Semantic HTML, forms, tables, accessibility basics.', 1, 2, 2)
        self.add_resource(s, 'HTML Full Course - freeCodeCamp', 'https://www.youtube.com/watch?v=pQN-pnXPaVg', 'VIDEO', 'YouTube', True, 'BEGINNER', 4)
        self.add_resource(s, 'HTML - MDN Docs', 'https://developer.mozilla.org/en-US/docs/Web/HTML', 'ARTICLE', 'MDN', True, 'BEGINNER', 2)

        s = self.add_step(slug, 'CSS Basics', 'Selectors, box model, flexbox, grid, responsive design.', 1, 3, 3)
        self.add_resource(s, 'CSS Full Course - freeCodeCamp', 'https://www.youtube.com/watch?v=OXGznpKZ_sA', 'VIDEO', 'YouTube', True, 'BEGINNER', 5)
        self.add_resource(s, 'Flexbox Froggy', 'https://flexboxfroggy.com/', 'INTERACTIVE', 'Flexbox Froggy', True, 'BEGINNER', 1)

        s = self.add_step(slug, 'JavaScript Fundamentals', 'Variables, functions, loops, DOM manipulation.', 1, 4, 3, True)
        self.add_resource(s, 'JavaScript Full Course - freeCodeCamp', 'https://www.youtube.com/watch?v=PkZNo7MFNFg', 'VIDEO', 'YouTube', True, 'BEGINNER', 7)
        self.add_resource(s, 'JavaScript.info', 'https://javascript.info/', 'ARTICLE', 'javascript.info', True, 'BEGINNER', 10)

        # Level 2 - Beginner
        s = self.add_step(slug, 'Git & Version Control', 'Git init, add, commit, push, pull, branches.', 2, 1, 1)
        self.add_resource(s, 'Git & GitHub Crash Course', 'https://www.youtube.com/watch?v=RGOj5yH7evk', 'VIDEO', 'YouTube', True, 'BEGINNER', 1)
        self.add_resource(s, 'Pro Git Book', 'https://git-scm.com/book/en/v2', 'BOOK', 'git-scm.com', True, 'BEGINNER', 5)

        s = self.add_step(slug, 'Responsive Design', 'Media queries, mobile-first design, CSS frameworks.', 2, 2, 2)
        self.add_resource(s, 'Responsive Web Design - freeCodeCamp', 'https://www.freecodecamp.org/learn/2022/responsive-web-design/', 'INTERACTIVE', 'freeCodeCamp', True, 'BEGINNER', 10)

        s = self.add_step(slug, 'JavaScript ES6+', 'Arrow functions, async/await, destructuring, modules.', 2, 3, 2, True)
        self.add_resource(s, 'ES6 JavaScript Tutorial', 'https://www.youtube.com/watch?v=nZ1DMMsyVyI', 'VIDEO', 'YouTube', True, 'BEGINNER', 3)

        s = self.add_step(slug, 'React Basics', 'Components, props, state, hooks, JSX.', 2, 4, 3)
        self.add_resource(s, 'React Official Tutorial', 'https://react.dev/learn', 'ARTICLE', 'React Docs', True, 'BEGINNER', 8)
        self.add_resource(s, 'React Course - freeCodeCamp', 'https://www.youtube.com/watch?v=bMknfKXIFA8', 'VIDEO', 'YouTube', True, 'BEGINNER', 12)

        # Level 3 - Intermediate
        s = self.add_step(slug, 'Node.js & Express', 'Server-side JavaScript, REST APIs, middleware.', 3, 1, 3)
        self.add_resource(s, 'Node.js Crash Course', 'https://www.youtube.com/watch?v=fBNz5xF-Kx4', 'VIDEO', 'YouTube', True, 'INTERMEDIATE', 3)
        self.add_resource(s, 'The Odin Project - Node', 'https://www.theodinproject.com/paths/full-stack-javascript', 'INTERACTIVE', 'The Odin Project', True, 'INTERMEDIATE', 20)

        s = self.add_step(slug, 'Databases & SQL', 'PostgreSQL, MySQL basics, queries, joins, ORMs.', 3, 2, 2)
        self.add_resource(s, 'SQL Full Course', 'https://www.youtube.com/watch?v=HXV3zeQKqGY', 'VIDEO', 'YouTube', True, 'INTERMEDIATE', 4)

        s = self.add_step(slug, 'Authentication & Security', 'JWT, sessions, OAuth, password hashing.', 3, 3, 2, True)
        self.add_resource(s, 'Web Security - MDN', 'https://developer.mozilla.org/en-US/docs/Web/Security', 'ARTICLE', 'MDN', True, 'INTERMEDIATE', 3)

        s = self.add_step(slug, 'React Advanced', 'Redux, React Query, performance optimization.', 3, 4, 3)
        self.add_resource(s, 'Redux Toolkit Tutorial', 'https://www.youtube.com/watch?v=bbkBuqC1rU4', 'VIDEO', 'YouTube', True, 'INTERMEDIATE', 4)

        # Level 4 - Advanced
        s = self.add_step(slug, 'System Design Basics', 'Scalability, load balancing, caching, microservices.', 4, 1, 3)
        self.add_resource(s, 'System Design Primer', 'https://github.com/donnemartin/system-design-primer', 'ARTICLE', 'GitHub', True, 'ADVANCED', 15)

        s = self.add_step(slug, 'Testing', 'Unit tests, integration tests, Jest, Cypress.', 4, 2, 2)
        self.add_resource(s, 'JavaScript Testing - freeCodeCamp', 'https://www.youtube.com/watch?v=IPiUDhwnZxA', 'VIDEO', 'YouTube', True, 'ADVANCED', 4)

        s = self.add_step(slug, 'DevOps for Web Devs', 'Docker, CI/CD, deployment, Nginx basics.', 4, 3, 2, True)
        self.add_resource(s, 'Docker Tutorial for Beginners', 'https://www.youtube.com/watch?v=fqMOX6JJhGo', 'VIDEO', 'YouTube', True, 'ADVANCED', 3)

        # Level 5 - Expert
        s = self.add_step(slug, 'Web Performance', 'Core Web Vitals, lazy loading, code splitting, CDN.', 5, 1, 2)
        self.add_resource(s, 'Web Performance - web.dev', 'https://web.dev/performance/', 'ARTICLE', 'Google', True, 'ADVANCED', 5)

        s = self.add_step(slug, 'Full Stack Architecture', 'Design and build complete production applications.', 5, 2, 4, True)
        self.add_resource(s, 'Full Stack Open', 'https://fullstackopen.com/', 'INTERACTIVE', 'University of Helsinki', True, 'ADVANCED', 40)

    def populate_data_science(self):
        self.stdout.write('Creating Data Science roadmap...')
        slug = 'data-science'

        # Level 1
        s = self.add_step(slug, 'Python for Data Science', 'Python basics, NumPy, Pandas fundamentals.', 1, 1, 3)
        self.add_resource(s, 'Python for Everybody - Coursera', 'https://www.coursera.org/specializations/python', 'COURSE', 'Coursera', False, 'BEGINNER', 20)
        self.add_resource(s, 'Python Data Science Handbook', 'https://jakevdp.github.io/PythonDataScienceHandbook/', 'BOOK', 'GitHub', True, 'BEGINNER', 15)

        s = self.add_step(slug, 'Statistics & Mathematics', 'Mean, median, probability, distributions, hypothesis testing.', 1, 2, 2)
        self.add_resource(s, 'Statistics - Khan Academy', 'https://www.khanacademy.org/math/statistics-probability', 'INTERACTIVE', 'Khan Academy', True, 'BEGINNER', 10)

        s = self.add_step(slug, 'Data Cleaning with Pandas', 'Load, clean, filter, transform real datasets.', 1, 3, 2, True)
        self.add_resource(s, 'Pandas Tutorial - freeCodeCamp', 'https://www.youtube.com/watch?v=vmEHCJofslg', 'VIDEO', 'YouTube', True, 'BEGINNER', 4)
        self.add_resource(s, 'Pandas Official Docs', 'https://pandas.pydata.org/docs/getting_started/index.html', 'ARTICLE', 'Pandas', True, 'BEGINNER', 3)

        # Level 2
        s = self.add_step(slug, 'Data Visualization', 'Matplotlib, Seaborn, Plotly for charts and dashboards.', 2, 1, 2)
        self.add_resource(s, 'Matplotlib Tutorial', 'https://www.youtube.com/watch?v=3Xc3CA655Y4', 'VIDEO', 'YouTube', True, 'BEGINNER', 3)

        s = self.add_step(slug, 'Exploratory Data Analysis', 'Finding patterns, correlations, and insights in data.', 2, 2, 2, True)
        self.add_resource(s, 'EDA with Python - Kaggle', 'https://www.kaggle.com/learn/pandas', 'INTERACTIVE', 'Kaggle', True, 'BEGINNER', 4)

        s = self.add_step(slug, 'SQL for Data Science', 'Queries, joins, aggregations, window functions.', 2, 3, 2)
        self.add_resource(s, 'SQL for Data Science - Coursera', 'https://www.coursera.org/learn/sql-for-data-science', 'COURSE', 'Coursera', False, 'BEGINNER', 8)
        self.add_resource(s, 'SQLZoo', 'https://sqlzoo.net/', 'INTERACTIVE', 'SQLZoo', True, 'BEGINNER', 5)

        # Level 3
        s = self.add_step(slug, 'Machine Learning Basics', 'Regression, classification, clustering with Scikit-learn.', 3, 1, 4, True)
        self.add_resource(s, 'ML Course - Andrew Ng', 'https://www.coursera.org/learn/machine-learning', 'COURSE', 'Coursera', False, 'INTERMEDIATE', 30)
        self.add_resource(s, 'Scikit-learn Docs', 'https://scikit-learn.org/stable/getting_started.html', 'ARTICLE', 'Scikit-learn', True, 'INTERMEDIATE', 5)

        s = self.add_step(slug, 'Feature Engineering', 'Creating and selecting features to improve models.', 3, 2, 2)
        self.add_resource(s, 'Feature Engineering - Kaggle', 'https://www.kaggle.com/learn/feature-engineering', 'INTERACTIVE', 'Kaggle', True, 'INTERMEDIATE', 5)

        s = self.add_step(slug, 'Model Evaluation', 'Cross-validation, metrics, bias-variance tradeoff.', 3, 3, 2)
        self.add_resource(s, 'Model Evaluation - StatQuest', 'https://www.youtube.com/watch?v=fSytzGwwBVw', 'VIDEO', 'YouTube', True, 'INTERMEDIATE', 2)

        # Level 4
        s = self.add_step(slug, 'Deep Learning Intro', 'Neural networks, backpropagation, TensorFlow basics.', 4, 1, 4, True)
        self.add_resource(s, 'Deep Learning Specialization', 'https://www.coursera.org/specializations/deep-learning', 'COURSE', 'Coursera', False, 'ADVANCED', 50)

        s = self.add_step(slug, 'Big Data Tools', 'Spark, Hadoop, distributed computing basics.', 4, 2, 3)
        self.add_resource(s, 'Apache Spark Tutorial', 'https://www.youtube.com/watch?v=_C8kWso4ne4', 'VIDEO', 'YouTube', True, 'ADVANCED', 4)

        # Level 5
        s = self.add_step(slug, 'MLOps & Deployment', 'Deploy models to production, monitoring, pipelines.', 5, 1, 3)
        self.add_resource(s, 'MLOps Course - freeCodeCamp', 'https://www.youtube.com/watch?v=NgWujOrCZFo', 'VIDEO', 'YouTube', True, 'ADVANCED', 6)

        s = self.add_step(slug, 'Data Science Portfolio', 'Build end-to-end projects for Kaggle and GitHub.', 5, 2, 4, True)
        self.add_resource(s, 'Kaggle Competitions', 'https://www.kaggle.com/competitions', 'INTERACTIVE', 'Kaggle', True, 'ADVANCED', 20)

    def populate_cybersecurity(self):
        self.stdout.write('Creating Cybersecurity roadmap...')
        slug = 'cybersecurity'

        # Level 1
        s = self.add_step(slug, 'Networking Basics', 'TCP/IP, DNS, HTTP, firewalls, OSI model.', 1, 1, 2)
        self.add_resource(s, 'Networking Basics - Cisco', 'https://www.netacad.com/courses/networking/networking-basics', 'COURSE', 'Cisco', True, 'BEGINNER', 10)
        self.add_resource(s, 'Computer Networking - Khan Academy', 'https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:the-internet', 'INTERACTIVE', 'Khan Academy', True, 'BEGINNER', 3)

        s = self.add_step(slug, 'Linux Fundamentals', 'Command line, file permissions, processes, scripting.', 1, 2, 2)
        self.add_resource(s, 'Linux Command Line - freeCodeCamp', 'https://www.youtube.com/watch?v=ZtqBQ68cfJc', 'VIDEO', 'YouTube', True, 'BEGINNER', 5)

        s = self.add_step(slug, 'Security Fundamentals', 'CIA triad, encryption basics, common attack types.', 1, 3, 2, True)
        self.add_resource(s, 'Cybersecurity for Everyone - Coursera', 'https://www.coursera.org/learn/cybersecurity-for-everyone', 'COURSE', 'Coursera', False, 'BEGINNER', 8)

        # Level 2
        s = self.add_step(slug, 'Web Application Security', 'OWASP Top 10, XSS, SQL injection, CSRF.', 2, 1, 3, True)
        self.add_resource(s, 'OWASP Top 10', 'https://owasp.org/www-project-top-ten/', 'ARTICLE', 'OWASP', True, 'BEGINNER', 5)
        self.add_resource(s, 'Web Security - PortSwigger', 'https://portswigger.net/web-security', 'INTERACTIVE', 'PortSwigger', True, 'INTERMEDIATE', 20)

        s = self.add_step(slug, 'Cryptography Basics', 'Symmetric/asymmetric encryption, hashing, PKI.', 2, 2, 2)
        self.add_resource(s, 'Cryptography - Khan Academy', 'https://www.khanacademy.org/computing/computer-science/cryptography', 'INTERACTIVE', 'Khan Academy', True, 'BEGINNER', 4)

        s = self.add_step(slug, 'Ethical Hacking Intro', 'Penetration testing methodology, tools like Kali Linux.', 2, 3, 3)
        self.add_resource(s, 'Ethical Hacking - TCM Security', 'https://www.youtube.com/watch?v=3Kq1MIfTWCE', 'VIDEO', 'YouTube', True, 'INTERMEDIATE', 10)

        # Level 3
        s = self.add_step(slug, 'Network Security', 'VPNs, IDS/IPS, network scanning, Wireshark.', 3, 1, 3, True)
        self.add_resource(s, 'Wireshark Tutorial', 'https://www.youtube.com/watch?v=lb1Dw0elw0Q', 'VIDEO', 'YouTube', True, 'INTERMEDIATE', 3)

        s = self.add_step(slug, 'CTF Challenges', 'Capture the Flag competitions to practice skills.', 3, 2, 3)
        self.add_resource(s, 'TryHackMe', 'https://tryhackme.com/', 'INTERACTIVE', 'TryHackMe', True, 'INTERMEDIATE', 20)
        self.add_resource(s, 'HackTheBox', 'https://www.hackthebox.com/', 'INTERACTIVE', 'HackTheBox', True, 'INTERMEDIATE', 20)

        # Level 4
        s = self.add_step(slug, 'Malware Analysis', 'Static and dynamic analysis of malicious software.', 4, 1, 3)
        self.add_resource(s, 'Malware Analysis - OpenSecurityTraining', 'https://opensecuritytraining.info/', 'COURSE', 'OpenSecurityTraining', True, 'ADVANCED', 15)

        s = self.add_step(slug, 'Security Certifications', 'CompTIA Security+, CEH, OSCP preparation.', 4, 2, 4, True)
        self.add_resource(s, 'CompTIA Security+ Study Guide', 'https://www.youtube.com/watch?v=9NE33fpQuw8', 'VIDEO', 'YouTube', True, 'ADVANCED', 10)

        # Level 5
        s = self.add_step(slug, 'Red Team vs Blue Team', 'Offensive and defensive security operations.', 5, 1, 4)
        self.add_resource(s, 'Red Team Development - SANS', 'https://www.sans.org/cyber-security-courses/', 'COURSE', 'SANS', False, 'ADVANCED', 30)

        s = self.add_step(slug, 'Security Architecture', 'Design secure systems, threat modeling, zero trust.', 5, 2, 4, True)
        self.add_resource(s, 'Zero Trust Security - Google', 'https://cloud.google.com/beyondcorp', 'ARTICLE', 'Google', True, 'ADVANCED', 3)

    def populate_ai_ml(self):
        self.stdout.write('Creating AI & Machine Learning roadmap...')
        slug = 'ai-ml'

        # Level 1
        s = self.add_step(slug, 'Python & Math Foundations', 'Python, NumPy, linear algebra, calculus basics.', 1, 1, 3)
        self.add_resource(s, 'Python for ML - freeCodeCamp', 'https://www.youtube.com/watch?v=i_LwzRVP7bg', 'VIDEO', 'YouTube', True, 'BEGINNER', 6)
        self.add_resource(s, 'Linear Algebra - 3Blue1Brown', 'https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab', 'VIDEO', 'YouTube', True, 'BEGINNER', 5)

        s = self.add_step(slug, 'Statistics for ML', 'Probability, distributions, Bayes theorem.', 1, 2, 2)
        self.add_resource(s, 'Statistics for ML - StatQuest', 'https://www.youtube.com/watch?v=qBigTkBLU6g', 'VIDEO', 'YouTube', True, 'BEGINNER', 4)

        s = self.add_step(slug, 'ML Fundamentals', 'Supervised, unsupervised learning, model evaluation.', 1, 3, 3, True)
        self.add_resource(s, 'ML Crash Course - Google', 'https://developers.google.com/machine-learning/crash-course', 'COURSE', 'Google', True, 'BEGINNER', 15)

        # Level 2
        s = self.add_step(slug, 'Scikit-learn', 'Classification, regression, clustering, pipelines.', 2, 1, 2)
        self.add_resource(s, 'Scikit-learn Tutorial', 'https://www.youtube.com/watch?v=0B5eIE_1vpU', 'VIDEO', 'YouTube', True, 'BEGINNER', 3)
        self.add_resource(s, 'Kaggle ML Course', 'https://www.kaggle.com/learn/intro-to-machine-learning', 'INTERACTIVE', 'Kaggle', True, 'BEGINNER', 5)

        s = self.add_step(slug, 'Neural Networks Basics', 'Perceptrons, activation functions, backpropagation.', 2, 2, 3, True)
        self.add_resource(s, 'Neural Networks - 3Blue1Brown', 'https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi', 'VIDEO', 'YouTube', True, 'INTERMEDIATE', 4)

        s = self.add_step(slug, 'TensorFlow & Keras', 'Build and train deep learning models.', 2, 3, 3)
        self.add_resource(s, 'TensorFlow Official Tutorial', 'https://www.tensorflow.org/tutorials', 'ARTICLE', 'TensorFlow', True, 'INTERMEDIATE', 8)

        # Level 3
        s = self.add_step(slug, 'Computer Vision', 'CNNs, image classification, object detection.', 3, 1, 4, True)
        self.add_resource(s, 'Computer Vision - fast.ai', 'https://course.fast.ai/', 'COURSE', 'fast.ai', True, 'INTERMEDIATE', 30)

        s = self.add_step(slug, 'Natural Language Processing', 'Text processing, sentiment analysis, transformers.', 3, 2, 4)
        self.add_resource(s, 'NLP with Python - freeCodeCamp', 'https://www.youtube.com/watch?v=X2vAabgKiuM', 'VIDEO', 'YouTube', True, 'INTERMEDIATE', 5)
        self.add_resource(s, 'Hugging Face Course', 'https://huggingface.co/learn/nlp-course', 'INTERACTIVE', 'Hugging Face', True, 'INTERMEDIATE', 20)

        # Level 4
        s = self.add_step(slug, 'Large Language Models', 'GPT architecture, fine-tuning, prompt engineering.', 4, 1, 3)
        self.add_resource(s, 'LLM Course - Andrej Karpathy', 'https://www.youtube.com/watch?v=kCc8FmEb1nY', 'VIDEO', 'YouTube', True, 'ADVANCED', 4)

        s = self.add_step(slug, 'MLOps & Production', 'Deploy models, monitoring, A/B testing, pipelines.', 4, 2, 3, True)
        self.add_resource(s, 'MLOps Zoomcamp', 'https://github.com/DataTalksClub/mlops-zoomcamp', 'COURSE', 'DataTalks.Club', True, 'ADVANCED', 40)

        # Level 5
        s = self.add_step(slug, 'AI Research Papers', 'Read and implement papers from arXiv and top conferences.', 5, 1, 4)
        self.add_resource(s, 'Papers With Code', 'https://paperswithcode.com/', 'ARTICLE', 'Papers With Code', True, 'ADVANCED', 20)

        s = self.add_step(slug, 'AI Project Portfolio', 'Build end-to-end AI projects and publish on GitHub.', 5, 2, 4, True)
        self.add_resource(s, 'Kaggle Competitions', 'https://www.kaggle.com/competitions', 'INTERACTIVE', 'Kaggle', True, 'ADVANCED', 20)

    def populate_mobile_development(self):
        self.stdout.write('Creating Mobile Development roadmap...')
        slug = 'mobile-development'

        # Level 1
        s = self.add_step(slug, 'Mobile Dev Fundamentals', 'iOS vs Android, native vs cross-platform, app lifecycle.', 1, 1, 1)
        self.add_resource(s, 'Mobile Dev Overview - freeCodeCamp', 'https://www.youtube.com/watch?v=0-S5a0eXPoc', 'VIDEO', 'YouTube', True, 'BEGINNER', 2)

        s = self.add_step(slug, 'JavaScript & React Basics', 'JS fundamentals and React concepts needed for React Native.', 1, 2, 3)
        self.add_resource(s, 'JavaScript Full Course', 'https://www.youtube.com/watch?v=PkZNo7MFNFg', 'VIDEO', 'YouTube', True, 'BEGINNER', 7)

        s = self.add_step(slug, 'React Native Setup', 'Environment setup, Expo, first app, components.', 1, 3, 2, True)
        self.add_resource(s, 'React Native - Official Docs', 'https://reactnative.dev/docs/getting-started', 'ARTICLE', 'React Native', True, 'BEGINNER', 3)
        self.add_resource(s, 'React Native Crash Course', 'https://www.youtube.com/watch?v=0-S5a0eXPoc', 'VIDEO', 'YouTube', True, 'BEGINNER', 3)

        # Level 2
        s = self.add_step(slug, 'Navigation & Routing', 'React Navigation, stack, tab, drawer navigation.', 2, 1, 2)
        self.add_resource(s, 'React Navigation Docs', 'https://reactnavigation.org/docs/getting-started', 'ARTICLE', 'React Navigation', True, 'BEGINNER', 3)

        s = self.add_step(slug, 'State Management', 'useState, useContext, Redux for mobile apps.', 2, 2, 2, True)
        self.add_resource(s, 'React Native State Management', 'https://www.youtube.com/watch?v=re3OIOr9dJI', 'VIDEO', 'YouTube', True, 'INTERMEDIATE', 3)

        s = self.add_step(slug, 'Device APIs', 'Camera, GPS, push notifications, storage.', 2, 3, 2)
        self.add_resource(s, 'Expo Device APIs', 'https://docs.expo.dev/versions/latest/', 'ARTICLE', 'Expo', True, 'INTERMEDIATE', 4)

        # Level 3
        s = self.add_step(slug, 'Backend Integration', 'REST APIs, Firebase, authentication in mobile apps.', 3, 1, 3, True)
        self.add_resource(s, 'Firebase with React Native', 'https://www.youtube.com/watch?v=ql4J6SpLXZA', 'VIDEO', 'YouTube', True, 'INTERMEDIATE', 4)

        s = self.add_step(slug, 'UI/UX for Mobile', 'Mobile design patterns, gestures, animations.', 3, 2, 2)
        self.add_resource(s, 'React Native Animations', 'https://reactnative.dev/docs/animations', 'ARTICLE', 'React Native', True, 'INTERMEDIATE', 3)

        s = self.add_step(slug, 'Flutter Basics', 'Dart language, Flutter widgets, cross-platform.', 3, 3, 3)
        self.add_resource(s, 'Flutter Course - freeCodeCamp', 'https://www.youtube.com/watch?v=VPvVD8t02U8', 'VIDEO', 'YouTube', True, 'INTERMEDIATE', 6)
        self.add_resource(s, 'Flutter Official Docs', 'https://flutter.dev/docs', 'ARTICLE', 'Flutter', True, 'INTERMEDIATE', 5)

        # Level 4
        s = self.add_step(slug, 'App Performance', 'Profiling, optimization, memory management.', 4, 1, 2)
        self.add_resource(s, 'React Native Performance', 'https://reactnative.dev/docs/performance', 'ARTICLE', 'React Native', True, 'ADVANCED', 3)

        s = self.add_step(slug, 'App Store Deployment', 'Publishing to Google Play Store and Apple App Store.', 4, 2, 2, True)
        self.add_resource(s, 'Publishing React Native Apps', 'https://www.youtube.com/watch?v=oBWBDaqNuws', 'VIDEO', 'YouTube', True, 'ADVANCED', 3)

        # Level 5
        s = self.add_step(slug, 'Native Modules', 'Bridge between JavaScript and native iOS/Android code.', 5, 1, 3)
        self.add_resource(s, 'Native Modules Guide', 'https://reactnative.dev/docs/native-modules-intro', 'ARTICLE', 'React Native', True, 'ADVANCED', 4)

        s = self.add_step(slug, 'Mobile App Portfolio', 'Build and publish 2-3 complete apps to app stores.', 5, 2, 6, True)
        self.add_resource(s, 'App Ideas Collection', 'https://github.com/florinpop17/app-ideas', 'ARTICLE', 'GitHub', True, 'ADVANCED', 5)

    def populate_cloud_devops(self):
        self.stdout.write('Creating Cloud & DevOps roadmap...')
        slug = 'cloud-devops'

        # Level 1
        s = self.add_step(slug, 'Linux & Command Line', 'Shell scripting, file system, processes, permissions.', 1, 1, 2)
        self.add_resource(s, 'Linux Command Line - freeCodeCamp', 'https://www.youtube.com/watch?v=ZtqBQ68cfJc', 'VIDEO', 'YouTube', True, 'BEGINNER', 5)
        self.add_resource(s, 'Linux Journey', 'https://linuxjourney.com/', 'INTERACTIVE', 'Linux Journey', True, 'BEGINNER', 5)

        s = self.add_step(slug, 'Networking Fundamentals', 'TCP/IP, DNS, HTTP, load balancers, firewalls.', 1, 2, 2)
        self.add_resource(s, 'Networking for DevOps', 'https://www.youtube.com/watch?v=IPvYjXCsTg8', 'VIDEO', 'YouTube', True, 'BEGINNER', 3)

        s = self.add_step(slug, 'Git & Version Control', 'Git workflow, branching strategies, GitHub Actions basics.', 1, 3, 1, True)
        self.add_resource(s, 'Git & GitHub Crash Course', 'https://www.youtube.com/watch?v=RGOj5yH7evk', 'VIDEO', 'YouTube', True, 'BEGINNER', 1)

        # Level 2
        s = self.add_step(slug, 'Docker & Containers', 'Images, containers, Dockerfile, Docker Compose.', 2, 1, 3, True)
        self.add_resource(s, 'Docker Tutorial - TechWorld with Nana', 'https://www.youtube.com/watch?v=3c-iBn73dDE', 'VIDEO', 'YouTube', True, 'BEGINNER', 4)
        self.add_resource(s, 'Docker Official Docs', 'https://docs.docker.com/get-started/', 'ARTICLE', 'Docker', True, 'BEGINNER', 3)

        s = self.add_step(slug, 'CI/CD Pipelines', 'GitHub Actions, automated testing, deployment pipelines.', 2, 2, 2)
        self.add_resource(s, 'GitHub Actions Tutorial', 'https://www.youtube.com/watch?v=R8_veQiYBjI', 'VIDEO', 'YouTube', True, 'INTERMEDIATE', 3)

        s = self.add_step(slug, 'Cloud Basics - AWS', 'EC2, S3, IAM, VPC, core AWS services.', 2, 3, 3)
        self.add_resource(s, 'AWS Cloud Practitioner - freeCodeCamp', 'https://www.youtube.com/watch?v=SOTamWNgDKc', 'VIDEO', 'YouTube', True, 'BEGINNER', 14)
        self.add_resource(s, 'AWS Free Tier', 'https://aws.amazon.com/free/', 'INTERACTIVE', 'AWS', True, 'BEGINNER', 10)

        # Level 3
        s = self.add_step(slug, 'Kubernetes', 'Container orchestration, pods, services, deployments.', 3, 1, 4, True)
        self.add_resource(s, 'Kubernetes Tutorial - TechWorld with Nana', 'https://www.youtube.com/watch?v=X48VuDVv0do', 'VIDEO', 'YouTube', True, 'INTERMEDIATE', 4)
        self.add_resource(s, 'Kubernetes Official Docs', 'https://kubernetes.io/docs/tutorials/', 'ARTICLE', 'Kubernetes', True, 'INTERMEDIATE', 8)

        s = self.add_step(slug, 'Infrastructure as Code', 'Terraform, CloudFormation, managing infra with code.', 3, 2, 3)
        self.add_resource(s, 'Terraform Tutorial', 'https://www.youtube.com/watch?v=SLB_c_ayRMo', 'VIDEO', 'YouTube', True, 'INTERMEDIATE', 4)

        s = self.add_step(slug, 'Monitoring & Logging', 'Prometheus, Grafana, ELK stack, alerting.', 3, 3, 2)
        self.add_resource(s, 'Prometheus & Grafana Tutorial', 'https://www.youtube.com/watch?v=h4Sl21AKiDg', 'VIDEO', 'YouTube', True, 'INTERMEDIATE', 3)

        # Level 4
        s = self.add_step(slug, 'Cloud Security', 'IAM best practices, secrets management, compliance.', 4, 1, 2)
        self.add_resource(s, 'AWS Security Best Practices', 'https://aws.amazon.com/architecture/security-identity-compliance/', 'ARTICLE', 'AWS', True, 'ADVANCED', 4)

        s = self.add_step(slug, 'Microservices Architecture', 'Design, deploy and manage microservices at scale.', 4, 2, 3, True)
        self.add_resource(s, 'Microservices - Martin Fowler', 'https://martinfowler.com/articles/microservices.html', 'ARTICLE', 'martinfowler.com', True, 'ADVANCED', 3)

        # Level 5
        s = self.add_step(slug, 'Cloud Certifications', 'AWS Solutions Architect, CKA, GCP Professional.', 5, 1, 6)
        self.add_resource(s, 'AWS Solutions Architect - freeCodeCamp', 'https://www.youtube.com/watch?v=Ia-UEYYR44s', 'VIDEO', 'YouTube', True, 'ADVANCED', 10)

        s = self.add_step(slug, 'DevOps Portfolio', 'Build complete CI/CD pipelines and cloud infrastructure.', 5, 2, 4, True)
        self.add_resource(s, 'DevOps Projects - GitHub', 'https://github.com/topics/devops-project', 'ARTICLE', 'GitHub', True, 'ADVANCED', 10)


