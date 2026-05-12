import os
import re

BASE_DIR = "/home/azaz/AntigravityData/Chemistry-Semester-Final"
BOSS_DIR = os.path.join(BASE_DIR, "boss_notes")
ANSWERS_DIR = os.path.join(BASE_DIR, "answers")

os.makedirs(BOSS_DIR, exist_ok=True)

# ─── Mappings ───
phases = {
    "01": {"topic": "Chemical Kinetics", "priority": "🔴 CRITICAL", "files": {
        "01.1_Rate_and_Rate_Law.md": ["2020 Q.4(a)", "2018 Q4(a)", "2018 Q5(a)", "ClassTests Q.1 Define rate"],
        "01.2_Order_and_Molecularity.md": ["2024 Q.5(a)", "2021 Q.2(a)", "2023 Q.7(c)", "2018 Q5(b)", "2020 Q.4(c)", "2021 Q.2(b)", "2017 Q5(b)", "ClassTests Q.2 Distinguish"],
        "01.3_First_Order_Reactions.md": ["2024 Q.5(b)", "2024 Q.5(c)", "2023 Q.7(a)", "2023 Q.7(b)", "2018 Q5(c)", "2019 Q.6(b)", "ClassTests Q.3 Derive", "ClassTests Q.4 Show"],
        "01.4_Second_Order_Reactions.md": ["2020 Q.4(b)", "2019 Q.6(a)", "2018 Q4(a)", "2017 Q5(a)"],
        "01.5_Methods_of_Order_Determination.md": [],
        "01.6_Temperature_and_Arrhenius.md": ["2017 Q5(c)", "ClassTests Q.1"],  # Note: CT03 Q1 was "Define rate... temperature effect"
        "01.7_Activated_Complex_Theory.md": ["2018 Q4(b)"]
    }},
    "02": {"topic": "Chemical Equilibrium", "priority": "🔴 CRITICAL", "files": {
        "02.1_Reversible_Reactions.md": ["2020 Q.3(c)", "2023 Q.8(c)", "2019 Q.6(c)", "2024 Q.6(a)", "2021 Q.4(c)", "2017 Q8(a)", "2017 Q8(c)"],
        "02.2_Law_of_Mass_Action.md": ["2024 Q.6(b)", "2023 Q.8(b)", "2018 Q6(a)", "2020 Q.3(a)"],
        "02.3_Equilibrium_Constant_Derivations.md": ["2024 Q.6(c)", "2018 Q3(a)", "2018 Q3(b)", "2017 Q8(b)"],
        "02.4_Le_Chatelier_Principle.md": ["2023 Q.8(a)", "2021 Q.2(c)", "2020 Q.3(b)"],
        "02.5_Gibbs_Free_Energy.md": ["2019 Q.4(a)", "2018 Q6(b)"],
        "02.6_Equilibrium_Numericals.md": ["2019 Q.4(b)", "2018 Q6(c)"]
    }},
    "03": {"topic": "Chemical Bonding", "priority": "🔴 CRITICAL", "files": {
        "03.1_Types_of_Chemical_Bonds.md": ["2024 Q.1(a)", "2019 Q.2(a)", "2021 Q.8(a)", "2020 Q.8(a)", "2017 Q1(a)"],
        "03.2_Ionic_vs_Covalent_Properties.md": ["2024 Q.1(b)", "2020 Q.8(c)", "2019 Q.2(b)", "2017 Q1(b)"],
        "03.3_Intermolecular_Forces.md": ["ClassTests 1. Explain different"],
        "03.4_Sigma_Pi_Bonds_and_Hybridization.md": ["2018 Q2(a)", "2021 Q.8(b)"],
        "03.5_Molecular_Orbital_Theory.md": ["2024 Q.3(a)", "2023 Q.3(a)"],
        "03.6_MO_Diagrams_Specific_Molecules.md": ["2024 Q.3(b)", "2023 Q.3(b)", "2023 Q.3(c)", "ClassTests 2. .*N_2.*diamagnetic"],
        "03.7_Metallic_Bond_and_Band_Theory.md": ["2019 Q.2(c)", "2021 Q.8(c)", "2018 Q2(b)", "2017 Q1(c)"]
    }},
    "04": {"topic": "Colligative Properties", "priority": "🟠 HIGH", "files": {
        "04.1_Vapor_Pressure_Lowering.md": ["2019 Q.5(a)", "2019 Q.5(b)", "2019 Q.5(c)", "2023 Q.6(b)"],
        "04.2_Boiling_Point_Elevation.md": [],
        "04.3_Freezing_Point_Depression.md": [],
        "04.4_Osmotic_Pressure.md": ["2023 Q.6(a)", "2023 Q.6(c)", "2021 Q.3(a)", "2021 Q.3(b)", "2021 Q.3(c)", "2020 Q.2(a)", "2020 Q.2(b)", "2020 Q.2(c)", "2019 Q.7(a)", "2019 Q.7(b)", "2019 Q.7(c)", "2018 \\(b\\) Osmotic pressure"],
        "04.5_Abnormal_Colligative_Properties.md": []
    }},
    "05": {"topic": "Atomic Structure", "priority": "🟠 HIGH", "files": {
        "05.1_Atomic_Models.md": ["2023 Q.1(a)", "2020 Q.6(a)", "2019 Q.1(b)"],
        "05.2_Quantum_Numbers.md": ["2023 Q.2(a)", "2023 Q.2(b)", "2021 Q.5(b)", "2018 \\(b\\) Magnetic quantum"],
        "05.3_Electronic_Configuration_Rules.md": ["2018 \\(c\\) Hund"],
        "05.4_Atomic_Spectra.md": ["2023 Q.1(c)", "2021 Q.5(a)", "2020 Q.6(b)", "2020 Q.6(c)", "2019 Q.1(a)"],
        "05.5_Wave_Mechanics.md": ["2021 Q.5(c)", "2018 Q1 Short.*\\(a\\)"],
        "05.6_Orbit_vs_Orbital.md": ["2023 Q.1(b)"]
    }},
    "06": {"topic": "Thermochemistry", "priority": "🟠 HIGH", "files": {
        "06.1_Laws_of_Thermochemistry.md": ["2024 Q.4(a)", "2017 Q4 Write.*\\(a\\) Laws"],
        "06.2_Types_of_Heat_of_Reaction.md": ["2024 Q.4(b)", "2023 Q.4(a)", "2021 Q.7(a)", "2021 Q.7(c)", "2020 Q.5(a)", "2019 Q.8(b)"],
        "06.3_Enthalpy_Derivation.md": ["2017 Q2(b)", "2020 Q.5(b)"],
        "06.4_Kirchhoffs_Equation.md": ["2017 Q2(a)", "2021 Q.7(b)"],
        "06.5_Bomb_Calorimeter_and_Numericals.md": ["2023 Q.4(b)", "2023 Q.4(c)", "2024 Q.4(c)", "2017 Q2(c)", "2020 Q.5(c)"]
    }},
    "07": {"topic": "Electrochemistry", "priority": "🟠 HIGH", "files": {
        "07.1_Conductors_and_Electrolytes.md": ["2024 Q.7(a)", "2018 Q7(a)"],
        "07.2_Electrolytic_Conduction.md": ["2024 Q.7(b)", "2018 Q7(b)", "2020 Q.8(b)"],
        "07.3_Faradays_Laws.md": ["2021 Q.4(a)", "2019 Q.8(a)", "2019 Q.8(c)"],
        "07.4_Conductance_and_Kohlrausch.md": ["2017 Q6(a)", "ClassTests Q.1 Define molar", "ClassTests Q.2 State Kohlrausch"],
        "07.5_Electrochemical_Cells_and_Nernst.md": ["2024 Q.7(c)", "2018 Q7(c)"],
        "07.6_Debye_Huckel_Theory.md": ["2017 Q6(b)", "2017 Q6(c)", "2021 Q.4(b)"]  # CT04 Q1 is actually included in Kohlrausch
    }},
    "08": {"topic": "Solutions", "priority": "🟡 MEDIUM", "files": {
        "08.1_Solution_Definitions_and_Types.md": ["2024 Q.8(a)", "2021 Q.1(a)", "2020 Q.1(a)", "2017 Q7(a)", "2024 Q.8(c)", "2021 Q.1(c)", "ClassTests Q.1 Define the term", "ClassTests Q.5 Calculate"],
        "08.2_Henrys_Law.md": ["2021 Q.1(b)", "2020 Q.1(b)", "2017 Q7(b)", "ClassTests Q.2 State Henry"],
        "08.3_Ideal_vs_Non_Ideal_Solutions.md": ["ClassTests Q.3 Distinguish"],
        "08.4_Solubility_and_Temperature.md": ["2024 Q.8(b)", "2020 Q.1(c)", "2017 Q7(c)", "ClassTests Q.4 Discuss briefly"]
    }},
    "09": {"topic": "Periodic Table", "priority": "🟡 MEDIUM", "files": {
        "09.1_Modern_Periodic_Law.md": ["2024 Q.2(a)", "2020 Q.7(a)", "2017 Q3(a)", "2024 Q.2(b)", "2020 Q.7(b)", "2017 Q3(b)"],
        "09.2_Periodic_Properties.md": ["2017 Q4 Write.*\\(b\\) Electron"],
        "09.3_Ionization_Potential.md": ["2020 Q.7(c)", "2017 Q3(c)", "2021 Q.6(a)", "2021 Q.6(b)"],
        "09.4_Redox_from_Electronic_Config.md": ["2023 Q.2(c)", "2021 Q.6(c)"]
    }},
    "10": {"topic": "Acid-Base & Buffer", "priority": "🟡 MEDIUM", "files": {
        "10.1_Acid_Base_Theories.md": ["2019 Q.3(a)", "2017 Q4 Write.*\\(c\\) Lewis"],
        "10.2_pH_and_Ionic_Equilibrium.md": [],
        "10.3_Buffer_Solutions.md": ["2023 Q.5(a)", "2023 Q.5(b)", "2023 Q.5(c)", "2019 Q.3(b)", "2018 \\(c\\) Buffer solution"],
        "10.4_Precision_and_Accuracy.md": ["2019 Q.3(c)"]
    }},
    "11": {"topic": "Miscellaneous", "priority": "🟡 MEDIUM", "files": {
        "11.00_Miscellaneous.md": ["2018 \\(a\\) Crystal structure"]
    }}
}

