import os

workspace = "/home/azaz/AntigravityData/Chemistry-Semester-Final"

readmes = {
    "boss_notes": """# 👑 Boss Notes
> **The Definitive, High-Fidelity Master Study Guide for the Chemistry Semester Final**

Welcome to the `boss_notes` directory, the crown jewel and pedagogical core of the Chemistry Semester Final repository. If you are short on time and need to study for the exam immediately, **start here.**

## 🎯 Purpose & Philosophy
Unlike raw lecture slides or unstructured notes, the files in this directory have been meticulously synthesized. The philosophy behind `boss_notes` is to eliminate the friction of studying by bridging raw facts with deep, actionable understanding.

Every sub-topic in this directory has been standardized to feature:
1.  **📌 Quick Summary:** A high-level "elevator pitch" of the concept to ground your understanding before diving into the math.
2.  **📖 Core Theory:** Clear, pedagogical explanations that focus on the *why* and *how*, rather than just rote memorization.
3.  **🧮 Key Derivations:** Step-by-step mathematical proofs (e.g., Nernst Equation, Arrhenius Equation) with rigorous, boxed LaTeX formatting so you can follow the logic seamlessly.
4.  **🏆 Golden Questions:** Past exam questions (from 2017 to 2024) mapped directly into the notes, showing you precisely how the theory you just read will be tested.
5.  **⚡ Exam Tips:** Insider warnings about common pitfalls, calculation traps, and the specific keywords examiners demand for full marks.

## 🗂️ The Curriculum Phases
The curriculum is divided into 11 distinct phases, consisting of 55 detailed markdown files. Navigate through them sequentially using the interactive links at the top and bottom of each page:

*   [**Phase 01:** Chemical Kinetics](index.md) 
*   [**Phase 02:** Chemical Equilibrium](index.md)
*   [**Phase 03:** Chemical Bonding](index.md)
*   [**Phase 04:** Colligative Properties](index.md)
*   [**Phase 05:** Atomic Structure](index.md)
*   [**Phase 06:** Thermochemistry](index.md)
*   [**Phase 07:** Electrochemistry](index.md)
*   [**Phase 08:** Solutions](index.md)
*   [**Phase 09:** Periodic Table](index.md)
*   [**Phase 10:** Acid-Base & Buffer](index.md)
*   [**Phase 11:** Miscellaneous](index.md)

## 🚀 How to Use This Directory
1. Open the [Index](index.md) and select the topic you wish to study.
2. Read the Core Theory carefully.
3. Attempt the "Golden Questions" at the bottom of the page before checking the provided answers.
4. Note the "Exam Tips" to ensure you don't lose silly marks on technicalities.
5. Click `[Next ➡]` at the bottom of the page to proceed to the next topic.
""",

    "PreviousYearQuestions": """# 📜 Previous Year Questions (PYQ)
> **The Raw Archive of Past University Exam Papers**

Welcome to the `PreviousYearQuestions` directory. This folder houses the actual, raw exam question papers from previous university semesters spanning from 2017 to 2024.

## 🎯 Purpose & Significance
Analyzing past exam questions is arguably the most critical step in university exam preparation. Reviewing the files in this directory will allow you to:
1.  **Understand the Exam Format:** Familiarize yourself with the structure of the exam (e.g., number of questions, required alternatives, total marks).
2.  **Identify High-Frequency Topics:** Spot trends in which topics the professors test year after year (e.g., the Nernst Equation, Buffer Action).
3.  **Simulate Real Exam Conditions:** Use these raw question files to take timed, full-length mock exams.

## 🔗 Related Resources
*   **Need the Answers?** If you want to grade your mock exam chronologically, navigate to the [`../answers/`](../answers/README.md) directory, which contains full solutions matching these specific years.
*   **Studying by Topic?** If you don't want to take a full mock exam but instead want to see how a specific *topic* has been tested over the years, navigate to the [`../Topicwise-Answers/`](../Topicwise-Answers/README.md) directory.

Use the [Index](index.md) to navigate through the available exam years.
""",

    "answers": """# ✅ Past Exam Answers (Chronological)
> **Comprehensive, Year-by-Year Solutions to Past University Exams**

Welcome to the `answers` directory. This folder contains detailed, chronological solutions to the past university exam papers found in the `PreviousYearQuestions` directory.

## 🎯 Purpose & Significance
These files serve as the foundational data source for the "Golden Questions" section integrated within the master `boss_notes`. They are organized year-by-year (e.g., `2017.md`, `2021.md`).

**When to use this directory:**
This directory is most useful during the final stages of your exam preparation. When you sit down to take a full, timed mock exam using a paper from `PreviousYearQuestions`, you will come to this directory afterward to grade yourself.

*   If you are trying to study *conceptually*, you should use the [`../boss_notes/`](../boss_notes/README.md) instead, where these answers have been integrated pedagogically alongside the theory.
*   If you are trying to drill questions for a specific topic (e.g., only Electrochemistry questions), use the [`../Topicwise-Answers/`](../Topicwise-Answers/README.md) directory.

Use the [Index](index.md) to navigate through the solutions by year.
""",

    "Topicwise-Answers": """# 🧩 Topic-Wise Exam Answers
> **Past Exam Questions and Solutions Categorized strictly by Curriculum Topic**

Welcome to the `Topicwise-Answers` directory. Unlike the `answers/` directory, which sorts solutions chronologically by year, this folder compiles all historical exam questions (2017–2024) into specific topical categories.

## 🎯 Purpose & Strategy
This directory is designed for **targeted practice and active recall**. 

When studying for a final exam, jumping between completely unrelated topics in a chronological past paper can be jarring if you haven't mastered the entire curriculum yet. This folder allows you to hyper-focus your practice.

**How to use this directory:**
1.  Study a specific phase in the [`../boss_notes/`](../boss_notes/README.md) (for example, Phase 01: Chemical Kinetics).
2.  Once you feel confident in the theory, navigate to this directory and open `01-Chemical-Kinetics.md`.
3.  You will be presented with every single question the university has asked about Chemical Kinetics over the last 7 years, all in one place.
4.  Test yourself aggressively to ensure you have mastered the topic from every angle the examiners can throw at you.

Use the [Index](index.md) to select a topic and begin practicing.
""",

    "ClassTestQuestions": """# 📝 Class Test Questions
> **Archive of Mid-Semester Assessments and Quizzes**

Welcome to the `ClassTestQuestions` directory. This folder archives the smaller, mid-semester tests administered throughout the academic term.

## 🎯 Purpose & Strategy
Do not underestimate the importance of class tests. While previous year questions (PYQs) show historical trends, class tests reveal the **current priorities** of your specific professors.

**Why these matter:**
1.  **Foreshadowing:** The specific concepts, numerical values, and derivations heavily emphasized in these class tests frequently reappear on the final exam.
2.  **Identifying Blind Spots:** Class tests often feature trickier, more specific phrasing than broad final exam questions.
3.  **Pacing:** They are excellent for quick, low-stakes practice sessions.

Review these tests carefully and ensure you understand the solutions to any questions you got wrong during the semester. Use the [Index](index.md) to navigate through the tests.
""",

    "ResourcesGivenByTeachers": """# 📚 Instructor Resources
> **The Raw Educational Materials Provided by the University Professors**

Welcome to the `ResourcesGivenByTeachers` directory. This is the foundational data layer of the entire repository.

## 🎯 Purpose & Context
This folder contains the digitized, transcribed versions of the original lecture slides, textbooks, and class handouts provided by the instructors during the course. 

The content here is broken down into specific sub-directories based on the major curriculum topics (e.g., `Chemical-Kinetics`, `Thermochemistry`).

**How this relates to the rest of the repository:**
1.  **The Raw Material:** This directory contains the raw facts exactly as the professors presented them.
2.  **The Refined Product:** The [`../boss_notes/`](../boss_notes/README.md) directory took these raw materials and fully synthesized them into an optimized, highly pedagogical, exam-ready format.

While you should primarily study from the `boss_notes`, these original resources are preserved here for historical reference. If you ever need to deep-dive into a topic exactly as it was originally taught, or if you need to double-check a specific diagram from the professor's slides, this is where you look.

Use the sub-directories below to explore the raw materials.
"""
}

