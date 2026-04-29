from datetime import datetime

class InteractiveJournal:
    def __init__(self, output_file):
        self.output_file = output_file

    def write_entries(self):
        with open(self.output_file, 'a') as file:
            
            current_date = datetime.now().strftime("%A, %B %d, %Y")
            file.write("\n" + "="*40 + "\n")
            file.write(f" ENTRY DATE: {current_date}\n")
            file.write("="*40 + "\n")
            
            while True:
                line = input("Enter line: ")
                file.write(f" • {line}\n")
                
                more_lines = input("Are there more lines y/n? ").strip().lower()
                if more_lines != 'y':
                    break
                    
        print(f"[+] Journal updated securely at {self.output_file}")