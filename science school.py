import random

ALL_QUESTIONS = [
    # Concept of Science Education
    {
        "q": "What does science education focus on?",
        "opts": [
            "Only memorizing scientific facts",
            "Teaching, learning, and understanding science",
            "Only laboratory experiments and fieldwork",
            "Only preparing students for college entrance exams"
        ],
        "a": 1,
        "exp": "Science education focuses on teaching, learning, and understanding science."
    },
    {
        "q": "What does teaching science involve?",
        "opts": [
            "Only conducting experiments",
            "Exploring pedagogical theories and models to help teachers teach scientific concepts and processes effectively",
            "Memorizing textbook content",
            "Only using technology in the classroom"
        ],
        "a": 1,
        "exp": "Teaching science involves exploring pedagogical theories and models to help teachers teach scientific concepts and processes effectively."
    },
    {
        "q": "What is the most interesting aspect of learning science according to the lesson?",
        "opts": [
            "Taking exams and quizzes",
            "Reading scientific journals",
            "Helping students understand and love science",
            "Memorizing the periodic table"
        ],
        "a": 2,
        "exp": "Learning science includes both pedagogy and the most interesting aspect — helping students understand and love science."
    },
    {
        "q": "What does 'understanding science' imply?",
        "opts": [
            "Passing all science subjects",
            "Developing and applying science process skills and using science literacy to understand the natural world and everyday life",
            "Only reading about scientific discoveries",
            "Only conducting research in a laboratory"
        ],
        "a": 1,
        "exp": "Understanding science implies developing and applying science process skills and using science literacy to understand the natural world and activities in everyday life."
    },
    # Science Education in Basic and Tertiary
    {
        "q": "What skills does science education help students develop in basic education?",
        "opts": [
            "Only memorization skills",
            "Process skills, critical thinking skills, and life skills",
            "Only artistic and creative skills",
            "Only physical and athletic skills"
        ],
        "a": 1,
        "exp": "In basic education, science education helps students learn important concepts and develop process skills, critical thinking skills, and life skills."
    },
    {
        "q": "In basic education, what kinds of concepts does science education help students learn?",
        "opts": [
            "Abstract philosophical ideas",
            "Important concepts and facts related to everyday life",
            "Only advanced scientific theories",
            "Only historical facts about scientists"
        ],
        "a": 1,
        "exp": "In basic education, science education helps students learn important concepts and facts related to everyday life."
    },
    {
        "q": "What does science education in tertiary level focus on in terms of professions?",
        "opts": [
            "Only preparing students to become doctors",
            "Preparation of science teachers, scientists, engineers, and other professionals in science-related fields",
            "Only training future politicians",
            "Only training athletes and artists"
        ],
        "a": 1,
        "exp": "In tertiary education, science education focuses on the preparation of science teachers, scientists, engineers, and other professionals in various science-related fields."
    },
    {
        "q": "What does tertiary science education also develop in students?",
        "opts": [
            "Only vocational and trade skills",
            "Understanding and appreciation of science ideas and scientific works",
            "Only business and entrepreneurship skills",
            "Only language and communication skills"
        ],
        "a": 1,
        "exp": "In tertiary education, science education deals with developing students' understanding and appreciation of science ideas and scientific works."
    },
    # PSHSS
    {
        "q": "What is the Philippine Science High School System (PSHSS)?",
        "opts": [
            "A private school for wealthy students",
            "A government program for gifted students in the Philippines",
            "A university specializing in medical sciences",
            "A vocational school for technology students"
        ],
        "a": 1,
        "exp": "The Philippine Science High School System (PSHSS) is a government program for gifted students in the Philippines."
    },
    {
        "q": "Under which government agency is the PSHSS a service institute?",
        "opts": [
            "Department of Education (DepEd)",
            "Department of Health (DOH)",
            "Department of Science and Technology (DOST)",
            "Department of Interior and Local Government (DILG)"
        ],
        "a": 2,
        "exp": "The PSHSS is a service institute of the DOST (Department of Science and Technology)."
    },
    {
        "q": "What does the PSHSS offer to its students?",
        "opts": [
            "Paid tuition with partial scholarships",
            "Free scholarship for secondary courses with special emphasis on science subjects",
            "College-level programs only",
            "Vocational training in technology"
        ],
        "a": 1,
        "exp": "The PSHSS offers a free scholarship for secondary courses with special emphasis on subjects pertaining to the sciences."
    },
    # SSES
    {
        "q": "When did the Special Science Elementary School (SSES) Project start?",
        "opts": [
            "June 2000",
            "June 2005",
            "June 2007",
            "June 2010"
        ],
        "a": 2,
        "exp": "The SSES Project started in June 2007."
    },
    {
        "q": "How many elementary schools initially participated in the SSES Project?",
        "opts": [
            "25",
            "37",
            "57",
            "75"
        ],
        "a": 2,
        "exp": "The SSES Project started in June 2007 with 57 identified elementary schools participating across the country."
    },
    {
        "q": "What is the aim of the Special Science Elementary School (SSES) Project?",
        "opts": [
            "To develop Filipino children equipped with scientific and technological knowledge, skills, and values",
            "To build more science high schools in the provinces",
            "To train elementary teachers in research methods",
            "To provide free laptops to science students"
        ],
        "a": 0,
        "exp": "The SSES Project aims to develop Filipino children equipped with scientific and technological knowledge, skills, and values."
    },
    {
        "q": "What type of curriculum does the SSES Project provide for science-inclined children?",
        "opts": [
            "A standard curriculum identical to regular schools",
            "A special curriculum that recognizes the multiple intelligence of learners",
            "A purely online curriculum",
            "A curriculum focused only on mathematics"
        ],
        "a": 1,
        "exp": "The SSES Project provides a special curriculum that recognizes the multiple intelligence of learners."
    },
    {
        "q": "Which of the following is a mission of the SSES Project?",
        "opts": [
            "Promote the development of lifelong learning skills and holistic development of learners",
            "Focus only on academic competitions",
            "Reduce the number of science schools in the Philippines",
            "Provide scholarship to college students only"
        ],
        "a": 0,
        "exp": "The SSES Project's missions include promoting lifelong learning skills and fostering the holistic development of the learners."
    },
    # QC Regional Science High School
    {
        "q": "What is the vision of the Quezon City Regional Science High School?",
        "opts": [
            "To be the biggest school in Metro Manila",
            "To serve as a venue providing maximum opportunities for science-gifted students to develop the spirit of inquiry and creativity",
            "To produce the most number of doctors in the Philippines",
            "To be fully funded by the private sector"
        ],
        "a": 1,
        "exp": "The QC Regional Science High School envisions to serve as a venue providing maximum opportunities for science-gifted students to develop the spirit of inquiry and creativity."
    },
    {
        "q": "What is the focus of the curriculum of Quezon City Regional Science High School?",
        "opts": [
            "Arts and humanities",
            "Business and entrepreneurship",
            "Science and technology",
            "Physical education and sports"
        ],
        "a": 2,
        "exp": "The curriculum of QC Regional Science High School focuses on science and technology."
    },
    {
        "q": "Who supports the Quezon City Regional Science High School?",
        "opts": [
            "Private corporations only",
            "International organizations and the UN",
            "The local government unit and the PTA",
            "The national government exclusively"
        ],
        "a": 2,
        "exp": "The QC Regional Science High School is well-supported by the local government unit (LGU) and the PTA (Parent-Teacher Association)."
    },
    # Cebu City Science High School
    {
        "q": "When was the Cebu City Science High School (also known as Cebu City National High School) established?",
        "opts": [
            "July 17, 1960",
            "July 17, 1965",
            "July 17, 1970",
            "July 17, 1975"
        ],
        "a": 2,
        "exp": "Cebu City Science High School was established on July 17, 1970."
    },
    {
        "q": "After which school's objectives was the Cebu City Science High School patterned?",
        "opts": [
            "Manila Science High School",
            "Philippine Science High School",
            "Quezon City Regional Science High School",
            "Central Visayan Institute Foundation"
        ],
        "a": 1,
        "exp": "Cebu City Science High School's overall concept was patterned after the objectives of the Philippine Science High School."
    },
    {
        "q": "Who donated the land where the Cebu City Science High School is located?",
        "opts": [
            "President Ferdinand Marcos",
            "President Sergio Osmena Jr.",
            "Don Sergio Osmena Sr.",
            "Rosalina Kintanar"
        ],
        "a": 2,
        "exp": "The land where Cebu City Science High School stands was donated by Don Sergio Osmena Sr. to the City Government."
    },
    {
        "q": "Who was the founding principal of Cebu City Science High School?",
        "opts": [
            "Don Sergio Osmena Sr.",
            "Rosalina Kintanar",
            "Ferdinand Marcos",
            "Angel Alcala"
        ],
        "a": 1,
        "exp": "Rosalina Kintanar was the founding principal of Cebu City Science High School."
    },
    {
        "q": "What building did the founding principal of Cebu City Science High School seek aid to construct?",
        "opts": [
            "A science laboratory building",
            "A gymnasium",
            "A 2-storey Academic Library building",
            "A dormitory for students"
        ],
        "a": 2,
        "exp": "Founding principal Rosalina Kintanar sought direct and financial aid from the Office of the President to construct a 2-storey Academic Library building."
    },
    # Manila Science High School
    {
        "q": "What is the distinction of Manila Science High School among all science high schools in the Philippines?",
        "opts": [
            "It is the largest science high school",
            "It is the first science high school in the Philippines",
            "It is the only government-funded science high school",
            "It has the most number of Nobel Prize winners"
        ],
        "a": 1,
        "exp": "Manila Science High School is the first science high school in the Philippines."
    },
    {
        "q": "What is the guiding aim of Manila Science High School?",
        "opts": [
            "To produce the most number of engineers",
            "To produce scientists with souls",
            "To be the top school in ASEAN",
            "To focus only on mathematics"
        ],
        "a": 1,
        "exp": "Manila Science High School aims to produce scientists with souls."
    },
    {
        "q": "What subjects does Manila Science High School's curriculum put more emphasis on?",
        "opts": [
            "History and social studies",
            "Arts and physical education",
            "Science and mathematics",
            "Language and literature"
        ],
        "a": 2,
        "exp": "The curriculum of Manila Science High School puts more emphasis on science and mathematics."
    },
    {
        "q": "What is the name of the entrance exam administered by Manila Science High School?",
        "opts": [
            "UPCAT",
            "NSAT",
            "MSAT",
            "DOST Exam"
        ],
        "a": 2,
        "exp": "Manila Science High School administers the MSAT (Manila Science Aptitude Test) as an entrance exam for students who wish to enroll."
    },
    {
        "q": "Which of the following is a famous alumna of Manila Science High School who became a White House Executive Chef?",
        "opts": [
            "Marizel Sarangelo",
            "Cristeta Comerford",
            "Von Hernandez",
            "Reev Robledo"
        ],
        "a": 1,
        "exp": "Cristeta Comerford, a famous alumna of Manila Science High School, became known as a White House Executive Chef."
    },
    {
        "q": "Which famous Manila Science High School alumnus is known as a Philippine basketball legend and former PBA player?",
        "opts": [
            "Beethoven V. Bunagan",
            "Louie Mar Gangcuangco",
            "Alvin Patrimonio",
            "Von Hernandez"
        ],
        "a": 2,
        "exp": "Alvin Patrimonio, a legendary PBA basketball player, is a famous alumnus of Manila Science High School."
    },
    {
        "q": "Which Manila Science High School alumnus is known for environmental advocacy and was a Goldman Environmental Prize winner?",
        "opts": [
            "Alvin Patrimonio",
            "Beethoven V. Bunagan",
            "Louie Mar Gangcuangco",
            "Von Hernandez"
        ],
        "a": 3,
        "exp": "Von Hernandez, a Goldman Environmental Prize winner known for environmental advocacy, is a famous alumnus of Manila Science High School."
    },
    # CVIF
    {
        "q": "What is the Central Visayan Institute Foundation (CVIF) known as the home and pioneer of?",
        "opts": [
            "The Philippine Science High School System",
            "The Dynamic Learning Program (DLP)",
            "The Special Science Elementary School Project",
            "The National Research Council of the Philippines"
        ],
        "a": 1,
        "exp": "The Central Visayan Institute Foundation (CVIF) is the home and pioneer of the Dynamic Learning Program (DLP)."
    },
    {
        "q": "What is the Dynamic Learning Program (DLP)?",
        "opts": [
            "A digital learning platform for online classes",
            "A synthesis of classical and modern pedagogical theories adapted to foster the highest level of learning, creativity, and productivity",
            "A government program for science scholars",
            "A special curriculum only for elementary students"
        ],
        "a": 1,
        "exp": "DLP is a synthesis of classical and modern pedagogical theories adapted to foster the highest level of learning, creativity, and productivity."
    },
    {
        "q": "What special research facility does the Central Visayan Institute Foundation take pride in?",
        "opts": [
            "A Marine Biology Research Center",
            "A National Agricultural Research Station",
            "A Research Center for Theoretical Physics",
            "A Climate Change Monitoring Center"
        ],
        "a": 2,
        "exp": "The Central Visayan Institute Foundation takes pride in its Research Center for Theoretical Physics."
    },
    {
        "q": "What type of pedagogical approach does CVIF's Dynamic Learning Program combine?",
        "opts": [
            "Online and traditional lecture methods",
            "Classical and modern pedagogical theories",
            "Foreign and local teaching methods only",
            "Only modern technology-based learning"
        ],
        "a": 1,
        "exp": "The Dynamic Learning Program (DLP) is a synthesis of classical and modern pedagogical theories."
    },
    {
        "q": "Which of the following correctly describes science education in the Philippines at the basic level?",
        "opts": [
            "It focuses only on advanced research and theoretical science",
            "It helps students learn concepts related to everyday life and develop process, critical thinking, and life skills",
            "It exclusively prepares students for international science competitions",
            "It focuses only on memorizing scientific formulas"
        ],
        "a": 1,
        "exp": "In basic education, science education helps students learn important concepts and facts related to everyday life, including process skills, critical thinking skills, and life skills."
    },
    {
        "q": "Which science school was established in line with the Government's Science and Technological Education and Manpower Development Program?",
        "opts": [
            "Manila Science High School",
            "QC Regional Science High School",
            "Cebu City Science High School",
            "Central Visayan Institute Foundation"
        ],
        "a": 2,
        "exp": "Cebu City Science High School was established in line with the Government's Science and Technological Education and Manpower Development Program."
    },
]


def shuffle_options(question):
    indices = list(range(len(question["opts"])))
    random.shuffle(indices)
    new_opts = [question["opts"][i] for i in indices]
    new_answer = indices.index(question["a"])
    return {**question, "opts": new_opts, "a": new_answer}


def get_grade(score, total):
    pct = score / total * 100
    if pct == 100:
        return "PERFECT! Outstanding mastery of Science Education in the Philippines!"
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
    print("     SCIENCE EDUCATION IN THE PHILIPPINES REVIEWER")
    print("     Science, Technology, and Society")
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