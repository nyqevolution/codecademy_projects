# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_email_one(email):
    banned_words = "learning algorithms"
    for words in email:
        if banned_words in email:
            censored_email = email.replace(banned_words, "*" * len(banned_words))
    return censored_email


#censoring a list of words from email_two. cleaned up code from first step.
censor_list = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithms", "her", "herself"]

def censor_email_two(email, banned_words):
    for word in banned_words:
        email = email.replace(word, "*" *len(word))
    return email

#print(censor_email_two(email_two, censor_list))


#censoring a list of words while also replacing other 'negative' words
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor_email_three(email, banned_words, negative_words):
    email = email.lower()
    count = 0
    for word in negative_words:
        if word in email:
            count += 1
            if count > 2:
                email = email.replace(word, "*" * len(word))
    for word in banned_words:
        email = email.replace(word, "*" * len(word))
    return email

print(censor_email_three(email_three, censor_list, negative_words))
