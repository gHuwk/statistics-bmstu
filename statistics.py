def get_filename():
    filename = input("Input filename: ")
    return filename

def print_file(data):
    path = './result.txt'
    counter = 1
    with open(path, 'w') as file:
        for ceil in data:
            string = str(counter) + ' ' + str(ceil[0]) + '\t\t' + str(ceil[1][0]) + '\t' + str(ceil[1][1]) + '\n'
            file.write(string)
            counter += 1
    
def read(path):
    with open(path, 'r') as file:
        data = [line.strip() for line in file]
        for i in range(len(data)):
            data[i] = data[i].replace('\t', '')
        count = 0
        for i in range(len(data)):
            if data[i] == '':
                count += 1
        for i in range(count):
            data.remove('')
                
        return data

def create_first_dict(data):
    dict_st = {}
    for i in range(0, len(data), 3):
        marks = data[i+2].split()
        dict_st[data[i]] = [data[i+1], marks[-1]]
    return dict_st

def sort_dict(dict_st):
    list_d = list(dict_st.items())
    list_d.sort(key=lambda i: int(i[1][1]))
    list_d.reverse()
    return list_d

def main():
    input_file = get_filename()
    dict_s = create_first_dict(read(input_file))
    print_file(sort_dict(dict_s))

if __name__ == '__main__':
    main()
