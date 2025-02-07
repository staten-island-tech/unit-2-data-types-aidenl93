time = input("Type a specific day (ex: groundhog day)").strip().lower()
if time == "groundhog day":
    print("stop copying me bro")
    exit()
bro = input("choose a specific number from 1-31")
celeb = input("Choose a celebrity")
verba = input("Choose a verb, past tense (ex: walked:)")
verbb = input("Choose an action")

print(f"It was {time} on the {bro}st when {celeb} {verba}'d in, and started to {verbb}")