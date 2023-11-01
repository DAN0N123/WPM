import random

def get_word():
    subjects = ["cat", "dog", "friend", "sun", "bird", "car", "mailman", "buddy", "entrepreneur"]
    verbs = ["jumps", "runs", "sings", "sleeps", "eats", "delivered", "bought", "told"]
    adjectives = ["A quick", "The lazy", "The happy", "A bright", "The friendly", "A witty", "An instinctive", "His own"]
    objects = ["the ball", "a book", "the sky", "a rainbow", "a sandwich", "an apple", "the program"]


    text = ""

    word_count = 0

    while word_count < 5:
        subject = random.choice(subjects)
        verb = random.choice(verbs)
        adjective = random.choice(adjectives)
        object_ = random.choice(objects)
        sentence = f"{adjective} {subject} {verb} {object_}. "
        
        sentence_word_count = len(sentence.split())
        if word_count + sentence_word_count <= 70:
            text += sentence
            word_count += sentence_word_count
        else:
            break
    return text


