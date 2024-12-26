def merge(first_file, second_file, third_file, output_file):
    file1 = list(map(lambda x: x.rstrip(), open(first_file, 'r')))
    file2 = list(map(lambda x: x.rstrip(), open(second_file, 'r')))
    file3 = list(map(lambda x: x.rstrip(), open(third_file, 'r')))
    result = open(output_file, 'a+')

    merge_set = set(file1 + file2 + file3)
    merge_list = list(merge_set)
    result.write("\n".join(merge_list))
    result.close()
