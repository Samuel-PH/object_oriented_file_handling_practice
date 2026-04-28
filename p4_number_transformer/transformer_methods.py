import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from p1_even_odd_extractor.extractor_methods import NumberSeparator

class MathTransformer(NumberSeparator):
    def __init__(self, input_file, double_file, triple_file):
        super().__init__(input_file, double_file, triple_file)

    def _write_to_files(self, number, out_one, out_two):

        if number % 2 == 0:
            out_one.write(f"{number ** 2}\n")
        else:
            out_two.write(f"{number ** 3}\n")