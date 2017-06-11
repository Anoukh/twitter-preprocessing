def select_emoticon(x):
    return {
        ":)": 'happy',
        ":(": 'sad',
        ":o": 'surprised',
        ":/": 'confused',
        "gr8": 'great',
        "n8": 'night',
        "gd": 'good',
        "awsm": 'awesome',
        "h8": 'hate',
        "lol": "laugh",
        "rofl": "laugh",
        "rotfl": "laugh",
        "srsly": "seriously",
        "thx": "thanks"
    }.get(x, x)
