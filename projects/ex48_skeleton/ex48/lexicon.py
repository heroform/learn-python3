try:
    from ex48_convert import convert_number
except:
    from .ex48_convert import convert_number

directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs      = ['go', 'stop', 'kill', 'eat']
stop       = ['the', 'in', 'of', 'from', 'at', 'it']
nouns      = ['door', 'bear', 'princess', 'cabinet']

# Input stuff
#stuff = input('> ')

def scan(stuff):
    try:
        word = stuff.split()
        tuppleList = []
        for instance in word:
            if (instance.lower() in directions): 
                tuppleList.append(("direction", instance))
            elif (instance.lower() in verbs):
                tuppleList.append(("verb", instance))
            elif (instance.lower() in stop):
                tuppleList.append(("stop", instance))
            elif (instance.lower() in nouns):
                tuppleList.append(("noun", instance))
            elif (convert_number(instance)):
                tuppleList.append(("number", convert_number(instance)))
            else:
                tuppleList.append(("error", instance))

        return tuppleList
    except ValueError:
        return None
