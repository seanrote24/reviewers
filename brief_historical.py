#BRIEF-HISTORICAL-BACKGROUND-OF-SCIENCE-AND-TECHNOLOGY
import random 

ALL_QUESTIONS = [
    {
        "q": "When did the Stone Age begin?",
        "opts": ["Around 5 million years ago", "Around 2.5 million years ago", "Around 1200 BCE", "Around 500 BCE"],
        "a": 1,
        "exp": "The Stone Age began around 2.5 million years ago and ended when humans started using metal tools."
    },
    {
        "q": "Which of the following is NOT one of the three main periods of the Stone Age?",
        "opts": ["Paleolithic (Old Stone Age)", "Mesolithic (Middle Stone Age)", "Neolithic (New Stone Age)", "Metallolithic (Metal Stone Age)"],
        "a": 3,
        "exp": "The three main periods are Paleolithic, Mesolithic, and Neolithic. 'Metallolithic' is not a real period."
    },
    {
        "q": "What characterized the Paleolithic (Old Stone Age) period?",
        "opts": ["Farming begins", "Transition between ages", "Hunting and gathering", "Use of iron tools"],
        "a": 2,
        "exp": "The Paleolithic period was characterized by hunting and gathering as the primary way of life."
    },
    {
        "q": "What major discovery was considered a turning point in human evolution during the Stone Age?",
        "opts": ["Discovery of agriculture", "Discovery of fire", "Invention of writing", "Smelting of iron"],
        "a": 1,
        "exp": "The discovery of fire was a major turning point — used for cooking, warmth, and protection."
    },
    {
        "q": "What is cave art considered to be?",
        "opts": ["Military records", "Religious rituals only", "Some of the earliest forms of art", "Evidence of alien contact"],
        "a": 2,
        "exp": "Cave art — paintings showing animals and daily life — is considered among the earliest forms of art by early humans."
    },
    {
        "q": "Which Stone Age period marked the beginning of farming and permanent settlements?",
        "opts": ["Paleolithic", "Mesolithic", "Bronze Age", "Neolithic"],
        "a": 3,
        "exp": "In the Neolithic (New Stone Age), humans began farming and domesticating animals, leading to permanent settlements."
    },
    {
        "q": "When did the Iron Age begin?",
        "opts": ["Around 5000 BCE", "Around 3000 BCE", "Around 1200 BCE", "Around 500 CE"],
        "a": 2,
        "exp": "The Iron Age began around 1200 BCE, following the Bronze Age."
    },
    {
        "q": "Why was iron preferred over bronze during the Iron Age?",
        "opts": ["Iron was more colorful", "Iron was stronger and more widely available", "Iron was lighter", "Iron was easier to melt"],
        "a": 1,
        "exp": "Iron was stronger and more available than bronze, making it the preferred material for tools and weapons."
    },
    {
        "q": "Which civilizations emerged as powerful during the Iron Age?",
        "opts": ["Egypt and Mesopotamia", "China and India", "Ancient Greece and Ancient Rome", "Aztec and Inca"],
        "a": 2,
        "exp": "Powerful civilizations like Ancient Greece and Ancient Rome emerged during the Iron Age."
    },
    {
        "q": "How did iron tools improve life during the Iron Age?",
        "opts": ["They made cave painting easier", "They improved plowing and harvesting, increasing food production", "They helped build boats", "They were used only for writing"],
        "a": 1,
        "exp": "Iron tools improved plowing and harvesting, leading to increased food production and better farming."
    },
    {
        "q": "What was a key result of iron weapons during the Iron Age?",
        "opts": ["Armies became weaker", "Warfare became more organized and armies more effective", "People stopped fighting", "Iron weapons replaced all farming tools"],
        "a": 1,
        "exp": "Iron weapons made armies stronger and more effective, and warfare became more organized."
    },
    {
        "q": "What musical instrument from the Philippine Pre-Colonial Period is the kulintang?",
        "opts": ["Guitar", "Drum", "Gong-based instrument", "Flute"],
        "a": 2,
        "exp": "The kulintang is a gong-based instrument from the Philippine Pre-Colonial Period."
    },
    {
        "q": "What is a 'tambuli' in the context of Philippine Pre-Colonial culture?",
        "opts": ["A type of boat", "A traditional wind instrument (horn)", "A form of writing", "A type of blade"],
        "a": 1,
        "exp": "The tambuli is a traditional Philippine wind instrument, typically a horn used for communication or signaling."
    },
    {
        "q": "Which colonial power introduced the Galleon Trade to the Philippines?",
        "opts": ["Americans", "Japanese", "Portuguese", "Spanish"],
        "a": 3,
        "exp": "The Galleon Trade was introduced during the Spanish Colonial Era in the Philippines."
    },
    {
        "q": "What was a major characteristic of education during the Spanish Colonial Era in the Philippines?",
        "opts": ["Free education for all Filipinos", "Schools focused mainly on Science and medicine, mainly for boys", "Universal literacy programs", "Education focused on trade for all"],
        "a": 1,
        "exp": "Schools during the Spanish era focused on Science and medicine and were mainly for boys, serving the principalia class."
    },
    {
        "q": "What government institution did the Spanish establish during their colonial rule in the Philippines?",
        "opts": ["A research university", "The first government agency", "A public school system", "A national hospital"],
        "a": 1,
        "exp": "The Spanish established the first government agency in the Philippines during their colonial era."
    },
    {
        "q": "What did the American Colonial Era establish that the Spanish did not?",
        "opts": ["The Galleon Trade", "A public education system for all", "Religious institutions", "Traditional blade-making"],
        "a": 1,
        "exp": "The Americans established the Public Education System, making education available to all."
    },
    {
        "q": "Which fields of science did the American Colonial Era emphasize?",
        "opts": ["Astronomy and physics", "Food Processing, Agriculture, and Biology", "Military science", "Mathematics and engineering"],
        "a": 1,
        "exp": "The American Colonial Era focused on Food Processing, Agriculture, and Biology as key scientific fields."
    },
    {
        "q": "What healthcare advancement came with the American Colonial Era?",
        "opts": ["Only military hospitals were built", "Hospitals and healthcare services were built for all social classes", "Healthcare was only for the elite", "Traditional healing was promoted"],
        "a": 1,
        "exp": "The Americans built hospitals and healthcare accessible to all social statuses."
    },
    {
        "q": "What key educational institution did Americans establish in the Philippines?",
        "opts": ["The first seminary", "A Research University", "A military academy", "A trade school only"],
        "a": 1,
        "exp": "The Americans established a Research University in the Philippines during their colonial period."
    },
    {
        "q": "What are the post-colonial periods discussed in the lecture?",
        "opts": ["Martial Law Era and People Power", "Marcos Era and the Fifth Republic", "Commonwealth and Japanese Occupation", "Aguinaldo Era and the Third Republic"],
        "a": 1,
        "exp": "The post-colonial periods covered are the Marcos Era and the Fifth Republic."
    },
    {
        "q": "Which lifestyle did Stone Age people primarily follow before the Neolithic period?",
        "opts": ["Sedentary farming lifestyle", "Industrial factory work", "Nomadic hunter-gatherer lifestyle", "Trading in permanent towns"],
        "a": 2,
        "exp": "Before the Neolithic period, Stone Age people were nomadic — moving from place to place hunting and gathering."
    },
    {
        "q": "How did the Iron Age affect social organization?",
        "opts": ["Villages disappeared", "Villages grew into larger communities and early cities with complex trade", "People returned to caves", "Social organization became simpler"],
        "a": 1,
        "exp": "During the Iron Age, villages grew into larger communities and early cities, with trade and social organization becoming more complex."
    },
    {
        "q": "What was the main focus of Spanish-era health and education in the Philippines?",
        "opts": ["Universal access for all Filipinos", "It was mainly used by the principalia class", "It was focused on women's education", "It was established only in rural areas"],
        "a": 1,
        "exp": "Health and education systems during the Spanish colonial era were used mainly by the principalia (elite) class."
    },
    {
        "q": "What cultural changes did the American Colonial Era bring to the Philippines?",
        "opts": ["Introduction of Spanish language only", "New ways of language, alphabet, food and clothing culture, and preservatives/additives", "Promotion of pre-colonial traditions only", "Introduction of the Galleon Trade"],
        "a": 1,
        "exp": "The American era brought new language, a new alphabet, food and clothing culture, and introduced preservatives and additives."
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
        return "PERFECT! Outstanding mastery of Science & Technology in the Philippines!"
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
    print("  SCIENCE & TECHNOLOGY IN THE PHILIPPINES REVIEWER")
    print("  Based on: Brief Historical Background Lecture")
    print_separator("=")
    print(f"  Total questions: {len(ALL_QUESTIONS)}")
    print("  Questions and choices shuffle every attempt!")
    print_separator("=")
    print()

    while True:
        # Shuffle questions and options each attempt
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

            # Get valid answer
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

        # Final score
        print_separator("=")
        print("                     QUIZ COMPLETE!")
        print_separator("=")
        pct = round(score / len(questions) * 100)
        print(f"\n  FINAL SCORE: {score} / {len(questions)}  ({pct}%)\n")
        print(f"  {get_grade(score, len(questions))}")
        print()

        # Show missed items
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

        # Ask to retry
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

