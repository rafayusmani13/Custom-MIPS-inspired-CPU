######################################
## ECE 366 Fall 2020 - Project 3    ##
##                                  ##
## Created by Group 8               ##
######################################


def bin_to_dec(b):
    """
    converts b, a positive binary integer or two's compliment negative integer, to its decimal equivilant
    
    returns a decimal integer
    """
    if (b[0] == "0"):
        return int(b, base=2)
    else:

        c = b[1:]
        c_flip = ""
        for bit in c:
            if (bit == '0'):
                c_flip = c_flip + '1'
            else:
                c_flip = c_flip + '0'

        c_int = int(c_flip, base=2)
        c_int = -1 * (c_int + 1)
        return c_int


def dec_to_bin(val, b):
    """
    converts val, a decimal integer, to its binary equivilant
    
    returns a positive binary integer or two's compliment negative integer of length b bits
    """
    val_bin = ""
    if (val >= 0):
        val_bin = str(bin(val))
        val_bin = val_bin[2:].zfill(b)
    else:
        c_int = val * -1
        c_flip = dec_to_bin(c_int, b)

        index = (b - 1)
        while index >= 0:
            if c_flip[index] == '1':
                break
            else:
                index -= 1
        c_end = c_flip[index:]
        flip_index = 0

        while flip_index < index:
            if (c_flip[flip_index] == '0'):
                val_bin = val_bin + '1'
            else:
                val_bin = val_bin + '0'

            flip_index += 1

        val_bin = val_bin + c_end

    return val_bin


def hex_to_bin(hex):
    """
    converts hex, a positive hexidecimal integer, to its binary equivilant
    
    returns a 8 bit positive binary integer
    """
    h = hex.replace("\n", "")
    i = int(h, base=16)
    b = dec_to_bin(i, 8)
    print(f'Instruction {h} in binary is {b}')
    return (b)


def dec_to_hex(dec, b):
    """
    converts dec, a positive decimal integer, to its hexidecimal equivilant
    
    returns a positive hexidecimal integer of length b bits 
    """
    h = str(hex(dec))
    h = h[2:]

    if (len(h) < b):
        z = b - len(h)
        while z > 0:
            h = '0' + h
            z = z - 1

    h = '0x' + h
    return (h)


