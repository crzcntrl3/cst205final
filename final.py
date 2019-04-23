# Guess That Picture game
import os
import random

PATH = os.path.dirname(os.path.realpath(__file__))

GAME_OPTIONS = [
    {
        'topic': 'Car parts',
        'questions': [
            {
                'value': 'The part that is responsible for something',
                'image_path': 'pictures/axle.jpg',
                'answers': [
                    {
                        'value': 'air filter',
                        'is_correct': False,
                    },
                    {
                        'value': 'clutch',
                        'is_correct': False,
                    },
                    {
                        'value': 'axle',
                        'is_correct': True,
                    },
                ]
            },
            {
                'value': 'The part that makes the car something',
                'image_path': 'pictures/compressor.jpg',
                'answers': [
                    {
                        'value': 'spark plug',
                        'is_correct': False,
                    },
                    {
                        'value': 'compressor',
                        'is_correct': True,
                    },
                    {
                        'value': 'radiator',
                        'is_correct': False,
                    },
                ]
            },
            {
                'value': 'What does something to a car',
                'image_path': 'pictures/piston.jpg',
                'answers': [
                    {
                        'value': 'piston',
                        'is_correct': True,
                    },
                    {
                        'value': 'jack',
                        'is_correct': False,
                    },
                    {
                        'value': 'muffler',
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
                'value': 'What makes humans do',
                'image_path': 'pictures/kidneys.jpg',
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
                'value': 'What is responsible for human',
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
                'value': 'What is human',
                'image_path': 'pictures/kidneys.jpg',
                'answers': [
                    {
                        'value': 'kidneys',
                        'is_correct': True,
                    },
                    {
                        'value': 'bladder',
                        'is_correct': False,
                    },
                    {
                        'value': 'intestines',
                        'is_correct': False,
                    },
                ]
            },
        ]
    }
]


def clip(source, start, end):
    target = makeEmptySound(end - start, int(getSamplingRate(source)))
    targetIndex = 0
    for index in range(start, end):
        value = getSampleValueAt(source, index)
        setSampleValueAt(target, targetIndex, value)
        targetIndex = targetIndex + 1
    return target

def copy(source, target, start):
    targetLength = getLength(target)
    for index in range(0, getLength(source)):
        targetIndex = start + index
        if targetIndex >= targetLength:
            break
        value = getSampleValueAt(source, index)
        setSampleValueAt(target, targetIndex, value)
    return target
 
class Quiz():
    def __init__(self, questions):
        self.questions = questions
        self.correct = []
        self.incorrect = []
        self.makeGameSounds()

    def start(self):
        # Loop through questions and get answers for each
        for question in self.questions:
            self.printQuestion(question)
            response = self.handleInput(question)
            answer = question.get_answer(response - 1)
            
            if answer.is_correct:
                self.handleCorrectAnswer(question)
            else:
                self.handleIncorrectAnswer(question)

        # Question taking is over, display some results
        if len(self.correct) > len(self.incorrect):
            self.handleWin()
        else:
            self.handleLose()

    def printQuestion(self, question):
        printNow(question.question)
        for index, answer in enumerate(question.get_answer_values()):
            print("%s. %s" % (str(index + 1), answer))

    def handleInput(self, question):
        printNow("Enter your answer")
        while True:
            response = raw_input()
            if response and int(response) in range(1, len(question.answers) + 1):
                response = int(response)
                print('\n')
                break
            else:
                printNow("Please enter a valid response")

        return response
        
    def isLastQuestion(self):
        return len(self.correct) + len(self.incorrect) == len(self.questions)

    def handleCorrectAnswer(self, question):
        self.correct.append(question)
        
        if not self.isLastQuestion():
          printNow("You are right!\n")
          reaction = random.choice(self.gameSounds['yays'])
          play(reaction)


    def handleIncorrectAnswer(self, question):
        self.incorrect.append(question)

        if not self.isLastQuestion():
            printNow("Wrong answer!\n")
            reaction = random.choice(self.gameSounds['oohs'])
            play(reaction)
        
    def handleWin(self):
        play(self.gameSounds['win'][0])
        showInformation("You win!\n"
                        "Correct answers: %s\n"
                        "Incorrect answers: %s" % (len(self.correct), len(self.incorrect))
                       )
        
    def handleLose(self):
        play(self.gameSounds['lose'][0])
        showInformation("You lose!\n"
                        "Correct answers: %s\n"
                        "Incorrect answers: %s" % (len(self.correct), len(self.incorrect))
                       )

    def makeGameSounds(self):
        samplingRate = 44100
        oohs = makeSound("%s/sounds/oohs.wav" % PATH)
        yays = makeSound("%s/sounds/yays.wav" % PATH)
        thanks = makeSound("%s/sounds/thanks.wav" % PATH)
        applause = makeSound("%s/sounds/applause.wav" % PATH)
        win = makeEmptySound(getLength(applause) + getLength(thanks), samplingRate)
        win = copy(applause, win, 0)
        win = copy(thanks, win, getLength(applause))
        nooo = makeSound("%s/sounds/nooo.wav" % PATH)
        lose = makeEmptySound(getLength(nooo) + getLength(thanks), samplingRate)
        lose = copy(nooo, lose, 0)
        lose = copy(thanks, lose, getLength(nooo))
        
        self.gameSounds = {
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


class Question():
    def __init__(self, question, answers, image_path=''):
        self.question = question
        self.answers = answers
        self.scramble_image(image_path)

    def scramble_image(self, image_path):
        return

    def get_answer_values(self):
        return [answer.value for answer in self.answers]

    def get_correct_answer(self):
        for answer in self.answers:
            if answer.is_correct:
                return answer

    def get_answer(self, index):
        return self.answers[index]


class Answer():
    def __init__(self, value, is_correct=False):
        self.value = value
        self.is_correct = is_correct


def chooseGameTopic():
    topics = [option['topic'] for option in GAME_OPTIONS]

    printNow("Choose topic:")        
    for index, topic in enumerate(topics):
        printNow("%s. %s" % (index + 1, topic))

    while True:
        response = raw_input()
        if response and int(response) in range(1, len(topics) + 1):
            break
    return int(response) - 1

def intro():
    intro = makeSound("%s/sounds/intro.wav" % PATH)
    play(intro)
    showInformation("Welcome to the quiz")
    
def game():
    intro()

    # choose the topic
    topic = chooseGameTopic()

    # load questions
    questions = GAME_OPTIONS[topic]['questions']
    quiz = Quiz([Question(question['value'], [Answer(value=answer['value'], is_correct=answer['is_correct']) for answer in question['answers']]) for question in questions])
    quiz.start()


game()
