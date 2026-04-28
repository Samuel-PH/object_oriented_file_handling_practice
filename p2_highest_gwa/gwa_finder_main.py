import sys
import os

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.join(current_dir, '..')))

from shared_functionalities_or_utilities import ProjectHelper
from gwa_methods import GwaAnalyzer

def main():
    ProjectHelper.print_header("Program 2: Highest GWA Finder")
    
    students_file = os.path.join(current_dir, "students.txt")
    
    ProjectHelper.create_dummy_students(students_file)
    
    analyzer = GwaAnalyzer(students_file)
    analyzer.find_top_student()

if __name__ == "__main__":
    main()