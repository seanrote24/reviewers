import random

ALL_QUESTIONS = [
    {
        "q": "What is the primary role of governments in science and technology?",
        "opts": [
            "To only fund military research",
            "To directly support scientific and technical research",
            "To limit access to scientific knowledge",
            "To privatize all research institutions"
        ],
        "a": 1,
        "exp": "Governments in many countries directly support scientific and technical research."
    },
    {
        "q": "Who carries the primary responsibility for funding fundamental research in science and technology?",
        "opts": [
            "Private corporations",
            "International organizations",
            "The federal government",
            "Non-government organizations"
        ],
        "a": 2,
        "exp": "The federal government carries the primary responsibility for funding fundamental research in science and technology."
    },
    {
        "q": "What is a critical role of institutions and facilities supported by the federal government?",
        "opts": [
            "Selling research results to private companies",
            "Educating and training the next generation of scientists and engineers",
            "Replacing private industries in research",
            "Reducing the number of scientists"
        ],
        "a": 1,
        "exp": "Institutions supported by the federal government play a critical role in educating and training the next generation of scientists and engineers."
    },
    {
        "q": "Why is fundamental research of current concern according to the slides?",
        "opts": [
            "Because of cutbacks by the Department of Defense and Industry central laboratories",
            "Because private companies are funding too much research",
            "Because there are too many scientists",
            "Because technology is advancing too quickly"
        ],
        "a": 0,
        "exp": "Fundamental research is of current concern because of cutbacks by the Department of Defense and Industry central laboratories in some fields."
    },
    {
        "q": "What does Science and Technology policy cover?",
        "opts": [
            "Only private sector research funding",
            "Public sector measures for the creation, funding, support, and mobilization of S&T resources",
            "Only military and defense technologies",
            "Only international science agreements"
        ],
        "a": 1,
        "exp": "S&T policy covers the public sector measures designed for the creation, funding, support, and mobilization of scientific and technological resources."
    },
    {
        "q": "What is the broad government policy objective for Science and Technology?",
        "opts": [
            "To limit science to academic institutions only",
            "To embed S&T as part of the culture of key sectors to promote competitiveness in quality goods and services",
            "To privatize all scientific research",
            "To focus only on military technology"
        ],
        "a": 1,
        "exp": "The broad government policy objective is to embed Science and Technology as part of the culture of key sectors to promote competitiveness in the production of a wider range of quality goods and services."
    },
    {
        "q": "What is Republic Act 2067 about?",
        "opts": [
            "An act creating the Sandiganbayan court",
            "An act to integrate, coordinate, and intensify scientific and technological research and development, and foster invention",
            "An act establishing the NCRP",
            "An act regulating pharmaceutical companies"
        ],
        "a": 1,
        "exp": "RA 2067 is an act to integrate, coordinate, and intensify scientific and technological research and development and to foster invention, providing funds for these purposes."
    },
    {
        "q": "What is the significance of Republic Act 2067 in Philippine history?",
        "opts": [
            "It created the Sandiganbayan",
            "It abolished government funding for science",
            "It started the government's strong support for science and technology in the Philippines",
            "It established the Department of Science and Technology"
        ],
        "a": 2,
        "exp": "RA 2067 is basically the law that started the government's strong support for science and technology in the Philippines—helping scientists, funding research, and creating agencies that still exist today."
    },
    {
        "q": "What did Republic Act 1606 create?",
        "opts": [
            "The Department of Science and Technology",
            "The National Research Council of the Philippines",
            "A special court (Sandiganbayan) to try corruption cases involving government officials",
            "The Food and Drug Administration"
        ],
        "a": 2,
        "exp": "RA 1606 created a special court (Sandiganbayan) whose main job is to try and decide corruption cases involving government officials."
    },
    {
        "q": "What is the full name of the NCRP?",
        "opts": [
            "National Center for Research and Planning",
            "National Council for Research Promotion",
            "National Research Council of the Philippines",
            "National Committee for Research Programs"
        ],
        "a": 2,
        "exp": "NCRP stands for the National Research Council of the Philippines."
    },
    {
        "q": "When was the NCRP established?",
        "opts": [
            "1901",
            "1946",
            "1933",
            "1987"
        ],
        "a": 2,
        "exp": "The NCRP was established in 1933 during the American period."
    },
    {
        "q": "Under which government department does the NCRP currently operate?",
        "opts": [
            "Department of Education (DepEd)",
            "Department of Science and Technology (DOST)",
            "Department of Interior and Local Government (DILG)",
            "Department of Health (DOH)"
        ],
        "a": 1,
        "exp": "The NCRP now operates under the Department of Science and Technology (DOST)."
    },
    {
        "q": "What was the original aim of the NCRP when it was established?",
        "opts": [
            "To regulate drug manufacturing firms",
            "To bring together Filipino researchers and scholars",
            "To oversee government corruption cases",
            "To manage Philippine trade with ASEAN"
        ],
        "a": 1,
        "exp": "The NCRP was originally aimed to bring together Filipino researchers and scholars."
    },
    {
        "q": "Which of the following is a function of the NCRP?",
        "opts": [
            "Providing funding and grants for research projects",
            "Creating laws without congressional approval",
            "Managing government corruption cases",
            "Regulating private businesses"
        ],
        "a": 0,
        "exp": "The NCRP provides funding and grants for research projects, among its many functions."
    },
    {
        "q": "What makes the NCRP unique compared to other agencies?",
        "opts": [
            "It only covers scientific fields",
            "It covers both scientific and non-scientific fields",
            "It only focuses on applied research",
            "It only operates in Metro Manila"
        ],
        "a": 1,
        "exp": "Unlike other agencies, NCRP covers both scientific and non-scientific fields (science, health, social sciences, humanities, etc.)."
    },
    {
        "q": "What type of research does the NCRP focus on?",
        "opts": [
            "Only military research",
            "Basic research — knowledge for understanding, not just application",
            "Only commercial product development",
            "Only agricultural research"
        ],
        "a": 1,
        "exp": "NCRP focuses on basic research — knowledge for understanding, not just application."
    },
    {
        "q": "Which cluster of NCRP policies deals with Social Sciences, Humanities, Education, International Policies, and Governance?",
        "opts": [
            "Cluster 2",
            "Cluster 3",
            "Cluster 4",
            "Cluster 1"
        ],
        "a": 3,
        "exp": "Cluster 1 covers Social Sciences, Humanities, Education, International Policies, and Governance."
    },
    {
        "q": "Which NCRP cluster covers Physics Engineering, Earth and Space Science, and Mathematics?",
        "opts": [
            "Cluster 1",
            "Cluster 2",
            "Cluster 3",
            "Cluster 4"
        ],
        "a": 1,
        "exp": "Cluster 2 covers Physics Engineering, and Industrial Research, Earth and Space Science, and Mathematics."
    },
    {
        "q": "Which NCRP cluster covers Medical, Chemical, and Pharmaceutical Sciences?",
        "opts": [
            "Cluster 1",
            "Cluster 2",
            "Cluster 3",
            "Cluster 4"
        ],
        "a": 2,
        "exp": "Cluster 3 covers Medical, Chemical, and Pharmaceutical Sciences."
    },
    {
        "q": "Which NCRP cluster covers Biological Sciences, Agriculture, and Forestry?",
        "opts": [
            "Cluster 1",
            "Cluster 2",
            "Cluster 3",
            "Cluster 4"
        ],
        "a": 3,
        "exp": "Cluster 4 covers Biological Sciences, Agriculture, and Forestry."
    },
    {
        "q": "What is the goal of the Social Sciences and Education cluster policy?",
        "opts": [
            "To promote military readiness",
            "To prepare the country and its people to meet the demands of a technologically driven world",
            "To limit education to urban areas",
            "To reduce the number of universities"
        ],
        "a": 1,
        "exp": "The goal is to prepare the whole country and its people to meet the demands of a technologically driven world and capacitate the people to live in a world driven by science."
    },
    {
        "q": "What does the Medical, Chemical, and Pharmaceutical Sciences cluster aim to ensure?",
        "opts": [
            "Free medicine for all citizens",
            "Compliance of drug-manufacturing firms with ASEAN-harmonized standards through full FDA implementation",
            "Privatization of all pharmaceutical companies",
            "Elimination of generic medicine"
        ],
        "a": 1,
        "exp": "This cluster aims to ensure compliance of drug-manufacturing firms with ASEAN-harmonized standards by full implementation of FDA."
    },
    {
        "q": "What does the Biological Sciences, Agriculture, and Forestry cluster promote?",
        "opts": [
            "Unlimited logging and mining",
            "Protecting and conserving biodiversity by full implementation of existing laws",
            "Replacing all traditional farming with industrial agriculture",
            "Reducing forest areas for development"
        ],
        "a": 1,
        "exp": "This cluster promotes protecting and conserving biodiversity by full implementation of existing laws."
    },
    {
        "q": "What is the Basic Research Cluster focused on?",
        "opts": [
            "Turning research into commercial products",
            "Knowledge for understanding—research to explain natural or social phenomena without immediate practical use",
            "Creating government policies only",
            "Solving immediate industrial problems"
        ],
        "a": 1,
        "exp": "The Basic Research Cluster focuses on knowledge for understanding—research that aims to explain natural or social phenomena without immediate practical use."
    },
    {
        "q": "Which of the following is an example of Basic Research?",
        "opts": [
            "Developing drought-resistant crops",
            "Designing affordable medical equipment",
            "Studying climate patterns in the Philippines",
            "Creating mobile apps for education"
        ],
        "a": 2,
        "exp": "Studying climate patterns in the Philippines is an example of basic research — seeking understanding without immediate practical application."
    },
    {
        "q": "What does the Applied Research Cluster do?",
        "opts": [
            "Focuses only on theoretical studies",
            "Uses knowledge from basic research to solve real-world problems",
            "Creates policies for the government",
            "Designs commercial products for export"
        ],
        "a": 1,
        "exp": "The Applied Research Cluster uses knowledge from basic research to solve real-world problems."
    },
    {
        "q": "Which of the following is an example of Applied Research?",
        "opts": [
            "Theoretical studies in physics",
            "Research on Filipino culture and identity",
            "Developing drought-resistant crops",
            "Studies on poverty reduction strategies"
        ],
        "a": 2,
        "exp": "Developing drought-resistant crops is an example of applied research — using scientific knowledge to solve a real-world problem."
    },
    {
        "q": "What does the Development Research Cluster focus on?",
        "opts": [
            "Basic theoretical knowledge",
            "Turning research into usable products, technologies, or systems",
            "Creating government laws",
            "Studying social phenomena only"
        ],
        "a": 1,
        "exp": "The Development Research Cluster focuses on turning research into usable products, technologies, or systems."
    },
    {
        "q": "Which of the following is an example under the Development Research Cluster?",
        "opts": [
            "Studying climate patterns",
            "Research on Filipino culture",
            "Creating mobile apps for education",
            "Analyzing poverty reduction strategies"
        ],
        "a": 2,
        "exp": "Creating mobile apps for education is an example of development research — turning research into a usable technology."
    },
    {
        "q": "What is the role of the Policy Research Center?",
        "opts": [
            "To conduct military research",
            "To provide research-based recommendations to guide government decisions and policies",
            "To replace the legislature in making laws",
            "To fund private business ventures"
        ],
        "a": 1,
        "exp": "The Policy Research Center provides research-based recommendations to guide government decisions and policies."
    },
    {
        "q": "Which of the following is an example under the Policy Research Center?",
        "opts": [
            "Designing affordable medical equipment",
            "Developing drought-resistant crops",
            "Studies on poverty reduction strategies",
            "Studying climate patterns"
        ],
        "a": 2,
        "exp": "Studies on poverty reduction strategies are an example of policy research, guiding government decisions with evidence."
    },
    {
        "q": "How does the NCRP contribute to governance?",
        "opts": [
            "By replacing elected officials",
            "By contributing to evidence-based policies and development",
            "By enforcing laws directly",
            "By managing government funds independently"
        ],
        "a": 1,
        "exp": "The NCRP contributes to evidence-based policies and development, strengthening the country's intellectual and scientific community."
    },
    {
        "q": "What did the Physics Engineering cluster do in response to the ASEAN 2015 agenda?",
        "opts": [
            "It reduced funding for local engineers",
            "DOST sought the expertise of NCRP to consult sectors on how the Philippines can prepare for ASEAN 2015",
            "It privatized all engineering research",
            "It eliminated math from the curriculum"
        ],
        "a": 1,
        "exp": "In response to ASEAN 2015, the government particularly the DOST, sought the expertise of the NCRP to consult various sectors on how the Philippines can prepare for the ASEAN 2015 agenda."
    },
    {
        "q": "What does the Social Sciences cluster emphasize in basic education?",
        "opts": [
            "Teaching only in English",
            "Integrating ASEAN awareness and emphasizing teaching in the Mother Tongue",
            "Reducing science subjects",
            "Eliminating ICT in schools"
        ],
        "a": 1,
        "exp": "The cluster emphasizes integrating ASEAN awareness in basic education and emphasizing teaching Education in the Mother Tongue."
    },
    {
        "q": "What type of court did Republic Act 1606 establish, and what is its main function?",
        "opts": [
            "A family court for civil cases",
            "A special court (Sandiganbayan) to try corruption cases involving government officials",
            "A patent court for inventors",
            "A science tribunal for research disputes"
        ],
        "a": 1,
        "exp": "RA 1606 created the Sandiganbayan, a special court whose main job is to try and decide corruption cases involving government officials, helping keep the government clean and accountable."
    },
]


