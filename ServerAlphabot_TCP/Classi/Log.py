import logging


class Log:
    def __init__(self, nomeFile):
        self.loggerFile = logging.getLogger('LogFile')
        self.loggerFile.setLevel(logging.DEBUG)
        fhFile = logging.FileHandler(nomeFile, 'w')
        fhFile.setLevel(logging.DEBUG)
        self.loggerFile.addHandler(fhFile)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fhFile.setFormatter(formatter)
        self.loggerFile.addHandler(fhFile)

        self.loggerConsole = logging.getLogger('LogConsole')
        self.loggerConsole.setLevel(logging.DEBUG)
        fhConsole = logging.StreamHandler()
        fhConsole.setLevel(logging.DEBUG)
        self.loggerConsole.addHandler(fhConsole)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fhConsole.setFormatter(formatter)
        self.loggerConsole.addHandler(fhConsole)

    def w(self, msg):
        self.loggerFile.warning(msg)
        self.loggerConsole.warning(msg)

    def e(self, msg):
        self.loggerFile.error(msg)
        self.loggerConsole.error(msg)

    def i(self, msg):
        self.loggerFile.info(msg)
        self.loggerConsole.info(msg)
