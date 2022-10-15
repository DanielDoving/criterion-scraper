from Config import Config


class FileWriter:
    @staticmethod
    def write(content: str):
        out = open(Config.OUTPUT_FILE, 'w', encoding="utf-8")
        out.write(content)
