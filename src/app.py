from explain import load_model, simplify_text
from keywords import get_keywords

def main():
    print("Explain It Simply")
    print("=================")
    print("Enter a science or technology paragraph:\n")

    text = input("> ").strip()

    if not text:
        print("No text was entered.")
        return

    keywords = get_keywords(text)

    print("\nLoading the language model...")
    generator = load_model()
    explanation = simplify_text(text, generator)

    print("\nSimple explanation")
    print("------------------")
    print(explanation)

    print("\n3 key words")
    print("-----------")
    for word in keywords:
        print(f"- {word}")

if __name__ == "__main__":
    main()
