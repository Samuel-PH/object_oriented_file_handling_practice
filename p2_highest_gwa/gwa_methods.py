class GwaAnalyzer:
    def __init__(self, input_file):
        self.input_file = input_file

    def find_top_student(self):
        highest_gwa = -1.0
        top_student = ""

        with open(self.input_file, 'r') as file:
            for line in file:
                name, gwa_str = line.strip().split(',')
                gwa = float(gwa_str)
                
                if gwa > highest_gwa:
                    highest_gwa = gwa
                    top_student = name

        print(f"[+] Top Student found: {top_student} with a GWA of {highest_gwa}")