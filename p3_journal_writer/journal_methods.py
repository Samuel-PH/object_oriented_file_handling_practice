class InteractiveJournal:
    def __init__(self, output_file):
        self.output_file = output_file

    def write_entries(self):
        with open(self.output_file, 'w') as file:
            while True:
                line = input("Enter line: ")
                file.write(line + "\n")
                
                more_lines = input("Are there more lines y/n? ").strip().lower()
                if more_lines != 'y':
                    break
                
        print(f"[+] Journal saved to {self.output_file}")
