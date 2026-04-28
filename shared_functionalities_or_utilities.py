import os
import random

# This file contains shared functionalities or utilities that can be used across multiple programs. Mainly creates dummy data and prints headers for the programs.
class ProjectHelper:
    @staticmethod
    def print_header(title):
        print(f"\n--- {title} ---")

    @staticmethod
    def create_dummy_numbers(filename):
        if not os.path.exists(filename):
            print(f"[*] Missing '{filename}'. Generating dummy data now...")
            with open(filename, 'w') as file:
                for _ in range(20):
                    file.write(f"{random.randint(1, 100)}\n")

    @staticmethod
    def create_dummy_students(filename):
        if not os.path.exists(filename):
            print(f"[*] Missing '{filename}'. Generating dummy students now...")
            with open(filename, 'w') as file:
                for i in range(1, 21):
                    file.write(f"Student_{i},{round(random.uniform(1.0, 3.0), 2)}\n")