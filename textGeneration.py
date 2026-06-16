from transformers import pipeline
generation= pipeline("text-generation",model='gpt2')
result= generation(
    "Artificial Intelligence is",
    max_length=30
)
print(result)