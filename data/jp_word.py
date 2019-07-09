class Word:

    def __str__(self):
        return '{0.lesson}, {0.word}, {0.gana}, {0.tone}, {0.attr}, {0.chinese}'.format(self)

    def __init__(self, lesson: str, word: str, gana: str, tone: str, attr: str, chinese):
        self.lesson = lesson
        self.word = word
        self.gana = gana
        self.tone = tone
        self.attr = attr
        self.chinese = chinese


def load_from_file(file_path: str) -> [Word]:
    ret = []
    with open(file_path) as data:
        for line in data:
            sline = line.split('\t')
            if len(sline) < 6:
                continue

            word = Word(sline[0].strip(),
                        sline[1].strip(),
                        sline[2].strip(),
                        sline[3].strip(),
                        sline[4].strip(),
                        sline[5].strip())

            if __name__ == '__main__':
                print(word)

            ret.append(word)

    return ret


if __name__ == '__main__':
    load_from_file('./clean_jp.csv')

