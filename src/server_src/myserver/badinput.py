import random

def badinput():
    badinput = [
    'I don\'t get it',
    'NO!',
    'Sorry',
    'Marry me first!',
    'I am too lasy today',
    'Boring...',
    'Go away!',
    'Try again',
    'Make me Great again',
    'Something went wrong',
    'I don\'t want to talk',
    'I am to busy now, to speak with you',
    'I swear, I knew it. But now I forgot',
    'Ok, ooooook, OK! One second. No. I missed that',
    'I don\'t know what that means',
    'I\'m not sure I understand',
    'Can you please repeat that?',
    'Sorry, I missed that']
    secure_random = random.SystemRandom()
    return secure_random.choice(badinput)