def shuffle_options(question):
    """Shuffle answer options and update the correct answer index."""
    indices = list(range(len(question["opts"])))
    random.shuffle(indices)
    new_opts = [question["opts"][i] for i in indices]
    new_answer = indices.index(question["a"])
    return {**question, "opts": new_opts, "a": new_answer}


def get_grade(score, total):
    pct = score / total * 100
    if pct == 100:
        return "PERFECT! Outstanding mastery of Government Policies and Laws of STS!"
    elif pct >= 80:
        return "EXCELLENT! You have a strong grasp of the material."
    elif pct >= 60:
        return "GOOD JOB! Review a few more topics and you'll master this."
    else:
        return "KEEP REVIEWING! Go through the slides again and try once more."


def print_separator(char="-", length=60):
    print(char * length)


def run_quiz():
    print_separator("=")
    print("  GOVERNMENT POLICIES AND LAWS OF STS REVIEWER")
    print("  Science, Technology, and Nation Building")
    print_separator("=")
    print(f"  Total questions: {len(ALL_QUESTIONS)}")
    print("  Questions and choices shuffle every attempt!")
    print_separator("=")
    print()

    while True:
        questions = random.sample(ALL_QUESTIONS, len(ALL_QUESTIONS))
        questions = [shuffle_options(q) for q in questions]

        score = 0
        wrong_items = []

        for i, q in enumerate(questions, 1):
            print_separator()
            print(f"Question {i} of {len(questions)}")
            print_separator()
            print(f"\n{q['q']}\n")

            labels = ["A", "B", "C", "D"]
            for j, opt in enumerate(q["opts"]):
                print(f"  {labels[j]}. {opt}")

            print()

            while True:
                answer = input("Your answer (A/B/C/D): ").strip().upper()
                if answer in labels:
                    break
                print("  Please enter A, B, C, or D only.")

            chosen_index = labels.index(answer)

            if chosen_index == q["a"]:
                score += 1
                print("\n  ✓ CORRECT!\n")
            else:
                correct_label = labels[q["a"]]
                print(f"\n  ✗ WRONG! Correct answer: {correct_label}. {q['opts'][q['a']]}")
                wrong_items.append({
                    "question": q["q"],
                    "your_answer": f"{answer}. {q['opts'][chosen_index]}",
                    "correct_answer": f"{correct_label}. {q['opts'][q['a']]}",
                    "explanation": q["exp"]
                })
                print()

            print(f"  Explanation: {q['exp']}")
            print()

        print_separator("=")
        print("                     QUIZ COMPLETE!")
        print_separator("=")
        pct = round(score / len(questions) * 100)
        print(f"\n  FINAL SCORE: {score} / {len(questions)}  ({pct}%)\n")
        print(f"  {get_grade(score, len(questions))}")
        print()

        if wrong_items:
            print_separator("-")
            print(f"  Items to review ({len(wrong_items)} missed):")
            print_separator("-")
            for idx, item in enumerate(wrong_items, 1):
                print(f"\n  {idx}. {item['question']}")
                print(f"     Your answer   : {item['your_answer']}")
                print(f"     Correct answer: {item['correct_answer']}")
                print(f"     Note          : {item['explanation']}")
            print()

        print_separator("=")
        again = input("Review again with shuffled questions? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print()
            print("  Good luck on your exam! Keep studying!")
            print_separator("=")
            break
        print()


if __name__ == "__main__":
    run_quiz()