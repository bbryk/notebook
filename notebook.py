import datetime

last_id = 0


class Note:
    """
    Note class. Contains __init__ and match methods
    """
    def __init__(self, memo, tags=''):
        """
        main method to create object. It is called when
        the new object is being created
        >>> note = Note('hello')
        >>> print(note.memo)
        hello
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, key_word):
        """
        method to check whether the keyword mathes the memo of note
        >>> note = Note('hello')
        >>> note.match('hell')
        True
        """
        isExisting = key_word in self.memo or key_word in self.tags
        return isExisting


class Notebook:
    """
    Notebook class. Contains __init__ , new_note , find__note, modify_memo, modify_tags, search methods
    """
    def __init__(self):
        """
        main method to create object. It is called when
        the new object is being created
        
        >>> notebook = Notebook()
        >>> print(notebook.notes)
        []
        """
        self.notes = []

    def new_note(self, memo, tags=''):
        """
        adds a new note

        >>> notebook = Notebook()
        >>> notebook.new_note('yes')
        >>> print(notebook.notes[0].memo)
        yes
        """

        self.notes.append(Note(memo, tags))

    def find__note(self, note_id):
        """
        finds the specific note

        >>> notebook = Notebook()
        >>> notebook.new_note('yes')
        >>> notebook.find__note(1)
        
        """
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        """
        modifies the memo of note

        >>> notebook = Notebook()
        >>> notebook.new_note('yes')
        >>> notebook.modify_memo(1,'qwerty')
        False
        """

        note = self.find__note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        """
        modifies the tags of specific note

        >>> notebook = Notebook()
        >>> notebook.new_note('yes')
        >>> notebook.modify_tags(1,'tag1')
        False
        """
        note = self.find__note(note_id)
        if note:
            note.tags = tags
            return True
        return False

    def search(self, key_word):
        """
        searches the note by keyword


        >>> notebook = Notebook()
        >>> notebook.new_note('yes')
        """
        return (note for note in self.notes if note.match(key_word))

import doctest
doctest.testmod()