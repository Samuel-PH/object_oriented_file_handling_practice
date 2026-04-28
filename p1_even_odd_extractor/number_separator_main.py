import sys
import os

current_dir = os.path.dirname(__file__)

sys.path.append(os.path.abspath(os.path.join(current_dir, '..')))
from shared_functionalities_or_utilities import ProjectHelper
from extractor_methods import NumberSeparator

def main():
    ProjectHelper.print_header("Program 1: Even and Odd Extractor")
    
    input_file = os.path.join(current_dir, "numbers.txt")
    even_file = os.path.join(current_dir, "even.txt")
    odd_file = os.path.join(current_dir, "odd.txt")
    
    ProjectHelper.create_dummy_numbers(input_file)
    
    extractor = NumberSeparator(input_file, even_file, odd_file)
    extractor.extract_numbers()
    print("[+] Numbers successfully extracted to even.txt and odd.txt")

if __name__ == "__main__":
    main()