# Read all answer files
all_answers = {}
answer_files = ["2024.md", "2023.md", "2021.md", "2020.md", "2019.md", "2018.md", "2017.md", "ClassTests.md"]
for fname in answer_files:
    path = os.path.join(ANSWERS_DIR, fname)
    with open(path, "r") as f:
        all_answers[fname] = f.read()

def extract_blocks(text, source_label):
    lines = text.split('\n')
    blocks = []
    current_header = None
    current_lines = []
    for line in lines:
        if re.match(r'^### ', line):
            if current_header:
                blocks.append({'header': current_header, 'content': '\n'.join(current_lines).strip(), 'source': source_label})
            current_header = line
            current_lines = [line]
        elif re.match(r'^## ', line):
            if current_header:
                blocks.append({'header': current_header, 'content': '\n'.join(current_lines).strip(), 'source': source_label})
            current_header = None
            current_lines = []
        elif current_header:
            current_lines.append(line)
    if current_header:
        blocks.append({'header': current_header, 'content': '\n'.join(current_lines).strip(), 'source': source_label})
    return blocks

all_blocks = {}
for fname in answer_files:
    label = fname.replace('.md', '')
    all_blocks[label] = extract_blocks(all_answers[fname], label)

def get_block(pattern_str):
    # Pattern is "Year Regex", e.g. "2020 Q.4(a)"
    parts = pattern_str.split(' ', 1)
    if len(parts) == 2:
        source, regex = parts
    else:
        source = "ClassTests"
        regex = pattern_str
        
    source = source.replace('.md', '')
    if source not in all_blocks:
        return None
    
    # Clean regex
    regex = regex.replace('(', r'\(').replace(')', r'\)').replace('.', r'\.')
    # Handle special custom regexes from earlier
    regex = regex.replace(r'\\(', r'\(').replace(r'\\)', r'\)') # fix double escapes
    
    # We want to match the header
    for block in all_blocks[source]:
        if re.search(regex, block['header']):
            return block
    return None

