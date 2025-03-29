def run_code(program, input_data=""):
    cells = [0 for i in range(256)]
    element = 0
    output = "" 
    program=program.replace('\n',' ').split()
    for i in range (0,len(program)-1,2):
        command=program[i]+' '+program[i+1]
        if command == 'Ook. Ook.':
            cells[element] = (cells[element] + 1) % 256
        elif command == 'Ook! Ook!':
            cells[element] = (cells[element] - 1) % 256
        elif command == 'Ook. Ook.':
            cells[element] = (cells[element] + 1) % 256
        elif command == 'Ook! Ook.':
            output += chr(cells[element])
        elif command == 'Ook? Ook.':
            element = (element - 1) % 256
        elif command == 'Ook. Ook?':
            element = (element + 1) % 256
        elif command == 'Ook. Ook!':
            cells[element] = ord(input_data[0])
            input_data = input_data[1:]
    return output
    # for command in program:
    #     if command == "+":
    #         x += 1
    #     elif command == '.':
    #         return chr(x)
    #return chr((0 + (program.count("+") - program.count("-"))) % 256)
