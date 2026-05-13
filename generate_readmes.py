import os

workspace = "/home/azaz/AntigravityData/Chemistry-Semester-Final"

readmes = {
    ".": """# Chemistry Semester Final Repository
> A comprehensive, digital master study guide and resource repository for the Chemistry Semester Final Exam.

This repository contains all materials required to ace the Chemistry exam, ranging from raw lecture slides to fully synthesized, high-fidelity "Boss Notes".

## 📂 Repository Structure

*   [**boss_notes/**](boss_notes/README.md) - The master, exam-ready study guide. This is the fully synthesized, pedagogical core of the repository.
*   [**PreviousYearQuestions/**](PreviousYearQuestions/README.md) - Archive of past university exam questions (2017–2024).
*   [**answers/**](answers/README.md) - Detailed, year-by-year solutions to the past exam questions.
*   [**Topicwise-Answers/**](Topicwise-Answers/README.md) - Exam questions and answers strategically sorted by specific curriculum topics.
*   [**ClassTestQuestions/**](ClassTestQuestions/README.md) - Archive of questions from mid-semester class tests.
*   [**ResourcesGivenByTeachers/**](ResourcesGivenByTeachers/README.md) - Raw digital assets including lecture slides, textbook PDFs, and class handouts.

---
*This repository is automatically indexed and features interactive navigation between study files.*
""",

    "boss_notes": """# Boss Notes
> The definitive, high-fidelity master study guide for the Chemistry Semester Final.

## 🎯 Purpose
The `boss_notes` directory is the crown jewel of this repository. It contains 55 fully synthesized markdown notes covering 11 phases of the curriculum. 

Instead of raw slides or unstructured text, these notes have been meticulously processed to include:
1.  **Synthesized Core Theory:** Clear, pedagogical explanations bridging raw facts with deep understanding.
2.  **Key Derivations:** Step-by-step mathematical proofs with rigorous LaTeX formatting.
3.  **Golden Questions:** Direct integration of past exam questions mapped to the exact concept.
4.  **Exam Tips:** Insider warnings about common pitfalls and specific keywords examiners look for.

Use the [Index](index.md) to navigate through the topics seamlessly.
""",

    "answers": """# Past Exam Answers (Year-by-Year)
> Comprehensive solutions to past university exam questions.

## 🎯 Purpose
This directory contains the year-by-year breakdown of answers to past exam papers (e.g., `2017.md`, `2018.md`). These files serve as the raw data source for the "Golden Questions" section in the `boss_notes`.

If you are practicing a specific past paper and need to check your answers sequentially, use the files in this directory.

Use the [Index](index.md) to navigate through the years.
""",

    "PreviousYearQuestions": """# Previous Year Questions (PYQ)
> The raw archive of past university exam papers.

## 🎯 Purpose
This directory contains the actual exam questions from previous years (2017–2024). Reviewing these files is critical for understanding the exam format, question distribution, and the frequency of specific topics.

For the detailed solutions to these questions, refer to the `answers/` or `Topicwise-Answers/` directories.

Use the [Index](index.md) to navigate through the exams.
""",

    "ClassTestQuestions": """# Class Test Questions
> Archive of mid-semester class assessments and quizzes.

## 🎯 Purpose
This directory contains questions from various class tests. These are highly valuable for identifying what specific concepts the instructors emphasized during the semester, which often strongly hints at what will appear on the final exam.

Use the [Index](index.md) to navigate through the tests.
""",

    "Topicwise-Answers": """# Topic-Wise Exam Answers
> Past exam questions and solutions categorized by curriculum topic.

## 🎯 Purpose
Unlike the `answers/` directory (which sorts by year), this directory compiles all historical exam questions regarding a single topic into one place. 

If you just finished studying "Chemical Kinetics" in the `boss_notes` and want to test yourself on every kinetics question asked between 2017 and 2024, this is the directory to use.

Use the [Index](index.md) to navigate through the topics.
""",

    "ResourcesGivenByTeachers": """# Instructor Resources
> The raw educational materials provided by the university professors.

## 🎯 Purpose
This directory acts as the foundational data layer of the repository. It contains the original, raw lecture slides, textbooks, and handouts provided during the course, organized by topic. 

While the `boss_notes` provide the synthesized, exam-ready version of this content, these original resources are kept here for historical reference and deep-dive reading.

### Sub-Directories
Each sub-directory corresponds to a major topic (e.g., `Chemical-Kinetics`, `Thermochemistry`) and contains the digitized lecture slides for that topic.
"""
}

# Write specific READMEs
for folder, content in readmes.items():
    readme_path = os.path.join(workspace, folder, "README.md")
    with open(readme_path, "w") as f:
        f.write(content)
    print(f"✅ Created README for {folder}")

# Handle subdirectories in ResourcesGivenByTeachers
resources_dir = os.path.join(workspace, "ResourcesGivenByTeachers")
if os.path.exists(resources_dir):
    subdirs = [d for d in os.listdir(resources_dir) if os.path.isdir(os.path.join(resources_dir, d))]
    for sub in subdirs:
        readme_path = os.path.join(resources_dir, sub, "README.md")
        topic_name = sub.replace("-", " ")
        content = f"""# {topic_name} - Raw Resources
> Digitized lecture slides and materials provided by the instructor for {topic_name}.

## 🎯 Purpose
This folder contains the transcribed, raw lecture slides and notes for {topic_name}. These materials have been digitized from their original PDF/PPT formats to preserve the exact wording and diagrams provided by the teachers.

For the optimized, exam-ready study guide based on this material, please refer to the `boss_notes/` directory.

Use the [Index](index.md) to navigate through the individual slide/resource files.
"""
        with open(readme_path, "w") as f:
            f.write(content)
        print(f"✅ Created README for ResourcesGivenByTeachers/{sub}")

print("\nAll README files generated successfully!")
