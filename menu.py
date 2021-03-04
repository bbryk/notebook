import doctest
import sys
from notebook import Notebook, Note


class Menu:
    """
    Menu class. Contains __init__ , display_menu, run, show_notes,
    search_notes, add_note, modify_note, quit methods
    """

    def __init__(self):
        """

        main method to create object. It is called when
        the new object is being created

        >>> menu = Menu()

        """
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit

        }

    def display_menu(self):
        """
        dispays the menu

        >>> menu = Menu()
        >>> menu.display_menu()
        <BLANKLINE>
        <BLANKLINE>
                Notebook Menu
        <BLANKLINE>
                1. Show all Notes
                2. Search Notes
                3. Add Note
                4. Modify Note
                5. Quit
        """
        print("""
        
        Notebook Menu

        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit""")

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        """
        displays the notes
        """
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f"{note.id}: {note.tags},\n{note.memo}")

    def search_notes(self):
        """
        searches fot the notes using the keyword

        """
        key_word = input("Search for:")
        notes = self.notebook.search(key_word)
        self.show_notes(notes)

    def add_note(self):
        """
        adds a note
        """
        memo = input("Enter a memo:")
        self.notebook.new_note(memo)
        print("Your note has been added")

    def modify_note(self):
        """
        modifies the note
        """
        id = input("enter a note id:")
        memo = input("Enter a memo:")
        tags = input("Enter tags:")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        """
        ends the program
        """
        print("Thank you")
        sys.exit(0)


# if __name__=="__main__":
#     Menu().run()
doctest.testmod()