def process(b, IM):
    """
    converts b, the binary form of a line of mips assembly code, to its mips instruction equivilant
    as the line is processed its contents are appeneded to PC, the instruction memory
    
    returns a string of the line of mips assembly code
    """
    b_func = b[0:4]
    b_init = b[0:2]
    b_irx  = b[2:4]
    b_rx   = b[4:6]
    b_ry   = b[6:8]
    b_ii   = b[6:8]
    b_iiii = b[4:8]


    if (b_init == '00'):  # N-Type
        print(f'-> {b_init} | {b_irx} | {b_iiii} ')

    elif((b_func == '0100') | (b_func == '0101') | (b_func == '1000') | (b_func == '1001') | (b_func == '1010') | (b_func == '1011')):  # Display R-Type
        print(f'-> {b_func} | {b_rx}  | {b_ry}')

    elif((b_func == '0110') ):  # Display I-Type
        print(f'-> {b_func} | {b_rx}  | {b_ry}')

    elif((b_func == '1101') | (b_func == '1110')):  # Display B-Type
        print(f'-> {b_func} | {b_iiii}')

    else: #(b_func == '1111'):  # F-Type
        print(f'-> 11111111')

    asm = ""

    instr = []
    instr.append(int(b,      base=2))
    instr.append(int(b_func, base=2))
    instr.append(int(b_init, base=2))
    instr.append(int(b_irx,  base=2))
    instr.append(int(b_rx,  base=2))
    instr.append(int(b_ry,  base=2))
    instr.append(bin_to_dec(b_ii))
    instr.append(bin_to_dec(b_iiii))

    IM.append(instr)

    if (b_init == '00'):  # INIT
        xx   = int(b_irx,  base=2)
        iiii = bin_to_dec(b_iiii)

        xx   = "R" + str(xx)
        iiii =  str(iiii)

        asm = "init " + xx + ",  " + iiii
        print(f'in asm: {asm}')

    elif (b_func == '0100'):  # LDUP
        xx = int(b_rx, base=2)
        yy = int(b_ry, base=2)

        xx = "R" + str(xx)
        yy = "R" + str(yy)

        asm = "ldup " + xx + ",  " + yy
        print(f'in asm: {asm}')

    elif (b_func == '0101'):  # ADD
        xx = int(b_rx, base=2)
        yy = int(b_ry, base=2)

        xx = "R" + str(xx)
        yy = "R" + str(yy)

        asm = "add  " + xx + ",  " + yy
        print(f'in asm: {asm}')

    elif (b_func == '0110'):  # ADDI
        xx = int(b_rx, base=2)
        ii = bin_to_dec(b_ii)

        xx = "R" + str(xx)
        ii =  str(ii)

        asm = "addi " + xx + ",  " + ii
        print(f'in asm: {asm}')

    elif (b_func == '1000'):  # XOR
        xx = int(b_rx, base=2)
        yy = int(b_ry, base=2)

        xx = "R" + str(xx)
        yy = "R" + str(yy)

        asm = "xor  " + xx + ",  " + yy
        print(f'in asm: {asm}')

    elif (b_func == '1001'):  # WDTH
        xx = int(b_rx, base=2)
        yy = int(b_ry, base=2)

        xx = "R" + str(xx)
        yy =  str(yy)

        asm = "wdth " + xx + ",  " + yy
        print(f'in asm: {asm}')

    elif (b_func == '1010'):  # LB
        xx = int(b_rx, base=2)
        yy = int(b_ry, base=2)

        xx = "R" + str(xx)
        yy = "R" + str(yy)

        asm = "lb   " + xx + ", (" + yy + ")"
        print(f'in asm: {asm}')

    elif (b_func == '1011'):  # SB
        xx = int(b_rx, base=2)
        yy = int(b_ry, base=2)

        xx = "R" + str(xx)
        yy = "R" + str(yy)

        asm = "sb   " + xx + ", (" + yy + ")"
        print(f'in asm: {asm}')

    elif (b_func == '1101'):  # BNZ
        iiii = bin_to_dec(b_iiii)

        iiii = str(iiii)

        asm = "bnz  " + iiii
        print(f'in asm: {asm}')

    elif (b_func == '1110'):  #JMP
        iiii = bin_to_dec(b_iiii)

        iiii = str(iiii)

        asm = "jmp  " + iiii
        print(f'in asm: {asm}')

    elif (b_func == '1111'):  #HALT

        asm = "halt"
        print(f'in asm: {asm}')

    else:
        print(f'NO idea about instruction = {b}')

    IM[-1][0] = asm  #replaces the binary machine code value with its assembly equivilent
    return (asm)


def print_(str):
    """
    writes str, a string, to the console and to the output file
    """
    output_line = str
    print(output_line)
    output_file.write(output_line + '\n')


def print_stat(stat_name, stat_value, percent_value):
    """
    adds the values of stat_name, stat_value, and percent_value;a string, and two decimal integers respectfully; to output_line, a string, to the console and to the output file
    """
    output_line = '{stat_name:>8}: {stat_value:>7} {percent_value:.0f}% '
    print(
        output_line.format(
            stat_name=stat_name,
            stat_value=stat_value,
            percent_value=percent_value))
    output_file.write(
        output_line.format(
            stat_name=stat_name,
            stat_value=stat_value,
            percent_value=percent_value) + '\n')


def add_(rx, ry):
    """
    adds rx, a decimal integer, to ry, a decimal integer

    returns the decimal integer sum,
    if the sum is greater than 8 bits, the value of the least significant 8 bits is returned
    """
    sum_dec= rx + ry

    if ((sum_dec < -128) | (sum_dec > 127)):
        sum_bin = dec_to_bin(sum_dec,8)
        sum_bin = sum_bin[-8:]
        sum_dec = bin_to_dec(sum_bin)

    return sum_dec


