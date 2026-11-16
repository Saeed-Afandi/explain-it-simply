# Explain It Simply

I made this project because I like the idea of using AI to make difficult information easier to understand.

The program takes a science or technology paragraph and gives a simpler explanation. It also finds three important words from the original text.

## Why I made it

While helping my younger sister with schoolwork, I noticed that sometimes the problem is not the idea itself. The explanation can just be too complicated.

I wanted to build a small project that could take a harder paragraph and explain it in a simpler way.

## What it does

The project:

- accepts a science or technology paragraph
- uses a small language model to rewrite it in simpler words
- keeps the main idea of the original text
- extracts three important keywords
- shows the result in a simple format

## Tools I used

- Python
- Hugging Face Transformers
- FLAN-T5
- scikit-learn

## Files

- `src/app.py` runs the full project
- `src/explain.py` creates the simpler explanation
- `src/keywords.py` finds three key words
- `examples/example_input.txt` has a sample paragraph
- `examples/example_output.txt` shows a sample result

## How to run it

Install the packages:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python src/app.py
```

The first run may take longer because the language model has to be downloaded.

## Example idea

Input:

> Photosynthesis is the process by which plants convert light energy into chemical energy.

Possible simpler explanation:

> Plants use sunlight to help make the food they need for energy.

## What I learned

This project helped me understand more about how language models can be used for something practical. I also learned that making an explanation shorter is not enough. The important part is keeping the original meaning while making it easier to understand.

I want to keep testing it with different science and technology topics and improve the results.
