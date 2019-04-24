# Guess That Picture game
import os
import random

PATH = os.path.dirname(os.path.realpath(__file__))
EXIT_STR = "exit"

# define the map of topics > questions > answers for the quiz game
GAME_OPTIONS = [
    {
        'topic': 'Car parts',
        'questions': [
            {
                'value': 'What engine component is this?',
                'image_path': 'pictures/crankshaft.jpg',
                'answers': [
                    {
                        'value': 'Axle rod',
                        'is_correct': False,
                    },
                    {
                        'value': 'Camshaft',
                        'is_correct': False,
                    },
                    {
                        'value': 'Crankshaft',
                        'is_correct': True,
                    },
                ]
            },
            {
                'value': 'What transmission component is this?',
                'image_path': 'pictures/clutchPlate.jpg',
                'answers': [
                    {
                        'value': 'Frisbee Wheel',
                        'is_correct': False,
                    },
                    {
                        'value': 'Clutch Plate',
                        'is_correct': True,
                    },
                    {
                        'value': 'Flux Capacitor',
                        'is_correct': False,
                    },
                ]
            },
            {
                'value': 'What suspension component is this?',
                'image_path': 'pictures/controlArm.jpg',
                'answers': [
                    {
                        'value': 'Control Arm',
                        'is_correct': True,
                    },
                    {
                        'value': 'Swing Arm',
                        'is_correct': False,
                    },
                    {
                        'value': 'Wish Bone',
                        'is_correct': False,
                    },
                ]
            },
            {
                'value': 'What engine component is this?',
                'image_path': 'pictures/engineControlUnit.jpg',
                'answers': [
                    {
                        'value': 'AI Unit',
                        'is_correct': False,
                    },
                    {
                        'value': 'Auto Drive Control Unit',
                        'is_correct': False,
                    },
                    {
                        'value': 'Engine Control Unit',
                        'is_correct': True,
                    },
                ]
            },
            {
                'value': 'What brake componenet is this?',
                'image_path': 'pictures/brakeRotor.jpg',
                'answers': [
                    {
                        'value': 'Saw Blade',
                        'is_correct': False,
                    },
                    {
                        'value': 'Brake Rotor',
                        'is_correct': True,
                    },
                    {
                        'value': 'Road Rage Defense Unit',
                        'is_correct': False,
                    },
                ]
            },
        ]
    },
    {
        'topic': 'Human anatomy',
        'questions': [
            {
                'value': 'Which human organ filters blood in a pair?',
                'image_path': 'pictures/kidneys.png',
                'answers': [
                    {
                        'value': 'lungs',
                        'is_correct': False,
                    },
                    {
                        'value': 'bladder',
                        'is_correct': False,
                    },
                    {
                        'value': 'kidneys',
                        'is_correct': True,
                    },
                ]
            },
            {
                'value': 'Which organ is responsible for pumping blood?',
                'image_path': 'pictures/heart.jpg',
                'answers': [
                    {
                        'value': 'intestines',
                        'is_correct': False,
                    },
                    {
                        'value': 'heart',
                        'is_correct': True,
                    },
                    {
                        'value': 'stomach',
                        'is_correct': False,
                    },
                ]
            },
            {
                'value': 'Which organ is a muscular sack in the pelvis?',
                'image_path': 'pictures/bladder.jpeg',
                'answers': [
                    {
                        'value': 'kidneys',
                        'is_correct': False,
                    },
                    {
                        'value': 'bladder',
                        'is_correct': True,
                    },
                    {
                        'value': 'intestines',
                        'is_correct': False,
                    },
                ]
            },
            {
                'value': 'Which organ aids in digestion?',
                'image_path': 'pictures/intestines.jpg',
                'answers': [
                    {
                        'value': 'kidneys',
                        'is_correct': False,
                    },
                    {
                        'value': 'bladder',
                        'is_correct': False,
                    },
                    {
                        'value': 'intestines',
                        'is_correct': True,
                    },
                ]
            },
        ]
    },
    {
        'topic': 'Rare animals',
        'questions': [
            {
                'value': 'What kind of animal is a vaquita?',
                'image_path': 'pictures/vaquita.jpg',
                'answers': [
                    {
                        'value': 'A desert reptile',
                        'is_correct': False,
                    },
                    {
                        'value': 'A marine mammal',
                        'is_correct': True,
                    },
                    {
                        'value': 'A taco-shaped bird',
                        'is_correct': False,
                    },
                ]
            },
            {
                'value': 'What is Poecilotheria metallica?',
                'image_path': 'pictures/metallica.jpg',
                'answers': [
                    {
                        'value': 'A type of tarantula',
                        'is_correct': True,
                    },
                    {
                        'value': 'A bird',
                        'is_correct': False,
                    },
                    {
                        'value': 'A loud rock band',
                        'is_correct': False,
                    },
                ]
            },
            {
                'value': 'The Saola is often called what?',
                'image_path': 'pictures/saola.jpg',
                'answers': [
                    {
                        'value': 'Chilean watergoblin',
                        'is_correct': False,
                    },
                    {
                        'value': 'Asian unicorn',
                        'is_correct': True,
                    },
                    {
                        'value': 'African treehugger',
                        'is_correct': False,
                    },
                ]
            },
            {
                'value': 'What solenodons look like?',
                'image_path': 'pictures/shrews.jpg',
                'answers': [
                    {
                        'value': 'Parakeets',
                        'is_correct': False,
                    },
                    {
                        'value': 'Horses',
                        'is_correct': False,
                    },
                    {
                        'value': 'Shrews',
                        'is_correct': True,
                    },
                ]
            },
            {
                'value': 'What kind of animal is the Lycaon pictus?',
                'image_path': 'pictures/pictus.jpg',
                'answers': [
                    {
                        'value': 'African wild dog',
                        'is_correct': True,
                    },
                    {
                        'value': 'Bonobo',
                        'is_correct': False,
                    },
                    {
                        'value': 'Blue whale',
                        'is_correct': False,
                    },
                ]
            },
        ]
    },
]