def xor_(rx, ry):
    """
    performs the bitwise XOR operation on rx, a decimal integer, and ry, a decimal integer
    
    returns the decimal integer value 
    """
    rx_bin = dec_to_bin(rx, 8)
    ry_bin = dec_to_bin(ry, 8)

    rd_bin = ""
    index = 0

    while index < 8:
        if ((rx_bin[index] != ry_bin[index])):
            rd_bin = rd_bin + '1'
        else:
            rd_bin = rd_bin + '0'
        index += 1

    rd_dec = bin_to_dec(rd_bin)
    return rd_dec

def ldup_(rx, ry):
    """
    takes the 4 least significant bits of rx and ry
    
    returns the decimal integer value
    """
    rx_bin  = dec_to_bin(rx, 8)
    ry_bin  = dec_to_bin(ry, 8)
    rx_LSB4 = rx_bin[4:]
    ry_LSB4 = ry_bin[4:]
    val_bin = ry_LSB4 + rx_LSB4
    val = int(val_bin, base=2)
    return val

#SPECIAL INSTRUCTION
def wdth_(ry,b):
    """
    finds the width of rs, a decimal integer, with a binary length of b bits
    
    where the width is defined as the number of bits between the most significant 1 and the least significant 1 (including both 1’s)
    
    returns the deciaml integer value of the width
    """
    if (ry == 0):
        width = 0
    else:
        rs_bin = dec_to_bin(ry, b)
        width = 1
        msb = 0
        lsb = 0

        index = 0
        while (index < b):
            if (rs_bin[index] == '1'):
                msb = index
                break
            else:
                index += 1

        index = (b - 1)
        while (index >= 0):
            if (rs_bin[index] == '1'):
                lsb = index
                break
            else:
                index -= 1

        if (width != 0):
            width = width + (lsb - msb)

    return width


def data_mem_address(address):
    address = dec_to_bin(address, 8)
    address = int(address, base=2)
    hex_address = dec_to_hex(address, 2)
    return hex_address


