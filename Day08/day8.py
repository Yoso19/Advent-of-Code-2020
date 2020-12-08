def handheld_halting():
    with open('day8.txt') as code_file:
        boot_code = [line.strip() for line in code_file]
    accumulator = 0
    program_counter = 0
    executed_instructions = set()

    while True:
        if program_counter in executed_instructions:
            result = accumulator
            break
        else:
            executed_instructions.add(program_counter)
            instruction = boot_code[program_counter]
            operation, argument = instruction.split()
            if operation == 'acc':
                accumulator += int(argument)
                program_counter += 1
            elif operation == 'jmp':
                program_counter += int(argument)
            else:
                program_counter += 1
            
    print('PART 1: Value in the accumulator is:', accumulator)

    accumulator = 0
    program_counter = 0
    executed_instructions = set()
    break_point = len(boot_code)
    result = None
    change = False
    changed = set()
    while True:
        if program_counter >= break_point:
            result = accumulator
            break
        if program_counter in executed_instructions:
            program_counter = 0
            accumulator = 0
            executed_instructions = set()
            change = False
        else:
            executed_instructions.add(program_counter)
            instruction = boot_code[program_counter]
            operation, argument = instruction.split()
            if operation == 'acc':
                accumulator += int(argument)
                program_counter += 1
            elif operation == 'jmp':
                if not change and program_counter not in changed:
                    change = True
                    changed.add(program_counter)
                    program_counter += 1
                else:
                    program_counter += int(argument)
            else:
                if not change and program_counter not in changed:
                    change = True
                    changed.add(program_counter)
                    program_counter += int(argument)
                else:
                    program_counter += 1
            
    print('PART 2: Value in the accumulator is:', accumulator)
    

if __name__ == '__main__':
    handheld_halting()