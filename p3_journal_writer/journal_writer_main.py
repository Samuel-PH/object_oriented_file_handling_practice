import sys
import os

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.join(current_dir, '..')))

from shared_functionalities_or_utilities import ProjectHelper
from journal_methods import InteractiveJournal

def main():
    ProjectHelper.print_header("Program 3: Journal Writer")
    
    journal_file = os.path.join(current_dir, "mylife.txt")
    
    writer = InteractiveJournal(journal_file)
    writer.write_entries()

if __name__ == "__main__":
    main()