def execute(IM, reg, stats, DM):
    instr_count = 0
    alu_count = 0
    jump_count = 0
    branch_count = 0
    memory_count = 0
    other_count = 0
    special_count = 0
    pc_cur = 0

    print_('')
    print_('##############################')
    print_('# Step by Step Instructions  #')
    print_('##############################\n')

    while pc_cur < len(IM):
        instr_count += 1
        instr = IM[pc_cur]
        instr_func = dec_to_bin(instr[1], 4)

        if (instr[2] == 0):
            instr_func = '00'

        output_line = '\n' + 'Instruction: {instr_count:>6}  PC: {pc_cur:>4}'
        formatted_line = output_line.format(
            instr_count=instr_count, pc_cur=(pc_cur))
        print_(formatted_line)


        if (instr_func == '00'):  # INIT
            xx   = instr[3]
            iiii = instr[7]

            print_(f'    init R{xx}, {iiii}')
            print_(f'    previous values: R{xx}: {reg[xx]}')
            reg[xx] = iiii
            print_(f'     current values: R{xx}: {reg[xx]}')
            other_count += 1

        elif (instr_func == '0100'):  # LDUP
            xx  = instr[4]
            yy  = instr[5]

            print_(f'    ldup R{xx}, R{yy}')
            print_(f'    previous values: R{xx}: {reg[xx]}, R{yy}: {reg[yy]}')

            rx_bin  = dec_to_bin(reg[xx], 8)
            ry_bin  = dec_to_bin(reg[yy], 8)
            rx_LSB4 = rx_bin[4:]
            ry_LSB4 = ry_bin[4:]

            print_(f'         LSB values: R{xx}: {rx_LSB4}, R{yy}: {ry_LSB4}')
            reg[xx] = ldup_(reg[xx], reg[yy])
            print_(f'     current values: R{xx}: {reg[xx]}, R{yy}: {reg[yy]}')
            other_count += 1

        elif (instr_func == '0101'):  # ADD
            xx  = instr[4]
            yy  = instr[5]

            print_(f'    add  R{xx}, R{yy}')
            print_(f'    previous values: R{xx}: {reg[xx]}, R{yy}: {reg[yy]}')
            reg[xx] = add_(reg[xx], reg[yy])
            print_(f'     current values: R{xx}: {reg[xx]}, R{yy}: {reg[yy]}')
            alu_count += 1

        elif (instr_func == '0110'):  # ADDI
            xx  = instr[4]
            ii  = instr[6]

            print_(f'    addi R{xx}, {ii}')
            print_(f'    previous values: R{xx}: {reg[xx]}')
            reg[xx] = add_(reg[xx], ii)
            print_(f'     current values: R{xx}: {reg[xx]}')
            alu_count += 1

        elif (instr_func == '1000'):  # XOR
            xx  = instr[4]
            yy  = instr[5]

            print_(f'    xor  R{xx}, R{yy}')
            print_(f'    previous values: R{xx}: {reg[xx]}, R{yy}: {reg[yy]}')
            reg[xx] = xor_(reg[xx], reg[yy])
            print_(f'     current values: R{xx}: {reg[xx]}, R{yy}: {reg[yy]}')
            alu_count += 1

        elif (instr_func == '1001'):  # WDTH
            xx  = instr[4]
            yy  = instr[5]

            print_(f'    wdth R{xx}, R{yy}')
            print_(f'    previous values: R{xx}: {reg[xx]}, R{yy}: {reg[yy]}')
            reg[xx] = wdth_(reg[yy], 8)
            print_(f'     current values: R{xx}: {reg[xx]}, R{yy}: {reg[yy]}')
            special_count += 1

        elif (instr_func == '1010'):  # LB
            xx  = instr[4]
            yy  = instr[5]

            address = reg[yy]
            address = dec_to_bin(address, 8)
            address = int(address, base=2)

            print_(f'    lb   R{xx}, (R{yy})')
            print_(f'    R{yy}   value: {reg[yy]}')
            print_(f'    R{yy} address: {address}')
            print_(f'    previous values: R{xx}: {reg[xx]}, R{yy}: {reg[yy]}, DM [{data_mem_address(reg[yy])}]: {DM[address]}')
            reg[xx] = DM[address]
            print_(f'     current values: R{xx}: {reg[xx]}, R{yy}: {reg[yy]}, DM [{data_mem_address(reg[yy])}]: {DM[address]}')
            memory_count += 1

        elif (instr_func == '1011'):  # SB
            xx  = instr[4]
            yy  = instr[5]

            address = reg[yy]
            address = dec_to_bin(address, 8)
            address = int(address, base=2)

            print_(f'    sb   R{xx}, (R{yy})')
            print_(f'    R{yy}   value: {reg[yy]}')
            print_(f'    R{yy} address: {address}')
            print_(f'    previous values: R{xx}: {reg[xx]}, R{yy}: {reg[yy]}, DM [{data_mem_address(reg[yy])}]: {DM[address]}')
            DM[address] = reg[xx]
            print_(f'     current values: R{xx}: {reg[xx]}, R{yy}: {reg[yy]}, DM [{data_mem_address(reg[yy])}]: {DM[address]}')
            memory_count += 1

        elif (instr_func == '1101'):  # BNZ
            iiii = instr[7]

            print_(f'    bnz {iiii}')

            print_(f'    previous values:  PC {pc_cur}, R3: {reg[3]}')
            if (reg[3] != 0):
                pc_cur = pc_cur + iiii
                print_(f'     current values:  PC {(pc_cur)}, R3: {reg[3]}')
            else:
                print_(f'     current values:  PC {(pc_cur + 1 )}, R3: {reg[3]}')
            branch_count += 1

        elif (instr_func == '1110'):  #JMP
            iiii = instr[7]

            print_(f'    j {iiii}')
            pc_cur = pc_cur +  iiii
            print_(f'    jump to pc: {pc_cur}')
            jump_count += 1

        elif (instr_func == '1111'):  #HALT

            print_(f'    halt')
            other_count += 1
            break

        else:
            print_(f'    NO idea about func = {instr_func}')
            break

        pc_cur += 1

        reg[4] = pc_cur

    stats.append(instr_count)
    stats.append(alu_count)
    stats.append(jump_count)
    stats.append(branch_count)
    stats.append(memory_count)
    stats.append(other_count)
    stats.append(special_count)


