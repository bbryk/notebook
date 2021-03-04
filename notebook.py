import datetime

last_id = 0


class Note:
    def __init__(self, memo, tags=''):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, key_word):
        isExisting = key_word in self.memo or key_word in self.tags
        return isExisting


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo, tags))

    def __find__note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):

        note = self.__find__note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        note = self.__find__note(note_id)
        if note:
            note.tags = tags
            return True
        return False

    def search(self, key_word):
        return (note for note in self.notes if note.match(key_word))
