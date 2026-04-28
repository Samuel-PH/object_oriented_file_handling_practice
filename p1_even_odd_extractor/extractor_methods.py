class NumberSeparator:
    def __init__(self, input_file, file_one, file_two):
        self.input_file = input_file
        self.file_one = file_one
        self.file_two = file_two

    def extract_numbers(self):
        with open(self.input_file, 'r') as infile, \
             open(self.file_one, 'w') as out_one, \
             open(self.file_two, 'w') as out_two:
            
            for line in infile:
                number = int(line.strip())
                self._write_to_files(number, out_one, out_two)

    def _write_to_files(self, number, out_one, out_two):
        if number % 2 == 0:
            out_one.write(f"{number}\n")
        else:
            out_two.write(f"{number}\n")