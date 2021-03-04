import datetime

last_id = 0

class Note:
    def __init__(self,memo,tags = ''):
        self.memo = memo 
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id +=1
        self.id = last_id

    def match(self, key_word):
        isExisting = key_word in self.memo or key_word in self.tags
        return isExisting

# n1 = Note('hello first')
# n2 = Note('hello second')
# print(n2.id)
# print(n2.match("hell"), n2.match("lmao"), n2.match("hello"))



class Notebook:
    def __init__(self):
        self.notes = []
    
    def new_note(self, memo , tags=''):
        self.notes.append(Note(memo, tags))

    def __find__note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
            return None

    def modify_memo(self, note_id, memo):
        self.__find__note(note_id).memo = memo

    def modify_tags(self,note_id, tags):
        self.__find__note(note_id).tags = tags

    def search(self, key_word):
        return (note for note in self.notes if note.match(key_word))

    
# notebook = Notebook()
# notebook.new_note("fuck u", tags="qqq")
# print(notebook.notes)
# print(notebook.notes[0].id)
# print(notebook.search("fuck"))
# notebook.modify_memo(1, 'fdgf')
# print(notebook.notes[0].memo)