# adds black frame around an image
def addBlackFrame(picture):
    width = getWidth(picture)
    height = getHeight(picture)
    thickness = 20
    addRectFilled(picture, 0, 0, width, thickness, black)
    addRectFilled(picture, 0, height - thickness, width, thickness, black)
    addRectFilled(picture, 0, 0, thickness, height, black)
    addRectFilled(picture, width - thickness, 0, thickness, height, black)
    return picture

# Function that clips a given sound
def clip(source, start, end):
    target = makeEmptySound(end - start, int(getSamplingRate(source)))
    targetIndex = 0
    for index in range(start, end):
        value = getSampleValueAt(source, index)
        setSampleValueAt(target, targetIndex, value)
        targetIndex = targetIndex + 1
    return target

# Function to copy source to target
def copy(source, target, start):
    targetLength = getLength(target)
    for index in range(0, getLength(source)):
        targetIndex = start + index
        if targetIndex >= targetLength:
            break
        value = getSampleValueAt(source, index)
        setSampleValueAt(target, targetIndex, value)
    return target

#  Class to handle
class Quiz():
    def __init__(self, questions):
        self.questions = questions
        self.correct = []
        self.incorrect = []
        self.game_sounds = self.makeGameSounds()

    # iterates over questions and prompt user
    def start(self):
        for question in self.questions:
            self.printQuestion(question)
            response = self.handleInput(question)

            if response == EXIT_STR:
                printNow("Thanks for playing!")
                return None

            answer = question.getAnswer(response - 1)

            if answer.is_correct:
                self.handleCorrectAnswer(question)
            else:
                self.handleIncorrectAnswer(question)

        # Question taking is over, display some results
        if len(self.correct) > len(self.incorrect):
            self.handleWin()
        else:
            self.handleLose()

    # pretty print questions
    def printQuestion(self, question):
        show(question.getScrambledImage())
        printNow(question.question)
        for index, answer in enumerate(question.getAnswerValues()):
            print("%s. %s" % (index + 1, answer))

    # handle user input
    def handleInput(self, question):
        printNow("Please enter your answer now:")
        while True:
            response = raw_input()
            if response == EXIT_STR:
                break
            elif response and int(response) in range(1, len(question.answers) + 1):
                response = int(response)
                break
            else:
                printNow("Unrecognized input. Please try again.")

        return response

    # check whether qucrrent question is last
    def isLastQuestion(self):
        return len(self.correct) + len(self.incorrect) == len(self.questions)

    # handle the correct answer
    def handleCorrectAnswer(self, question):
        self.correct.append(question)
        show(question.getUnscrambledImage())

        if not self.isLastQuestion():
            printNow("You are correct!\n")
            reaction = random.choice(self.game_sounds['yays'])
            play(reaction)

    # handle the wrong answer
    def handleIncorrectAnswer(self, question):
        self.incorrect.append(question)
        show(question.getUnscrambledImage())

        if not self.isLastQuestion():
            printNow("Sorry, wrong answer!\n")
            reaction = random.choice(self.game_sounds['oohs'])
            play(reaction)

    # handle the winning condition
    def handleWin(self):
        play(self.game_sounds['win'][0])
        showInformation("You have won the game. Well done!\n"
                        "Correct answers: %s\n"
                        "Incorrect answers: %s" % (
                            len(self.correct), len(self.incorrect))
                        )

    # handle the losing condition
    def handleLose(self):
        play(self.game_sounds['lose'][0])
        showInformation("Sorry, you lost the game. Better luck next time!\n"
                        "Correct answers: %s\n"
                        "Incorrect answers: %s" % (
                            len(self.correct), len(self.incorrect))
                        )

    # generate all game sounds
    def makeGameSounds(self):
        samplingRate = 44100
        oohs = makeSound("%s/sounds/oohs.wav" % PATH)
        yays = makeSound("%s/sounds/yays.wav" % PATH)
        thanks = makeSound("%s/sounds/thanks.wav" % PATH)
        applause = makeSound("%s/sounds/applause.wav" % PATH)
        win = makeEmptySound(getLength(applause) +
                             getLength(thanks), samplingRate)
        win = copy(applause, win, 0)
        win = copy(thanks, win, getLength(applause))
        nooo = makeSound("%s/sounds/nooo.wav" % PATH)
        lose = makeEmptySound(
            getLength(nooo) + getLength(thanks), samplingRate)
        lose = copy(nooo, lose, 0)
        lose = copy(thanks, lose, getLength(nooo))

        return {
            "yays": [
                clip(yays, 1998, 103563),
                clip(yays, 106893, 206460)
            ],
            "oohs": [
                clip(oohs, 7108, 72857),
                clip(oohs, 99512, 184808),
                clip(oohs, 262996, 341184),
                clip(oohs, 355400, 451358),
                clip(oohs, 490452, 584633),
                clip(oohs, 611288, 748117),
                clip(oohs, 787211, 908047),
                clip(oohs, 963134, 1119510),
            ],
            "lose": [
                lose,
            ],
            "win": [
                win,
            ],
        }