for phase_key, phase_data in phases.items():
    topic_name = phase_data["topic"]
    priority = phase_data["priority"]
    for filename, question_patterns in phase_data["files"].items():
        subtopic_title = filename.replace('.md', '').split('_', 1)[1].replace('_', ' ')
        
        content = f"""# {subtopic_title}
> **Topic:** {topic_name} | **Priority:** {priority} | **Exam Frequency:** ?/7 exams

## 📌 Quick Summary
> [TODO: A 3-5 line "elevator pitch" of the entire sub-topic.]

## 📖 Core Theory
[TODO: Detailed, exam-ready explanation with all definitions, laws, and principles]

## 🧮 Key Derivations & Equations
[TODO: Step-by-step derivations with full LaTeX, boxed final equations]

## 📊 Comparison Tables
[TODO: Clean tables for distinguish/compare questions, if applicable]

## 🔢 Solved Numericals
[TODO: Worked examples with Given → Find → Solution → Answer format]

## 🏆 Golden Questions (Past Exam Archive)
"""
        found_any = False
        for pattern in question_patterns:
            block = get_block(pattern)
            if block:
                found_any = True
                content += f"### 🎯 {block['source']} {block['header'].replace('### ', '')}\n"
                content += f"> **Source:** answers/{block['source']}.md\n\n"
                # The block['content'] already includes the header at the top, let's strip it
                content_lines = block['content'].split('\n')[1:]
                clean_content = '\n'.join(content_lines).strip()
                content += f"{clean_content}\n\n---\n\n"
            else:
                content += f"### 🎯 [MISSING MATCH] {pattern}\n\n---\n\n"
                
        if not found_any:
            content += "No direct past exam questions found — study the Core Theory.\n\n"
            
        content += """## ⚡ Exam Tips & Common Mistakes
[TODO: Pitfalls, shortcuts, and things examiners love to ask]

## 🔗 Related Sub-Topics
[TODO: Cross-references to other boss_notes files]
"""
        
        filepath = os.path.join(BOSS_DIR, filename)
        with open(filepath, "w") as f:
            f.write(content)
            
print("✅ setup complete")
