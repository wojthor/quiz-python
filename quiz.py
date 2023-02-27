import random
import string

alfabet = "abc"
result = None


QUESTION_AND_ANSWERS = [
    {
        "question": "Ile lat ma Cristiano Ronaldo?",
        "answers": ["36", "37", "38"],
        "correct_answer": "C",
    },
    {
        "question": "Jak się nazywa najnowsza nutka Kazka?",
        "answers": ["Jak zyć w WWA", "Szklane Domy", "Do zobaczenia"],
        "correct_answer": "A",
    },
    {
        "question": "Kto jest prezesem PZF? (Polski związek freak-fighterów)",
        "answers": ["Tańcula", "Borek", "Wiewiór"],
        "correct_answer": "A",
    },
    {
        "question": "Dokończ zdanie: Wczoraj była siłownia...",
        "answers": [
            "to dzisiaj fajrant",
            "to dzisiaj są zakwasy",
            "to jutro morsowanie",
        ],
        "correct_answer": "B",
    },
    {
        "question": "20 lipca 1969 roku na księżycu wylądował..?",
        "answers": ["Michał Florek", "Nico Belic", "Neil Amstrong"],
        "correct_answer": "C",
    },
    {
        "question": "Rodzice zrobili przetwory na zimę, w sumie 16 słoików. Dziewięć słoików zawieźli cioci Helenie. Ile słoików zostało rodzicom?",
        "answers": ["7", "16", "0"],
        "correct_answer": "A",
    },
    {
        "question": "Czy SEAT LEON od Marca był kręcony?",
        "answers": ["Tak", "Nie", "Trudno powiedzieć"],
        "correct_answer": "A",
    },
    {
        "question": "Wskaż funkcję pierwotną do funkcji y=2x",
        "answers": ["y=x+1", "y=x2+2 ", "y=1"],
        "correct_answer": "B",
    },
    {
        "question": "Patryczek przyszedł na siłownię, robi klateczkę i założył po 20kg na stronę. Ile Patryczek wyciska na klateczkę?",
        "answers": ["40kg", "60kg", "55kg"],
        "correct_answer": "B",
    },
    {
        "question": "Jaką diagnoze oświadczył dr. Michał Florek gdy Wojtek złamał sobie nogę?",
        "answers": [
            "OO BOŻE ZŁAMANIE OTWARTE",
            "MYŚLE ŻE ZŁAMANIE JEST PRAWDOPODOBNE",
            "NIE NO LEKKIE SKRĘCENIE",
        ],
        "correct_answer": "C",
    },
]


def score():
    global result
    score = "Wynik końcowy: " + str(result) + "/10"
    print()
    print(score)


def format_answers(question, answers):
    letter = "A"
    print(question)

    for answer in answers:
        print(letter + ". " + answer)
        letter = chr(ord(letter) + 1)


def run():
    global result

    for item in QUESTION_AND_ANSWERS:
        format_answers(item["question"], item["answers"])
        user_answer = input("Podaj odpowiedź: ")
        try:
            if (
                user_answer.upper() == item["correct_answer"]
                or alfabet[item["answers"].index(user_answer)].upper()
                == item["correct_answer"]
            ):
                print()
                print("POPRAWNA ODPOWIEDZ")
                print()
                result += 1

            else:
                print()
                print("NIEPOPRAWNA ODPOWIEDZ")
                print()
        except ValueError:
            print()
            print("NIEPOPRAWNA ODPOWIEDZ")
            print()


run()
score()
