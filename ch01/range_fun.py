from datetime import datetime


# range fun
odds = range(1, 60, 2)
evens = range(2, 60, 2)

this_minute = datetime.today().minute
if this_minute in odds:
    result = "Odd time for that!"

if this_minute in evens:
    result = "Even now!"

print(result)
