import random

ALL_QUESTIONS = [
    # Ramon Barba
    {
        "q": "What is Ramon Cabanos Barba known for?",
        "opts": [
            "Developing aquaculture and tilapia farming technologies",
            "Developing a method to induce mango flowering using potassium nitrate",
            "Studying toxins from cone snails for medical use",
            "Research on climate change and polar ice caps"
        ],
        "a": 1,
        "exp": "Ramon Cabanos Barba developed a method to induce mango flowering using potassium nitrate, greatly benefiting the Philippine mango industry."
    },
    {
        "q": "What chemical did Ramon Barba use to induce mango flowering?",
        "opts": [
            "Sodium chloride",
            "Calcium carbonate",
            "Potassium nitrate",
            "Sulfuric acid"
        ],
        "a": 2,
        "exp": "Ramon Barba used potassium nitrate to develop a method that induces mango flowering."
    },
    # Josefino Comiso
    {
        "q": "What is Josefino Cacas Comiso known for?",
        "opts": [
            "Research on wireless communication and microwave technologies",
            "Research on climate change and polar ice caps using satellite data",
            "Pioneering coral reef conservation",
            "Studying marine natural products"
        ],
        "a": 1,
        "exp": "Josefino Cacas Comiso is known for his research on climate change and polar ice caps using satellite data."
    },
    {
        "q": "What technology did Josefino Comiso use in his research on climate change?",
        "opts": [
            "Underwater drones",
            "Satellite data",
            "Soil sampling",
            "Chemical analysis of ocean water"
        ],
        "a": 1,
        "exp": "Josefino Comiso used satellite data to study climate change and polar ice caps."
    },
    # Jose Cruz Jr.
    {
        "q": "What field did Jose Bejar Cruz Jr. specialize in?",
        "opts": [
            "Marine biology and fisheries",
            "Plant chemistry and natural products",
            "Control systems engineering and robotics",
            "Optics and photonics"
        ],
        "a": 2,
        "exp": "Jose Bejar Cruz Jr. specialized in control systems engineering and robotics."
    },
    # Lourdes Cruz
    {
        "q": "What is Lourdes Jansuy Cruz known for?",
        "opts": [
            "Developing tissue culture techniques for plants",
            "Studying toxins from cone snails for medical use",
            "Research on coconut oil (VCO)",
            "Inventing a method to detect drug exposure in newborns"
        ],
        "a": 1,
        "exp": "Lourdes Jansuy Cruz studied toxins from cone snails and explored their potential for medical use."
    },
    {
        "q": "What organisms did Lourdes Cruz study to find toxins for medical use?",
        "opts": [
            "Jellyfish",
            "Sea urchins",
            "Cone snails",
            "Starfish"
        ],
        "a": 2,
        "exp": "Lourdes Cruz studied toxins from cone snails for their potential medical applications."
    },
    # Fabian Dayrit
    {
        "q": "What is Fabian Millar Dayrit known for?",
        "opts": [
            "Research on polar ice caps",
            "Developing aquaculture technologies",
            "Research on natural products chemistry and coconut oil (VCO)",
            "Pioneering coral reef conservation"
        ],
        "a": 2,
        "exp": "Fabian Millar Dayrit is known for his research on natural products chemistry, particularly coconut oil (VCO — Virgin Coconut Oil)."
    },
    {
        "q": "Which specific natural product is Fabian Dayrit's research closely associated with?",
        "opts": [
            "Mango extract",
            "Coconut oil (VCO)",
            "Banana peel compounds",
            "Tilapia oil"
        ],
        "a": 1,
        "exp": "Fabian Dayrit's research is closely associated with natural products chemistry and coconut oil, particularly Virgin Coconut Oil (VCO)."
    },
    # Rafael Guerrero
    {
        "q": "What is Rafael Dineros Guerrero known for?",
        "opts": [
            "Research on marine natural products",
            "Developing technologies in aquaculture and tilapia farming",
            "Research on optics and photonics",
            "Studying plant chemistry"
        ],
        "a": 1,
        "exp": "Rafael Dineros Guerrero developed technologies in aquaculture and tilapia farming, benefiting the Philippine fisheries industry."
    },
    {
        "q": "Which fish species is most associated with Rafael Guerrero's aquaculture research?",
        "opts": [
            "Bangus (milkfish)",
            "Tilapia",
            "Tuna",
            "Lapu-lapu (grouper)"
        ],
        "a": 1,
        "exp": "Rafael Guerrero developed technologies in aquaculture specifically focused on tilapia farming."
    },
    # Enrique Ostrea
    {
        "q": "What did Enrique Mapua Ostrea invent?",
        "opts": [
            "A method to detect cancer using blood tests",
            "A method to detect drug exposure in newborns through meconium testing",
            "A device to monitor coral reef health",
            "A satellite system to track climate change"
        ],
        "a": 1,
        "exp": "Enrique Mapua Ostrea invented a method to detect drug exposure in newborns through meconium (first stool) testing."
    },
    {
        "q": "What sample is used in Enrique Ostrea's method for detecting drug exposure in newborns?",
        "opts": [
            "Urine",
            "Blood",
            "Meconium (first stool of newborns)",
            "Saliva"
        ],
        "a": 2,
        "exp": "Enrique Ostrea's invention uses meconium — the first stool of a newborn — to detect drug exposure."
    },
    # Lilian Patena
    {
        "q": "What is Lilian Formalejo Patena known for?",
        "opts": [
            "Research on wireless communication",
            "Studying climate change using satellite data",
            "Developing tissue culture techniques for plants such as orchids and bananas",
            "Pioneering coral reef conservation"
        ],
        "a": 2,
        "exp": "Lilian Formalejo Patena developed tissue culture techniques for plants, including orchids and bananas."
    },
    {
        "q": "Which plants are examples of Lilian Patena's tissue culture research?",
        "opts": [
            "Rice and corn",
            "Orchids and banana",
            "Mango and coconut",
            "Tilapia and milkfish"
        ],
        "a": 1,
        "exp": "Lilian Patena's tissue culture techniques were applied to plants such as orchids and bananas."
    },
    # Marijo Ruiz
    {
        "q": "What is Marijo Panganiban Ruiz known for?",
        "opts": [
            "Research on marine natural products and environmental chemistry",
            "Developing mango flowering techniques",
            "Control systems engineering and robotics",
            "Research on polar ice caps"
        ],
        "a": 0,
        "exp": "Marijo Panganiban Ruiz is known for research on marine natural products and environmental chemistry."
    },
    # Gregorio Tangonan
    {
        "q": "What is Gregorio Lingot Tangonan known for?",
        "opts": [
            "Research on coral reef conservation",
            "Work on wireless communication and microwave technologies",
            "Developing aquaculture technologies",
            "Research on coconut oil"
        ],
        "a": 1,
        "exp": "Gregorio Lingot Tangonan is known for his work on wireless communication and microwave technologies."
    },
    # Caesar Saloma
    {
        "q": "What field is Caesar Saloma known for?",
        "opts": [
            "Marine science and fisheries",
            "Aquaculture and tilapia farming",
            "Research in optics and photonics (light-based technologies)",
            "Environmental chemistry"
        ],
        "a": 2,
        "exp": "Caesar Saloma is known for his research in optics and photonics — technologies based on light."
    },
    # Edgardo Gomez
    {
        "q": "What is Edgardo Gomez known for?",
        "opts": [
            "Developing tissue culture for plants",
            "Pioneer in coral reef conservation and marine science",
            "Studying toxins from cone snails",
            "Research on wireless communication"
        ],
        "a": 1,
        "exp": "Edgardo Gomez is a pioneer in coral reef conservation and marine science in the Philippines."
    },
    # William Padolina
    {
        "q": "What is William Padolina known for?",
        "opts": [
            "Research in optics and photonics",
            "Developing aquaculture and tilapia farming",
            "Research in plant chemistry and natural products",
            "Inventing meconium drug testing"
        ],
        "a": 2,
        "exp": "William Padolina is known for his research in plant chemistry and natural products."
    },
    # Angel Alcala
    {
        "q": "What is Angel Alcala known for?",
        "opts": [
            "Research on coconut oil and natural products",
            "Establishing marine protected areas and studying biodiversity",
            "Developing mango flowering techniques",
            "Work on wireless communication"
        ],
        "a": 1,
        "exp": "Angel Alcala is known for establishing marine protected areas and studying biodiversity, making major contributions to marine conservation."
    },
    {
        "q": "What conservation structures did Angel Alcala help establish?",
        "opts": [
            "National parks",
            "Forest reserves",
            "Marine protected areas",
            "Coral farming sites"
        ],
        "a": 2,
        "exp": "Angel Alcala established marine protected areas and studied biodiversity, greatly contributing to ocean conservation in the Philippines."
    },
    # Universities
    {
        "q": "Which UP campus is known as the leading agricultural and environmental science school in the Philippines?",
        "opts": [
            "UP Diliman",
            "UP Manila",
            "UP Visayas",
            "UP Los Baños"
        ],
        "a": 3,
        "exp": "UP Los Baños is known as the leading agricultural and environmental science school in the Philippines, focusing on agriculture, forestry, and environmental science."
    },
    {
        "q": "What is the science focus of UP Los Baños?",
        "opts": [
            "Marine science and fisheries",
            "Medicine, pharmacy, and public health",
            "Agriculture, forestry, environmental science, biotechnology, and veterinary medicine",
            "Engineering, physics, and computer science"
        ],
        "a": 2,
        "exp": "UP Los Baños focuses on agriculture, forestry, environmental science, biotechnology, and veterinary medicine."
    },
    {
        "q": "Which UP campus is considered the country's center for marine and fisheries research?",
        "opts": [
            "UP Los Baños",
            "UP Diliman",
            "UP Visayas",
            "UP Manila"
        ],
        "a": 2,
        "exp": "UP Visayas is considered the country's center for marine and fisheries research, focusing on marine science, fisheries, and aquaculture."
    },
    {
        "q": "What is the science focus of UP Visayas?",
        "opts": [
            "Engineering, physics, and mathematics",
            "Agriculture and biotechnology",
            "Medicine and pharmacy",
            "Marine science, fisheries, and aquaculture"
        ],
        "a": 3,
        "exp": "UP Visayas focuses on marine science, fisheries, and aquaculture, making it the center for marine research in the Philippines."
    },
    {
        "q": "Which UP campus is recognized as the premier health sciences institution in the Philippines?",
        "opts": [
            "UP Diliman",
            "UP Los Baños",
            "UP Manila",
            "UP Visayas"
        ],
        "a": 2,
        "exp": "UP Manila is recognized as the premier health sciences institution in the Philippines, offering programs in medicine, nursing, pharmacy, and biomedical sciences."
    },
    {
        "q": "What programs does UP Manila offer that make it a key health sciences institution?",
        "opts": [
            "Agriculture, forestry, and environmental engineering",
            "Marine science, fisheries, and aquaculture",
            "Medicine, nursing, pharmacy, and biomedical sciences",
            "Physics, engineering, and computer science"
        ],
        "a": 2,
        "exp": "UP Manila offers programs in medicine, nursing, pharmacy, and biomedical sciences, making it the premier health sciences institution in the Philippines."
    },
    {
        "q": "Which UP campus serves as the center of scientific research and innovation in the Philippines?",
        "opts": [
            "UP Los Baños",
            "UP Visayas",
            "UP Manila",
            "UP Diliman"
        ],
        "a": 3,
        "exp": "UP Diliman serves as the center of scientific research and innovation in the Philippines, housing the National Science Complex and major research institutes."
    },
    {
        "q": "What important facility does UP Diliman house that supports science and research?",
        "opts": [
            "The National Marine Research Center",
            "The National Science Complex and major research institutes",
            "The National Agricultural Research Station",
            "The National Health Sciences Laboratory"
        ],
        "a": 1,
        "exp": "UP Diliman houses the National Science Complex and major research institutes, supporting research in engineering, physics, IT, and more."
    },
    {
        "q": "What is the science focus of UP Diliman?",
        "opts": [
            "Agriculture, forestry, and veterinary medicine",
            "Marine science and fisheries",
            "Medicine, pharmacy, and public health",
            "Engineering, physics, mathematics, computer science, and advanced research"
        ],
        "a": 3,
        "exp": "UP Diliman focuses on engineering, physics, mathematics, computer science, and advanced research, and develops technologies in disaster risk reduction and computing."
    },
    {
        "q": "Which Filipino scientist's work most directly helps improve food security and the Philippine fishing industry?",
        "opts": [
            "Lourdes Cruz",
            "Caesar Saloma",
            "Rafael Guerrero",
            "Enrique Ostrea"
        ],
        "a": 2,
        "exp": "Rafael Guerrero developed technologies in aquaculture and tilapia farming, directly improving the Philippine fishing industry and food security."
    },
    {
        "q": "Which two Filipino scientists made major contributions to environmental and ocean conservation?",
        "opts": [
            "Ramon Barba and Fabian Dayrit",
            "Edgardo Gomez and Angel Alcala",
            "Lilian Patena and Marijo Ruiz",
            "Gregorio Tangonan and Caesar Saloma"
        ],
        "a": 1,
        "exp": "Edgardo Gomez (pioneer in coral reef conservation) and Angel Alcala (established marine protected areas) both made major contributions to ocean and environmental conservation."
    },
    {
        "q": "Which Filipino scientist's invention has a direct impact on detecting drug use in mothers and protecting newborn health?",
        "opts": [
            "Lourdes Cruz",
            "Lilian Patena",
            "Enrique Ostrea",
            "William Padolina"
        ],
        "a": 2,
        "exp": "Enrique Ostrea invented a method to detect drug exposure in newborns through meconium testing, directly impacting newborn health and protection."
    },
    {
        "q": "Which Filipino scientist's research on global warming and ice caps connects the Philippines to international climate science?",
        "opts": [
            "Edgardo Gomez",
            "Josefino Comiso",
            "Angel Alcala",
            "Gregorio Tangonan"
        ],
        "a": 1,
        "exp": "Josefino Comiso's research on climate change and polar ice caps using satellite data connects the Philippines to global climate science."
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
        return "PERFECT! You truly know your Filipino scientists!"
    elif pct >= 80:
        return "EXCELLENT! You have a strong grasp of the material."
    elif pct >= 60:
        return "GOOD JOB! Review a few more scientists and you'll master this."
    else:
        return "KEEP REVIEWING! Go through the slides again and try once more."


def print_separator(char="-", length=60):
    print(char * length)


def run_quiz():
    print_separator("=")
    print("   FAMOUS FILIPINOS IN THE FIELD OF SCIENCE REVIEWER")
    print("   Science, Technology, and Society")
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