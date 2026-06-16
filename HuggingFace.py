from transformers import pipeline 

classifier= pipeline("sentiment-analysis")

result= classifier("I am a diploma student and currently persuing IT from JES Jharsuguda.")

print(result)