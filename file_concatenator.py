import csv

class FileConcatenator:
    def __init__(self, file_type):
        self.file_type = file_type.lower()
    
    def concatenate_files(self, file_paths, output_path):
        if self.file_type == "text":
            self.concatenate_text_files(file_paths, output_path)
        elif self.file_type == "csv":
            self.concatenate_csv_files(file_paths, output_path)
        else:
            print("Unknown file type")

    def concatenate_text_files(self, file_paths, output_path):
        with open(output_path, "w") as outfile:
            for file_path in file_paths:
                with open(file_path, "r") as infile:
                    outfile.write(infile.read())

    def concatenate_csv_files(self, file_paths, output_path):
        with open(output_path, "w", newline='') as outfile:
            writer = csv.writer(outfile)
            headers_written = False
            for file_path in file_paths:
                with open(file_path, "r", newline='') as infile:
                    reader = csv.reader(infile)
                    headers = next(reader)
                    if not headers_written:
                        writer.writerow(headers)
                        headers_written = True
                    if headers != next(csv.reader([','.join(headers)])):
                        print(f"Skipping file {file_path} because headers do not match")
                        continue
                    for row in reader:
                        writer.writerow(row)