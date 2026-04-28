import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shared_functionalities_or_utilities import ProjectHelper
from extractor_methods import NumberSeparator

def main():
    ProjectHelper.print_header("Program 1: Even and Odd Extractor")
    
    ProjectHelper.create_dummy_numbers("numbers.txt")
    
    extractor = NumberSeparator("numbers.txt", "even.txt", "odd.txt")
    extractor.extract_numbers()
    print("[+] Numbers successfully extracted to even.txt and odd.txt")

if __name__ == "__main__":
    main()