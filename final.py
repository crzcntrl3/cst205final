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
                'image_path': 'pictures/bladder.jpg',
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
        ]
    }
]


class Puzzle:
    def __init__(self, image_path):
        self.pic = makePicture("%s/%s" % (PATH, image_path))

    # Makes the individual slice of the original image
    def slicing(self, pic, startX, startY, endX, endY):
        x = abs(startX-endX)
        y = abs(startY-endY)
        slicedPic = makeEmptyPicture(x, y)
        # creates arrays to hold the information of the original and empty images
        originalPixels = []
        slicedPixels = []
        # grabs pixel information of the original image and store it in its corresponding array
        for originalX in range(startX, endX):
            for originalY in range(startY, endY):
                originalP = getPixel(self.pic, originalX, originalY)
                originalPixels.append(originalP)
        # grabs pixel information of the empty image and store it in its corresponding array
        for slicedX in range(0, x):
            for slicedY in range(0, y):
                slicedP = getPixel(slicedPic, slicedX, slicedY)
                slicedPixels.append(slicedP)
        # uses the zip() to combine the two arrays and steps through each pair in the array
        for combinePixels in zip(originalPixels, slicedPixels):
            # grabs each element of the zipped array
            origPix = combinePixels[0]
            slicedPix = combinePixels[1]
            # sets the color to the empty image
            setColor(slicedPix, getColor(origPix))
        return slicedPic

    # slices the image into 12 peices
    def puzzleSlices(self, pic):
        w = getWidth(self.pic)
        h = getHeight(self.pic)
        sectionArray = []

        # First Quater
        section1 = self.slicing(self.pic, 0, 0, w/3, h/4)
        section2 = self.slicing(self.pic, (w/3), 0, (w*2)/3, h/4)
        section3 = self.slicing(self.pic, (w*2)/3, 0, w, h/4)
        # Second Quater
        section4 = self.slicing(self.pic, 0, h/4, w/3, (h*2)/4)
        section5 = self.slicing(self.pic, (w/3), h/4, (w*2)/3, (h*2)/4)
        section6 = self.slicing(self.pic, (w*2)/3, h/4, w, (h*2)/4)
        # Third Quater
        section7 = self.slicing(self.pic, 0, (h*2)/4, w/3, (h*3)/4)
        section8 = self.slicing(self.pic, (w/3), (h*2)/4, (w*2)/3, (h*3)/4)
        section9 = self.slicing(self.pic, (w*2)/3, (h*2)/4, w, (h*3)/4)
        # Fourth Quater
        section10 = self.slicing(self.pic, 0, (h*3)/4, w/3, h)
        section11 = self.slicing(self.pic, (w/3), (h*3)/4, (w*2)/3, h)
        section12 = self.slicing(self.pic, (w*2)/3, (h*3)/4, w, h)

        # creates an arrays of the image slices
        sectionArray.append(section1)
        sectionArray.append(section2)
        sectionArray.append(section3)
        sectionArray.append(section4)
        sectionArray.append(section5)
        sectionArray.append(section6)
        sectionArray.append(section7)
        sectionArray.append(section8)
        sectionArray.append(section9)
        sectionArray.append(section10)
        sectionArray.append(section11)
        sectionArray.append(section12)

        return sectionArray

    # Copy function
    def arrange(self, section, whole, placeX, placeY):
        w = getWidth(section)
        h = getHeight(section)

        sectionPixels = []
        wholePixels = []

        for secX in range(0, w):
            for secY in range(0, h):
                secP = getPixel(section, secX, secY)
                sectionPixels.append(secP)
        for wholeX in range(placeX, placeX+w):
            for wholeY in range(placeY, placeY+h):
                wholeP = getPixel(whole, wholeX, wholeY)
                wholePixels.append(wholeP)
        for combine in zip(sectionPixels, wholePixels):
            secPix = combine[0]
            wholePix = combine[1]
            setColor(wholePix, getColor(secPix))
        return wholePix

    # Creates the puzzle image

    def scrambled(self):
        w = getWidth(self.pic)
        h = getHeight(self.pic)
        section = self.puzzleSlices(self.pic)

        # Creates an array of 12 numbers 0-11 with no repeats
        r = random.sample(range(12), 12)

        puzzle = makeEmptyPicture(w, h)
        self.arrange(section[r[0]], puzzle, 0, 0)
        self.arrange(section[r[1]], puzzle, w/3, 0)
        self.arrange(section[r[2]], puzzle, (w*2)/3, 0)

        self.arrange(section[r[3]], puzzle, 0, h/4)
        self.arrange(section[r[4]], puzzle, w/3, h/4)
        self.arrange(section[r[5]], puzzle, (w*2)/3, h/4)

        self.arrange(section[r[6]], puzzle, 0, (h*2)/4)
        self.arrange(section[r[7]], puzzle, w/3, (h*2)/4)
        self.arrange(section[r[8]], puzzle, (w*2)/3, (h*2)/4)

        self.arrange(section[r[9]], puzzle, 0, (h*3)/4)
        self.arrange(section[r[10]], puzzle, w/3, (h*3)/4)
        self.arrange(section[r[11]], puzzle, (w*2)/3, (h*3)/4)

        return puzzle


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
        self.game_sounds = self.makeGameSounds()

    def start(self):
        # Loop through questions and get answers for each
        for question in self.questions:
            self.printQuestion(question)
            response = self.handleInput(question)
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

    def printQuestion(self, question):
        show(question.getScrambledImage())
        printNow(question.question)
        for index, answer in enumerate(question.getAnswerValues()):
            print("%s. %s" % (index + 1, answer))

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
        show(question.getUnscrambledImage())

        if not self.isLastQuestion():
            printNow("You are right!\n")
            reaction = random.choice(self.game_sounds['yays'])
            play(reaction)

    def handleIncorrectAnswer(self, question):
        self.incorrect.append(question)
        show(question.getUnscrambledImage())

        if not self.isLastQuestion():
            printNow("Wrong answer!\n")
            reaction = random.choice(self.game_sounds['oohs'])
            play(reaction)

    def handleWin(self):
        play(self.game_sounds['win'][0])
        showInformation("You win!\n"
                        "Correct answers: %s\n"
                        "Incorrect answers: %s" % (
                            len(self.correct), len(self.incorrect))
                        )

    def handleLose(self):
        play(self.game_sounds['lose'][0])
        showInformation("You lose!\n"
                        "Correct answers: %s\n"
                        "Incorrect answers: %s" % (
                            len(self.correct), len(self.incorrect))
                        )

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


class Question():
    def __init__(self, question, answers, image_path=''):
        self.question = question
        self.answers = answers
        self.image_path = image_path

    def getScrambledImage(self):
        pic = Puzzle(self.image_path)
        picture = pic.scrambled()
        return picture

    def getAnswerValues(self):
        return [answer.value for answer in self.answers]

    def getAnswer(self, index):
        return self.answers[index]
        
    def getUnscrambledImage(self):
        return makePicture("%s/%s" % (PATH, self.image_path))
    


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
    quiz = Quiz([Question(question['value'], [Answer(value=answer['value'], is_correct=answer['is_correct'])
                                              for answer in question['answers']], question['image_path']) for question in questions])
    quiz.start()


game()
