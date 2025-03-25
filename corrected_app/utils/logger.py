import logging

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

console_handler = logging.StreamHandler()
console_handler.setLevel("DEBUG")

formatter = logging.Formatter("{asctime} [{levelname}]: {message}", style="{", datefmt="%Y-%m-%d %H:%M")
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
