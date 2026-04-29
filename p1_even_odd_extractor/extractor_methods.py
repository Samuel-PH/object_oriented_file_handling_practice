class NumberSeparator:
    def __init__(self, input_file, file_one, file_two):
        self.input_file = input_file
        self.file_one = file_one
        self.file_two = file_two

    def extract_numbers(self):
        with open(self.input_file, 'r') as infile, \
             open(self.file_one, 'w') as out_one, \
             open(self.file_two, 'w') as out_two:
            
            self._write_headers(out_one, out_two)
            
            for line in infile:
                number = int(line.strip())
                self._write_line(number, out_one, out_two)

    def _write_headers(self, out_one, out_two):
        out_one.write("=========================\n")
        out_one.write("  EXTRACTED EVEN NUMBERS \n")
        out_one.write("=========================\n\n")
        
        out_two.write("=========================\n")
        out_two.write("  EXTRACTED ODD NUMBERS  \n")
        out_two.write("=========================\n\n")

    def _write_line(self, number, out_one, out_two):
        if number % 2 == 0:
            out_one.write(f" -> {number}\n")
        else:
            out_two.write(f" -> {number}\n")