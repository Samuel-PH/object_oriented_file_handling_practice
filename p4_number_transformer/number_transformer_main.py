import sys
import os

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.join(current_dir, '..')))

from shared_functionalities_or_utilities import ProjectHelper
from transformer_methods import MathTransformer

def main():
    ProjectHelper.print_header("Program 4: Math Transformer")
    
    input_file = os.path.join(current_dir, "integers.txt")
    double_file = os.path.join(current_dir, "double.txt")
    triple_file = os.path.join(current_dir, "triple.txt")
    
    ProjectHelper.create_dummy_numbers(input_file)
    
    transformer = MathTransformer(input_file, double_file, triple_file)
    transformer.extract_numbers()
    print("[+] Files transformed successfully into double.txt and triple.txt")

if __name__ == "__main__":
    main()
    