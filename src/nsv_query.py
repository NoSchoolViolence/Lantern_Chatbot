from s2t import speech2text
import speech_recognition as sr
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Query:
    def __init__(self, engine, recognizer, source):
        self.recognizer = recognizer
        self.source = source
        self.engine = engine
        self.subject = None
        self.verb = None
        self.subject_age = None
        self.subject_gender = None
        self.subject_grade = None
        self.subject_poss = None
        self.subject_grade_level = None # elementry, middle, high, university
        self.subject_location = None # northwest, northeast, southeast, southwest
        self.subject_behavior_type = None # physical or emotional
        self.subject_behavior_occurrence = None # once or multiple

    def get_missing_fields(self):
        if self.subject_age is None:
            self.get_age()
        if self.subject_gender is None:
            self.get_gender()
        if self.subject_grade is None:
            self.get_grade()
        if self.subject_behavior_type is None:
            self.get_behavior_type()
        if self.subject_behavior_occurrence is None:
            self.get_behavior_occurrence()

    @staticmethod
    def invert_poss(poss):
        if poss is None:
            return ""

        if poss.lower() == "my":
            return "your"
        if poss.lower() == "your":
            return "my"
        return poss

    def get_age(self):
        self.engine.say(f"What is {self.invert_poss(self.subject_poss)} {self.subject}'s age?")
        self.engine.runAndWait()
        try:
            self.subject_age = int(speech2text(self.recognizer, self.source))
        except sr.UnknownValueError:
            logger.info("Unable to understand age")

    def get_gender(self):
        self.engine.say(f"What is {self.invert_poss(self.subject_poss)} {self.subject}'s gender?")
        self.engine.runAndWait()
        try:
            self.subject_gender = speech2text(self.recognizer, self.source)
        except sr.UnknownValueError:
            logger.info("Unable to understand gender")

    def get_grade(self):
        self.engine.say(f"What grade is {self.invert_poss(self.subject_poss)} {self.subject} in?")
        self.engine.runAndWait()
        try:
            self.subject_grade = speech2text(self.recognizer, self.source)
        except sr.UnknownValueError:
            logger.info("Unable to understand grade")

    # TODO insert logic for grade level

    def get_behavior_type(self):
        self.engine.say(f"Is the behavior exhibited by {self.invert_poss(self.subject_poss)} {self.subject} physical or emotional?")
        self.engine.runAndWait()
        try:
            self.subject_behavior_type = speech2text(self.recognizer, self.source)
        except sr.UnknownValueError:
            logger.info("Unable to understand behavior_type")

    def get_behavior_occurrence(self):
        self.engine.say(f"How many times in the past year has {self.invert_poss(self.subject_poss)} {self.subject} experienced this behavior?")
        self.engine.runAndWait()
        try:
            self.subject_behavior_occurrence = speech2text(self.recognizer, self.source)
        except sr.UnknownValueError:
            logger.info("Unable to understand behavior_occurrence")

    def __str__(self):
        return f"{self.subject}, {self.verb}, {self.subject_age}, {self.subject_gender}, {self.subject_grade}, " \
            f"{self.subject_grade_level}, {self.subject_location}, {self.subject_behavior_type}, " \
            f"{self.subject_behavior_occurrence}"