# Write specific READMEs for main directories
for folder, content in readmes.items():
    readme_path = os.path.join(workspace, folder, "README.md")
    if os.path.exists(os.path.join(workspace, folder)):
        with open(readme_path, "w") as f:
            f.write(content)
        print(f"✅ Generated Detailed README for {folder}")

# Handle subdirectories in ResourcesGivenByTeachers
resources_dir = os.path.join(workspace, "ResourcesGivenByTeachers")
if os.path.exists(resources_dir):
    subdirs = [d for d in os.listdir(resources_dir) if os.path.isdir(os.path.join(resources_dir, d))]
    for sub in subdirs:
        readme_path = os.path.join(resources_dir, sub, "README.md")
        topic_name = sub.replace("-", " ")
        content = f"""# 📂 {topic_name} - Raw Resources
> **Digitized Lecture Slides and Materials Provided by the Instructor**

Welcome to the `{sub}` resource directory.

## 🎯 Purpose & Content
This folder contains the raw, transcribed lecture slides and supplementary notes specifically covering **{topic_name}**. 

These materials have been carefully digitized from their original PDF or PowerPoint formats. The primary goal of this digitization is to preserve the exact wording, specific numerical examples, and instructional diagrams exactly as provided by your professors.

**Important Note for Studying:**
While these files contain the original source truth, they are unoptimized. They may contain repetitive information or lack pedagogical structure. 

If you are actively studying for the final exam, it is highly recommended that you use the **[`../../boss_notes/`](../../boss_notes/README.md)** directory instead. The `boss_notes` contain this exact same information, but it has been fully synthesized, formatted with LaTeX, and integrated with past exam questions to maximize your study efficiency.

Use the [Index](index.md) below to navigate through the individual slide files in this directory.
"""
        with open(readme_path, "w") as f:
            f.write(content)
        print(f"✅ Generated Detailed README for ResourcesGivenByTeachers/{sub}")

print("\nAll highly detailed README files generated successfully!")
