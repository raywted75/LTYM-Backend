from transformers import pipeline


classifier = pipeline(
    "text-classification",
    model='bhadresh-savani/distilbert-base-uncased-emotion',
    top_k=None
)


def get_emotions(text):
    prediction = classifier(text)

    emotions = dict()
    for result in prediction[0]:
        emotion, score = result['label'], result['score']
        if emotion != 'fear':
            emotions[emotion] = score

    print(f"Emotions: {emotions}")
    return emotions
