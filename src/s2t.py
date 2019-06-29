import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def speech2text(recognizer, source):
    # recognize speech using Google Speech Recognition
    audio = recognizer.listen(source)
    heard = recognizer.recognize_google(audio)
    logger.debug(f"Heard {heard}")
    return heard

