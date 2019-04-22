# Guess That Picture game

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


class Quiz():
    def __init__(self, questions):
        self.questions = questions
        self.correct = []
        self.incorrect = []
        self.makeSounds()

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
        self.incorrect.append(question)

    def makeSounds(self):
        self.gameSounds = {}


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

    printNow("Choose 'topic':")
    for index, topic in enumerate(topics):
        printNow("%s. %s" % (index + 1, topic))

    while True:
        response = requestString("Enter your answer")
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
