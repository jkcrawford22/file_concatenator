def gen_tests_text():
    file_names = ["tests/test_files/text/file1.txt", "tests/test_files/text/file2.txt", "tests/test_files/text/file3.txt"]

    for file_name in file_names:
        with open(file_name, 'w') as f:
            f.write(str("This is the content of " + file_name))
    
    return file_names
