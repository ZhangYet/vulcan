from vulcan.data.jp_word import load_from_file
from vulcan.anki import Vulcan

if __name__ == '__main__':
    word_list = load_from_file('vulcan/data/clean_jp.csv')
    v = Vulcan('新编日语(上海教育出版社)')
    for word in word_list:
        v.add(word)
    v.save()
