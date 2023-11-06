import os
import unittest
from file_concatenator import FileConcatenator
from utilities import uniform_file_types
from tests.csv_gen import gen_tests_csv
from tests.text_gen import gen_tests_text

class TestFileConcatenator(unittest.TestCase):
    def setUp(self):
        self.text_concatenator = FileConcatenator("text")
        self.csv_concatenator = FileConcatenator("csv")

        # Create test files
        self.csv_files = gen_tests_csv()
        self.text_files = gen_tests_text()

    def test_uniform_file_types(self):
        self.assertEqual(uniform_file_types(self.csv_files), "csv")
        self.assertEqual(uniform_file_types([self.text_files[0], self.csv_files[0]]), None)

    def test_concatenate_files(self):
        self.text_concatenator.concatenate_files(self.text_files, "tests/test_files/text/output_default.txt")
        self.csv_concatenator.concatenate_files(self.csv_files, "tests/test_files/csv/output_default.csv")

        # Check the output file
        with open("tests/test_files/text/output_default.txt", 'r') as f:
            with open("tests/test_files/text/expected_default.txt", 'r') as expected:
                self.assertEqual(f.read(), expected.read())

        with open("tests/test_files/csv/output_default.csv", 'r') as f:
            with open("tests/test_files/csv/expected_default.csv", 'r') as expected:
                self.assertEqual(f.read(), expected.read())

    def tearDown(self):
        # Remove test files
        all_files = self.csv_files + self.text_files + ["tests/test_files/text/output_default.txt", "tests/test_files/csv/output_default.csv"]
        print(all_files)
        for file_name in all_files:
            os.remove(file_name)

if __name__ == "__main__":
    unittest.main()