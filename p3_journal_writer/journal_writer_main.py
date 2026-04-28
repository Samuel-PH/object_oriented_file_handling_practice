import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shared_functionalities_or_utilities import ProjectHelper
from journal_methods import InteractiveJournal

def main():
    ProjectHelper.print_header("Program 3: Journal Writer")
    
    writer = InteractiveJournal("mylife.txt")
    writer.write_entries()

if __name__ == "__main__":
    main()