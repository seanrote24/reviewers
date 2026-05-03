#Developments sci tech reviewer 

import random

ALL_QUESTIONS = [
    {
        "q": "From the beginning of time, what has man always strived to improve?",
        "opts": [
            "His physical strength",
            "His way and quality of life",
            "His political power",
            "His artistic abilities"
        ],
        "a": 1,
        "exp": "From the beginning of time, man has strived to improve his way and quality of life."
    },
    {
        "q": "What did the caveman develop that added value to their life?",
        "opts": [
            "Written language and art",
            "Tools, logical sequences for activities, and evolved processes",
            "Trading systems and currency",
            "Religious practices and rituals"
        ],
        "a": 1,
        "exp": "The caveman discovered how to make and use tools, developed logical sequences for activities, and evolved processes that added value to their life."
    },
    {
        "q": "How is 'technology' best described in the context of this lesson?",
        "opts": [
            "Only the use of modern computers and machines",
            "The totality of the use and application of knowledge, skills, tools, and materials",
            "The science of building structures",
            "A system of communication between people"
        ],
        "a": 1,
        "exp": "Technology is described as the totality of the use and application of knowledge, skills, tools, and materials."
    },
    {
        "q": "To many countries, what does 'development' simply mean?",
        "opts": [
            "Becoming more democratic",
            "Becoming in the future what industrialized countries are today",
            "Increasing the population",
            "Building more schools and hospitals"
        ],
        "a": 1,
        "exp": "To many countries, 'development' is simply becoming in the future what industrialized countries are today."
    },
    {
        "q": "Which of the following is NOT listed as a component of development?",
        "opts": [
            "The acceleration of economic growth",
            "The reduction of inequality",
            "The eradication of absolute poverty",
            "The expansion of military power"
        ],
        "a": 3,
        "exp": "Development involves the acceleration of economic growth, the reduction of inequality, and the eradication of absolute poverty. Military expansion is not listed."
    },
    {
        "q": "Is development purely an economic phenomenon?",
        "opts": [
            "Yes, development is only about economic growth",
            "No, development must encompass more than the material and financial side of people's lives",
            "Yes, but only for developing countries",
            "No, development is only about social change"
        ],
        "a": 1,
        "exp": "Development is not purely an economic phenomenon. It must encompass more than the material and financial side of people's lives."
    },
    {
        "q": "Development should be a _______ process.",
        "opts": [
            "Single-dimensional",
            "Purely economic",
            "Multi-dimensional",
            "Military-focused"
        ],
        "a": 2,
        "exp": "Development should be a multi-dimensional process involving reorganization of entire economic and social systems."
    },
    {
        "q": "Which of the following is part of what development should involve?",
        "opts": [
            "Only changes in government leadership",
            "Major changes in administrative, institutional, and social structures",
            "Only financial investment from foreign countries",
            "Reduction of education access"
        ],
        "a": 1,
        "exp": "Development involves major changes in administrative, institutional, and social structures, as well as popular attitudes, customs, and beliefs."
    },
    {
        "q": "Development also involves major changes in which of the following?",
        "opts": [
            "Popular attitudes, customs, and beliefs",
            "Only language and culture",
            "Only the military structure",
            "Only foreign policy"
        ],
        "a": 0,
        "exp": "Development involves major changes in popular attitudes, customs, and beliefs, not just structural changes."
    },
    {
        "q": "How are science and technology regarded in relation to developing states?",
        "opts": [
            "As threats to traditional culture",
            "As forces needed for improving the welfare of developing states",
            "As tools only for wealthy nations",
            "As optional enhancements to development"
        ],
        "a": 1,
        "exp": "Science and technology are both regarded as forces needed for improving the welfare of developing states."
    },
    {
        "q": "Scientific and technological revolutions underpin which of the following?",
        "opts": [
            "Economic advances and improvements in health, education, and infrastructure",
            "Only military advancements",
            "Cultural preservation only",
            "Environmental degradation only"
        ],
        "a": 0,
        "exp": "Technological and scientific revolutions underpin economic advances and improvements in health systems, education, and infrastructure."
    },
    {
        "q": "What negative role is science and technology feared to contribute to?",
        "opts": [
            "Reduction of poverty",
            "Dehumanization of man and degradation of the environment",
            "Improvement of education",
            "Strengthening of communities"
        ],
        "a": 1,
        "exp": "Science and technology are also feared to be contributors to the dehumanization of man and to the degradation of the environment."
    },
    {
        "q": "The role of science and technology in development should be directed towards reducing inequalities between which groups?",
        "opts": [
            "Only between different political parties",
            "Advanced and developing countries, and between various sections of the population",
            "Only between men and women",
            "Only between young and old generations"
        ],
        "a": 1,
        "exp": "S&T in development should reduce inequalities between advanced and developing countries, and between various sections of the population within a country."
    },
    {
        "q": "Through breakthroughs in health services and education, what power do technologies have?",
        "opts": [
            "The power to increase inequality",
            "The power to better the lives of poor people in developing countries",
            "The power to replace human labor entirely",
            "The power to reduce population growth"
        ],
        "a": 1,
        "exp": "Breakthroughs in health services and education give technologies the power to better the lives of poor people in developing countries."
    },
    {
        "q": "Which disease, described as a scourge of the African continent for centuries, is now possible to eradicate?",
        "opts": [
            "Tuberculosis",
            "Malaria",
            "Cholera",
            "Smallpox"
        ],
        "a": 1,
        "exp": "Eradicating malaria, a scourge of the African continent for centuries, is now possible through technological breakthroughs."
    },
    {
        "q": "What is the result of cures being found for diseases endemic in developing countries?",
        "opts": [
            "People with debilitating conditions can live healthy and productive lives",
            "Only wealthy people benefit from the cures",
            "Diseases spread more quickly",
            "Healthcare costs increase for everyone"
        ],
        "a": 0,
        "exp": "Cures for diseases endemic in developing countries allow people with debilitating conditions to live healthy and productive lives."
    },
    {
        "q": "What challenge does managing the technological revolution pose?",
        "opts": [
            "It makes all countries equal",
            "Certain innovations and discoveries will raise bio-ethical issues",
            "Technology eliminates the need for education",
            "It causes countries to stop trading"
        ],
        "a": 1,
        "exp": "Managing the technological revolution poses the challenge that certain innovations and discoveries will raise bio-ethical issues."
    },
    {
        "q": "Which of the following is given as an example of a bio-ethical issue raised by technology?",
        "opts": [
            "Building new roads",
            "Genetic modification of food crops and cloning",
            "Use of solar energy",
            "Development of new currencies"
        ],
        "a": 1,
        "exp": "Genetic modification of food crops and cloning are examples of bio-ethical issues raised by technological innovation."
    },
    {
        "q": "How does the cost of healthcare worsen present inequality?",
        "opts": [
            "By making healthcare free for everyone",
            "By limiting healthcare access to wealthy individuals",
            "By reducing the quality of medicine",
            "By increasing the number of doctors"
        ],
        "a": 1,
        "exp": "The cost of healthcare worsens present inequality by limiting health care access to wealthy individuals."
    },
    {
        "q": "What happens to public healthcare budgets in G7 countries due to high-cost medical equipment and interventions?",
        "opts": [
            "Budgets increase for poor neighborhoods",
            "Public health care budgets are overstretched and service quality in poor neighborhoods is lowered",
            "All citizens receive equal healthcare",
            "Medical research is halted"
        ],
        "a": 1,
        "exp": "Demand for very high-cost diagnostic equipment and surgical interventions overstretches public health care budgets and lowers service quality in poor neighborhoods."
    },
    {
        "q": "What type of technologies increase carbon emissions and environmental damage?",
        "opts": [
            "Technologies focused on renewable energy",
            "Resource-intensive technologies focused on satisfying high consumption demand",
            "Technologies used in farming",
            "Technologies used in building schools"
        ],
        "a": 1,
        "exp": "Resource-intensive technologies, focused on satisfying high consumption demand (like holidays in coastal resorts and iconic cities), increase carbon emissions and environmental damage."
    },
    {
        "q": "Which example of high consumption demand is mentioned as contributing to environmental damage?",
        "opts": [
            "Use of public transportation",
            "Holidays abroad in coastal resorts, wilderness areas, or iconic cities",
            "Recycling programs",
            "Home gardening"
        ],
        "a": 1,
        "exp": "Holidays abroad in coastal resorts, wilderness areas, or iconic cities are mentioned as high consumption demand activities that increase carbon emissions and environmental damage."
    },
    {
        "q": "What should developing countries invest in to promote technological advances?",
        "opts": [
            "Only in military technology",
            "Quality education for youth and continuous skills training for workers and managers",
            "Only in industrial machinery",
            "Only in foreign partnerships"
        ],
        "a": 1,
        "exp": "Developing countries should invest in quality education for youth and in continuous skills training for workers and managers."
    },
    {
        "q": "What should be ensured about knowledge to promote technological advances?",
        "opts": [
            "Knowledge should be kept secret for competitive advantage",
            "Knowledge should be shared as widely as possible across society",
            "Knowledge should only be shared with government officials",
            "Knowledge should only be available in universities"
        ],
        "a": 1,
        "exp": "Developing countries should ensure that knowledge is shared as widely as possible across society."
    },
    {
        "q": "What does adopting appropriate technologies directly lead to?",
        "opts": [
            "Higher unemployment",
            "Higher productivity, which is the key to growth",
            "Reduction in trade",
            "Increase in inequality"
        ],
        "a": 1,
        "exp": "Adopting appropriate technologies leads directly to higher productivity, which is the key to growth."
    }
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
        return "PERFECT! Outstanding mastery of Developments of Science and Technology!"
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
    print("     DEVELOPMENTS OF SCIENCE AND TECHNOLOGY REVIEWER")
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
