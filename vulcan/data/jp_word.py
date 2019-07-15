STAR = '☆'


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

    def to_chinese(self):
        return '汉语: {}'.format(self.chinese)

    def to_word(self):
        return '日文: {}'.format(self.word)

    def to_gana(self):
        return '假名: {}'.format(self.gana)

    def clean_lesson(self) -> str:
        lesson_num = self.lesson.strip().replace(STAR, '')
        try:
            if int(lesson_num) < 10:
                return '0' + self.lesson
            return self.lesson
        except:
            print(self.lesson)


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

