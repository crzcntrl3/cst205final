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
class puzzle:
  def __init__(self, pic):
    self.pic = makePicture(pic)
    
  #Makes the individual slice of the original image
  def slicing(self, pic, startX, startY, endX, endY):
    x = abs(startX-endX)
    y = abs(startY-endY)
    slicedPic = makeEmptyPicture(x,y)
    #creates arrays to hold the information of the original and empty images
    originalPixels = []
    slicedPixels = []
    #grabs pixel information of the original image and store it in its corresponding array
    for originalX in range(startX, endX):
      for originalY in range(startY, endY):
        originalP = getPixel(self.pic, originalX, originalY)
        originalPixels.append(originalP)
    #grabs pixel information of the empty image and store it in its corresponding array
    for slicedX in range(0, x):
      for slicedY in range(0, y):
        slicedP = getPixel(slicedPic, slicedX, slicedY)
        slicedPixels.append(slicedP)
    #uses the zip() to combine the two arrays and steps through each pair in the array
    for combinePixels in zip(originalPixels,slicedPixels):
      #grabs each element of the zipped array
      origPix = combinePixels[0]
      slicedPix = combinePixels[1]
      #sets the color to the empty image
      setColor(slicedPix,getColor(origPix))
    return slicedPic
    
  #slices the image into 12 peices
  def puzzleSlices(self, pic):
    w = getWidth(self.pic)
    h = getHeight(self.pic)
    sectionArray = []
  
    #First Quater
    section1 = self.slicing(self.pic, 0, 0,w/3,h/4)
    section2 = self.slicing(self.pic,(w/3),0,(w*2)/3,h/4)
    section3 = self.slicing(self.pic,(w*2)/3,0,w,h/4)
    #Second Quater
    section4 = self.slicing(self.pic,0,h/4,w/3,(h*2)/4)
    section5 = self.slicing(self.pic,(w/3),h/4,(w*2)/3,(h*2)/4)
    section6 = self.slicing(self.pic,(w*2)/3,h/4,w,(h*2)/4)
    #Third Quater
    section7 = self.slicing(self.pic,0,(h*2)/4,w/3,(h*3)/4)
    section8 = self.slicing(self.pic,(w/3),(h*2)/4,(w*2)/3,(h*3)/4)
    section9 = self.slicing(self.pic,(w*2)/3,(h*2)/4,w,(h*3)/4)
    #Fourth Quater
    section10 = self.slicing(self.pic,0,(h*3)/4,w/3,h)
    section11 = self.slicing(self.pic,(w/3),(h*3)/4,(w*2)/3,h)
    section12 = self.slicing(self.pic,(w*2)/3,(h*3)/4,w,h)
  
    #creates an arrays of the image slices
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

  #Copy function
  def arrange(self,section, whole, placeX, placeY):
    w = getWidth(section)
    h = getHeight(section)
  
    sectionPixels = []
    wholePixels  = []
  
    for secX in range(0, w):
      for secY in range(0, h):
        secP = getPixel(section, secX, secY)
        sectionPixels.append(secP)
    for wholeX in range(placeX, placeX+w):
      for wholeY in range(placeY, placeY+h):
        wholeP = getPixel(whole, wholeX, wholeY)
        wholePixels.append(wholeP)
    for combine in zip(sectionPixels,wholePixels):
      secPix = combine[0]
      wholePix = combine[1]
      setColor(wholePix,getColor(secPix))
    return wholePix


  #Creates the puzzle image
  def scrambled(self):
    w = getWidth(self.pic)
    h = getHeight(self.pic)
    section = self.puzzleSlices(self.pic)
  
    #Creates an array of 12 numbers 0-11 with no repeats
    r = random.sample(range(12),12)
  
    puzzle = makeEmptyPicture(w,h)
    self.arrange(section[r[0]],puzzle,0,0)
    self.arrange(section[r[1]],puzzle,w/3,0)
    self.arrange(section[r[2]],puzzle,(w*2)/3,0)
  
    self.arrange(section[r[3]],puzzle,0,h/4)
    self.arrange(section[r[4]],puzzle,w/3,h/4)
    self.arrange(section[r[5]],puzzle,(w*2)/3,h/4)
  
    self.arrange(section[r[6]],puzzle,0,(h*2)/4)
    self.arrange(section[r[7]],puzzle,w/3,(h*2)/4)
    self.arrange(section[r[8]],puzzle,(w*2)/3,(h*2)/4)
  
    self.arrange(section[r[9]],puzzle,0,(h*3)/4)
    self.arrange(section[r[10]],puzzle,w/3,(h*3)/4)
    self.arrange(section[r[11]],puzzle,(w*2)/3,(h*3)/4)
    
    return puzzle

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

        # Question taking over, display some results
        showInformation("Thank you for taking the quiz, here are your results!\n"
                        "Correct 'answers': %s\n"
                        "Incorrect 'answers': %s" % (str(len(self.correct)), str(len(self.incorrect))))

    def printQuestion(self, question):
        printNow(question.question)
        for index, answer in enumerate(question.get_answer_values()):
            print("%s. %s" % (str(index + 1), answer))

    def handleInput(self, question):
        while True:
            response = requestString("Enter your answer")
            if response and int(response) in range(1, len(question.answers) + 1):
                response = int(response)
                print('\n')
                break
            else:
                print("Please enter a valid response")

        return response

    def handleCorrectAnswer(self, question):
        printNow("You are right!\n")
        self.correct.append(question)

    def handleIncorrectAnswer(self, question):
        printNow("Wrong answer!\n")
        play(self.gameSounds['gasp'])
        self.incorrect.append(question)

    def makeGameSounds(self):
        self.gameSounds = {
          "gasp": makeSound("%s/sounds/gasp2.wav" % PATH)
        }


class Question():
    def __init__(self, question, answers, image_path=''):
        self.question = question
        self.answers = answers
        self.scramble_image(image_path)

    def scramble_image(self, image_path):
        pic = puzzle(image_path)
        picture = pic.scrambled()
        return picture

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
        response = requestString("Choose topic")
        if response and int(response) in range(1, len(topics) + 1):
            break
    return int(response) - 1

def game():
    showInformation("Welcome to the quiz")

    # choose the topic
    topic = chooseGameTopic()

    # load questions
    questions = GAME_OPTIONS[topic]['questions']
    quiz = Quiz([Question(question['value'], [Answer(value=answer['value'], is_correct=answer['is_correct']) for answer in question['answers']]) for question in questions])
    quiz.start()


game()
