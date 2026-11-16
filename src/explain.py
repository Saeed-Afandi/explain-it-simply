from transformers import pipeline

MODEL_NAME = "google/flan-t5-small"

def load_model():
    return pipeline(
        "text2text-generation",
        model=MODEL_NAME,
        tokenizer=MODEL_NAME,
    )

def simplify_text(text, generator):
    prompt = (
        "Explain the following text to a younger student using simple words. "
        "Keep the meaning accurate and use a short example if it helps:\n\n"
        + text
    )

    result = generator(
        prompt,
        max_new_tokens=160,
        do_sample=False,
    )

    return result[0]["generated_text"].strip()

def main():
    print("Explain It Simply")
    print("=================")
    print("Paste a science or technology paragraph below.")
    print("Press Enter when you are done.\n")

    text = input("> ").strip()

    if not text:
        print("No text was entered.")
        return

    print("\nLoading model...")
    generator = load_model()

    explanation = simplify_text(text, generator)

    print("\nSimplified explanation")
    print("----------------------")
    print(explanation)

if __name__ == "__main__":
    main()
