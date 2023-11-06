import csv


def gen_tests_csv():
    file_names = ["tests/test_files/csv/file1.csv", "tests/test_files/csv/file2.csv", "tests/test_files/csv/file3.csv"]

    i = 0
    for file_name in file_names:
        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Age"])
            writer.writerow(["Alice", str(20 + i)])
            writer.writerow(["Bob", str(25 + i)])
        i += 1

    return file_names

