import csv

# Your data manually arranged as tuples: (Title, Link)
data = [
    ("10 Best Online Prompt Engineering Courses [Free & Paid]", "https://learnprompting.org/blog/prompt_engineering_courses?srsltid=AfmBOoqg8vHiMkjlUEt63Uf-kZsuRLxIduneNVrTypPDxm21FR_ztZDf"),
    ("Free Prompt Engineering for ChatGPT Course with Certificate", "https://www.mygreatlearning.com/academy/learn-for-free/courses/prompt-engineering-for-chatgpt"),
    ("N/A", "https://learnprompting.org/blog/prompt_engineering_courses"),
    ("N/A", "https://www.justdial.com/Bangalore/Training-Institutes-For-Prompt-Engineering/nct-15610421"),
    ("N/A", "https://www.coursera.org/articles/how-to-become-a-prompt-engineer"),
    ("N/A", "https://www.edureka.co/prompt-engineering-generative-ai-course"),
    ("Prompt Engineering for ChatGPT", "https://www.coursera.org/learn/prompt-engineering"),
    ("The 10 best free prompt engineering courses & resources for ...", "https://blog.big-picture.com/en/the-10-best-free-prompt-engineering-courses-resources-for-chatgpt-midjourney-co/"),
    ("ChatGPT Prompt Engineering ( Free Course )", "https://www.udemy.com/course/chatgpt-prompt-engineering-free-course/?srsltid=AfmBOop_VdMbk0Hbx6URXkbshM4RZ8JkdAk4S_YJViahUKLkFvrUlLxQ"),
    ("How to learn prompt engineering for free", "https://www.reddit.com/r/PromptEngineering/comments/1g068oy/how_to_learn_prompt_engineering_for_free/"),
    ("Free Prompt Engineering Course with Certificate for ChatGPT", "https://www.simplilearn.com/prompt-engineering-free-course-skillup"),
    ("10 Best Prompt Engineering Courses [2025]", "https://www.geeksforgeeks.org/best-prompt-engineering-courses/"),
    ("ChatGPT Prompt Engineering for Developers", "https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/"),
    ("The 10 Best Free Prompt Engineering Courses & ...", "https://medium.com/@maximilian.vogel/the-10-best-free-prompt-engineering-courses-resources-for-chatgpt-midjourney-co-dd1865d4ad13"),
    ("Advanced Prompt Engineering Course with ChatGPT", "https://www.upgrad.com/free-courses/chatgpt-and-ai/advanced-prompt-engineering-course-free-with-chatgpt/"),
    ("Best Prompt Engineering Courses & Certificates Online ...", "https://www.coursera.org/courses?query=prompt%20engineering"),
    ("Prompt Engineering Courses and Certifications", "https://www.classcentral.com/subject/prompt-engineering"),
    ("AI Course Catalog", "https://learnprompting.org/courses?srsltid=AfmBOors47d9t9cxdVaLkdvoxqVuxGI8PHUycGdxpAE0q7Ip-7g_AWwm"),
    ("Prompt Engineering for AI Guide", "https://cloud.google.com/discover/what-is-prompt-engineering"),
    ("Introduction to Prompt Engineering for Generative AI", "https://www.linkedin.com/learning/introduction-to-prompt-engineering-for-generative-ai-24636124"),
    ("5 Free Courses for Mastering Prompt Engineering", "https://www.cmswire.com/digital-experience/top-5-free-prompt-engineering-courses/")
]

# Save to CSV
with open("final_prompt_engineering_links.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Link"])
    writer.writerows(data)

print("✅ CSV file saved as 'final_prompt_engineering_links.csv'")