# a class responsible for questions
class Question():
    def __init__(self, question, answers, image_path=''):
        self.question = question
        self.answers = answers
        self.image_path = image_path

    # scramble an image by slicing and randomising it
    def getScrambledImage(self):
        slice_num = 8
        picture = makePicture("%s/%s" % (PATH, self.image_path))
        width = getWidth(picture)
        height = getHeight(picture)
        scrambled_picture = makeEmptyPicture(width, height)
        slice_width = width / slice_num
        slice_height = height / slice_num
        slices = range(0, slice_num * slice_num)
        random.shuffle(slices)
        current_slice = 0

        for x in range(0, slice_num):
            for y in range(0, slice_num):
                col = slices[current_slice] % slice_num
                row = slices[current_slice] // slice_num
                for orig_x in range(x * slice_width, slice_width + (x * slice_width)):
                    for orig_y in range(y * slice_height, slice_height + (y * slice_height)):
                        px = getPixel(picture, orig_x, orig_y)
                        color = getColor(px)
                        setColor(getPixel(scrambled_picture, (orig_x - (x * slice_width)) + (
                            col * slice_width), (orig_y - (y * slice_height)) + (row * slice_height)), color)
                current_slice += 1

        scrambled_picture = addBlackFrame(scrambled_picture)
        return scrambled_picture

    # get all answer values for the question
    def getAnswerValues(self):
        return [answer.value for answer in self.answers]

    # get a specific answer
    def getAnswer(self, index):
        return self.answers[index]

    # get the opriginal unscrambled picrture
    def getUnscrambledImage(self):
        return makePicture("%s/%s" % (PATH, self.image_path))


# basic class responsible for answers
class Answer():
    def __init__(self, value, is_correct=False):
        self.value = value
        self.is_correct = is_correct


# prompts user to choose game topic
def chooseGameTopic():
    topics = [option['topic'] for option in GAME_OPTIONS]

    printNow("Choose topic:")
    for index, topic in enumerate(topics):
        printNow("%s. %s" % (index + 1, topic))

    while True:
        response = raw_input()
        if response == EXIT_STR:
            return response
        elif response and int(response) in range(1, len(topics) + 1):
            return int(response) - 1


# shows game intro
def intro():
    intro = makeSound("%s/sounds/intro.wav" % PATH)
    play(intro)
    showInformation("Welcome to the Guess That Picture quiz.\n"
                    "To play this game please first select a topic\n"
                    "Then pick correct answer to questions presented or type \"exit\" to quit.\n\n"
                    "Good luck!")


# main function
def main():
    intro()

    # choose the topic
    topic = chooseGameTopic()
    if topic == EXIT_STR:
        printNow("Thanks for playing!")
    else:
        # load questions
        questions = GAME_OPTIONS[topic]['questions']
        quiz = Quiz([Question(question['value'], [Answer(value=answer['value'], is_correct=answer['is_correct'])
                                                  for answer in question['answers']], question['image_path']) for question in questions])
        quiz.start()


main()
