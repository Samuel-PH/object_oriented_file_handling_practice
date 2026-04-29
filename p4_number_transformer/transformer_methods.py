import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from p1_even_odd_extractor.extractor_methods import NumberSeparator

class MathTransformer(NumberSeparator):
    def __init__(self, input_file, double_file, triple_file):
        super().__init__(input_file, double_file, triple_file)

    def _write_headers(self, out_one, out_two):
        out_one.write("==================================\n")
        out_one.write("  EVEN NUMBERS (SQUARED RESULTS)  \n")
        out_one.write("==================================\n\n")
        
        out_two.write("==================================\n")
        out_two.write("   ODD NUMBERS (CUBED RESULTS)    \n")
        out_two.write("==================================\n\n")

    def _write_line(self, number, out_one, out_two):
        if number % 2 == 0:
            out_one.write(f" Original: {number:<5} | Squared: {number ** 2}\n")
        else:
            out_two.write(f" Original: {number:<5} | Cubed:   {number ** 3}\n")

