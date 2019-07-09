import genanki
import datetime

from vulcan.data.jp_word import Word


CSS = '''
div.front, div.back {
    text-align:center;
    font-family: Courier;
    font-size: 30px;
}

span.small {font-size: 15px;}
span.normal {font-size: 30px;}
span.large {font-size: 60px;}
span.italic {font-style:italic;}
'''


def gen_id() -> int:
    return int(datetime.datetime.now().timestamp())


class Vulcan:

    def __init__(self, name: str):
        self.name = name
        self.model = genanki.Model(gen_id(),
                                   '新编日语（上海外语教育出版社）',
                                   fields=[
                                       {'name': 'Question'},
                                       {'name': 'Answer1'},
                                       {'name': 'Answer2'},
                                       {'name': 'Tone'},
                                       {'name': 'Attr'},
                                       {'name': 'Lesson'},
                                   ],
                                   templates=[
                                       {
                                           'name': 'new_japanese',
                                           'qfmt': '''
                                           <div class="front">
                                                <span class="large japanese">{{Question}}</span>
                                                <br/
                                            </div>
                                            ''',
                                           'afmt': '''
                                            <div class="back">
                                                 <span class="large">{{Answer1}}</span>
                                                 <span class="large">{{Answer2}}</span>
                                                 <hr/>
                                                 {{Tone}},{{Attr}},{{Lesson}}
                                                 <br/>
                                                 </span>
                                            </div>
                                            ''',
                                       },
                                   ],
                                   css=CSS)
        self.deck = genanki.Deck(gen_id(),
                                 name='新编日语')

    def add(self, word: Word):
        node1 = genanki.Note(model=self.model,
                            fields=[
                                word.word, word.chinese, word.gana,
                                word.tone, word.attr, word.lesson,
                            ])
        self.deck.add_note(node1)
        node2 = genanki.Note(model=self.model,
                            fields=[
                                word.chinese, word.gana, word.word,
                                word.tone, word.attr, word.lesson
                            ])
        self.deck.add_note(node2)
        node3 = genanki.Note(model=self.model,
                            fields=[
                                word.gana, word.word, word.chinese,
                                word.tone, word.attr, word.lesson,
                            ])
        self.deck.add_note(node3)

    def save(self):
        genanki.Package(self.deck).write_to_file(self.name + '.apkg')
