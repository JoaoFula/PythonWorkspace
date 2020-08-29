#! C:/Joao/PythonDocs/

storyFormat = '''
Once upon a time, deep in the ancient jungle, there lived a {animal}.
This {animal} liked to eat {food}, but the jungle had very little
{food} to offer. One day, an explorer found the {animal} and discovered
it liked {food}. The explorer took the {animal} back to {city}, where it
could eat as much {food} as it wanted. However, the {animal} became
homesick, so the explorer brought it back to the jungle, leaving a large
supply of {food}.

The End
'''

def tellStory():
    ''' Function that replaces the animal, food and city in the
storyFormat variable by saving the new version into the variable
story and printing it
    '''
    userPicks = dict()
    addPick('animal', userPicks)
    addPick('food', userPicks)
    addPick('city', userPicks)
    story = storyFormat.format(**userPicks)
    print(story)

def addPick(cue, dictionary):
    ''' Prompt a user response using the cue string and place the
cue-response pair in the dictionary
    '''
    prompt = 'Enter an example for ' + cue + ': '
    response = input(prompt)
    dictionary[cue] = response

tellStory()
input('Press Enter to end the program.')