def print_instr_mem(instr_mem):
    """
    writes instr_mem, a list of strings, to the console and to the output file
    """

    print_('')
    print_('######################')
    print_('# Instruction Memory #')
    print_('######################\n')

    line_count = 0
    outputline = '{line_count:>3}: {instr}'

    for line in instr_mem:
        instr = line[0]
        formatted_line = outputline.format(line_count=line_count, instr=instr)
        print_(formatted_line)
        line_count += 1


def print_reg(reg):
    """
    writes reg, a list of decimal integers, to the console and to the output file
    """
    print_('')
    print_('#################')
    print_('# Register File #')
    print_('#################\n')

    outputline = '{reg_num:>3}: {line:>5}'

    reg_count = 0
    for line in reg:

        if (reg_count == 4):
            formatted_line = outputline.format(reg_num='PC', line=(line))
            print_(formatted_line)

        else:
            formatted_line = outputline.format(
                reg_num=('R' + str(reg_count)), line=line)
            print_(formatted_line)

        reg_count += 1


def print_data_mem(data_mem):
    """
    writes data_mem, a list of decimal integers, to the console and to the output file
    """
    print_('')
    print_('###############')
    print_('# Data Memory #')
    print_('###############\n')

    outputline = '{line}| {address:>5}: {value_str:>5} '
    index = 0
    line = ''
    for value in data_mem:
        value_str = str(value)
        address = data_mem_address(index)

        if ((index + 1) % 8 != 0):
            value_str = str(value)
            
            line = outputline.format(
                line=line, address=address, value_str=value_str)

        else:
            formatted_line = outputline.format(
                line=line, address=address, value_str=value_str) + '|'
            print_(formatted_line)
            line = ''

        index += 1


def print_stats(stats):
    """
    writes stats, a list of decimal integers representing the instruction statistics, 
    to the console and to the output file
    """
    print_('')
    print_('##########################')
    print_('# Instruction Statistics #')
    print_('##########################\n')

    outputline = '{stat_name:>8}: {stat_value:>7} '
    formatted_line = outputline.format(stat_name='Total', stat_value=stats[0])
    print_(formatted_line)

    percent = (stats[1] / stats[0]) * 100
    print_stat('ALU', stats[1], percent)

    percent = (stats[2] / stats[0]) * 100
    print_stat('Jump', stats[2], percent)

    percent = (stats[3] / stats[0]) * 100
    print_stat('Branch', stats[3], percent)

    percent = (stats[4] / stats[0]) * 100
    print_stat('Memory', stats[4], percent)

    percent = (stats[5] / stats[0]) * 100
    print_stat('Other', stats[5], percent)

    percent = (stats[6] / stats[0]) * 100
    print_stat('Special', stats[6], percent)

# here begins main

input_file = open("_machinecode.txt", "r")
output_file = open("_instructions.txt", "w")

# Initialize Register file
reg = []
while (len(reg) < 5):
    reg.append(0)

# Initialize Instruction Memory
instr_mem = []

# Initialize Data Memory
data_mem = []
while (len(data_mem) < 257):
    data_mem.append(0)

# Initialize Instruction Stats
instr_stats = []

# Fill instruction memory, write mips assembly instructions to output file
line_count = 0
for line in input_file:
    line_count += 1
    print(f'\n Line {line_count}:', end='')
    bin_str = hex_to_bin(line)
    asmline = process(bin_str, instr_mem)
    output_file.write(asmline + '\n')

output_file.close()

output_file = open("_output.txt", "w")

# Execute instruction memory, writes instruction output to output file
execute(instr_mem, reg, instr_stats, data_mem)

# Print final contents of instruction memory, register file, data memory, and instruction statistics
print_instr_mem(instr_mem)
print_reg(reg)
print_data_mem(data_mem)
print_stats(instr_stats)

input_file.close()
output_file.close()
