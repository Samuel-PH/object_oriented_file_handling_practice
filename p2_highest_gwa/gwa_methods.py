from datetime import datetime

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

        report_file = self.input_file.replace(".txt", "_report.txt")
        
        with open(report_file, 'w') as out:
            out.write("+" + "-"*38 + "+\n")
            out.write("|       ACADEMIC EXCELLENCE REPORT     |\n")
            out.write("+" + "-"*38 + "+\n")
            
            # Get the current date and time
            current_time = datetime.now().strftime("%B %d, %Y at %I:%M %p")
            out.write(f"  Generated on: {current_time}\n\n")
            
            out.write(f"  Top Performing Student : {top_student}\n")
            out.write(f"  Grade Weighted Average : {highest_gwa}\n")
            out.write("+" + "-"*38 + "+\n")
            
        print(f"[+] Report generated beautifully at {report_file}")