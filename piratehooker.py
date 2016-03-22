import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

prefs = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}
def find_prefs():
    prefs = {}
    for type, question in questions.items():
        print(question)
        prefs[type] = input().lower() in ["yes"]
        print("")
    return prefs
    
def make_bev(prefs):
    bev = []
    for bev_type, liked in prefs.items():
        if not liked:
            continue
bev.append(random.choice(prefs[prefs_type]))
print ("question, want more?")


def main():
    prefs = find_prefs()
    bev = create_bev(prefs)
    print("The recipe for your drink, pirate hooker is:")
    for prefs in bev:
        print("A {}".format(prefs))

if __name__ == "__main__":
    main()