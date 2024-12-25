def main():
    while True:
        print("Enter your MIPS instruction:")
        inst = input()

        if inst == inst.lower():
            split_input_function(inst)
        else:
            print("Please check whether the input is in lowercase and follows the rules of the MIPS instruction set")

        repeat = input("Do you want to enter another instruction? (yes/no): ")
        if repeat.lower() != "yes":
            break

    print("Thanks!")


def split_input_function(input_str):
    remove_comma = input_str.replace(",", "")
    split_input = remove_comma.split()

    if len(split_input) == 0:
        print("No instruction entered.")
    else:
        op = split_input[0]
        data = split_input[1:]
        instructions(op, data)


def instructions(op, data):
    if op == "and":
        if len(data) == 3:
            rType(data[0], data[1], data[2], "00000", "100100")
        else:
            print("Invalid number of operands for 'and' instruction. Expected format: and $rd, $rs, $rt")
    elif op == "sub":
        if len(data) == 3:
            rType(data[0], data[1], data[2], "00000", "100010")
        else:
            print("Invalid number of operands for 'sub' instruction. Expected format: sub $rd, $rs, $rt")
    elif op == "addi":
        if len(data) == 3:
            iType("001000", data[0], data[1], data[2])
        else:
            print("Invalid number of operands for 'addi' instruction. Expected format: addi $rt, $rs, imm")
    elif op == "subi":
        if len(data) == 3:
            iType("001001", data[0], data[1], data[2])
        else:
            print("Invalid number of operands for 'subi' instruction. Expected format: subi $rt, $rs, imm")
    elif op == "slti":
        if len(data) == 3:
            iType("001010", data[0], data[1], data[2])
        else:
            print("Invalid number of operands for 'slti' instruction. Expected format: slti $rt, $rs, imm")
    elif op == "lw":
        if len(data) == 2:
            offset, base = parseLwSwOffset(data[1])
            if offset is not None and base is not None:
                iType("100011", base, data[0], offset)
            else:
                print("Invalid offset for 'lw' instruction. Expected format: lw $rt, offset($rs)")
        else:
            print("Invalid number of operands for 'lw' instruction. Expected format: lw $rt, offset($rs)")
    elif op == "sw":
        if len(data) == 2:
            offset, base = parseLwSwOffset(data[1])
            if offset is not None and base is not None:
                iType("101011", base, data[0], offset)
            else:
                print("Invalid offset for 'sw' instruction. Expected format: sw $rt, offset($rs)")
        else:
            print("Invalid number of operands for 'sw' instruction. Expected format: sw $rt, offset($rs)")
    elif op == "beq":
        if len(data) == 3:
            iTypeLabel("000100", data[0], data[1], data[2])
        else:
            print("Invalid number of operands for 'beq' instruction. Expected format: beq $rs, $rt, label")
    elif op == "bne":
        if len(data) == 3:
            iTypeLabel("000101", data[0], data[1], data[2])
        else:
            print("Invalid number of operands for 'bne' instruction. Expected format: bne $rs, $rt, label")
    elif op == "j":
        if len(data) == 1:
            jType("000010", data[0])
        else:
            print("Invalid number of operands for 'j' instruction. Expected format: j target")
    elif op == "jr":
        if len(data) == 1:
            rType(data[0], "00000", "00000", "00000", "001000")
        else:
            print("Invalid number of operands for 'jr' instruction. Expected format: jr $rs")
    elif op == "li":
        if len(data) == 2:
            iType("001111", "$zero", data[0], data[1])
        else:
            print("Invalid number of operands for 'li' instruction. Expected format: li $rt, immediate")
    elif op == "bgt":
        if len(data) == 3:
            iTypeLabel("000111", data[0], data[1], data[2])
        else:
            print("Invalid number of operands for 'bgt' instruction. Expected format: bgt $rs, $rt, label")
    elif op == "bge":
        if len(data) == 3:
            iTypeLabel("000110", data[0], data[1], data[2])
        else:
            print("Invalid number of operands for 'bge' instruction. Expected format: bge $rs, $rt, label")
    elif op == "blt":
        if len(data) == 3:
            iTypeLabel("000100", data[0], data[1], data[2])
        else:
            print("Invalid number of operands for 'blt' instruction. Expected format: blt $rs, $rt, label")
    elif op == "ble":
        if len(data) == 3:
            iTypeLabel("000101", data[0], data[1], data[2])
        else:
            print("Invalid number of operands for 'ble' instruction. Expected format: ble $rs, $rt, label")
    elif op == "jlar":
        if len(data) == 1:
            jType("011010", data[0])
        else:
            print("Invalid number of operands for 'jlar' instruction. Expected format: jlar target")
    elif op == "sll":
        if len(data) == 3:
            rType(data[0], "00000", data[1], data[2], "000000")
        else:
            print("Invalid number of operands for 'sll' instruction. Expected format: sll $rd, $rt, sa")
    elif op == "srl":
        if len(data) == 3:
            rType(data[0], "00000", data[1], data[2], "000010")
        else:
            print("Invalid number of operands for 'srl' instruction. Expected format: srl $rd, $rt, sa")
    elif op == "sra":
        if len(data) == 3:
            rType(data[0], "00000", data[1], data[2], "000011")
        else:
            print("Invalid number of operands for 'sra' instruction. Expected format: sra $rd, $rt, sa")
    elif op == "sllv":
        if len(data) == 3:
            rType(data[0], data[2], data[1], "00000", "000100")
        else:
            print("Invalid number of operands for 'sllv' instruction. Expected format: sllv $rd, $rt, $rs")
    elif op == "srlv":
        if len(data) == 3:
            rType(data[0], data[2], data[1], "00000", "000110")
        else:
            print("Invalid number of operands for 'srlv' instruction. Expected format: srlv $rd, $rt, $rs")
    elif op == "srav":
        if len(data) == 3:
            rType(data[0], data[2], data[1], "00000", "000111")
        else:
            print("Invalid number of operands for 'srav' instruction. Expected format: srav $rd, $rt, $rs")
    elif op == "jr":
        if len(data) == 1:
            rType(data[0], "00000", "00000", "00000", "001000")
        else:
            print("Invalid number of operands for 'jr' instruction. Expected format: jr $rs")
    elif op == "jalr":
        if len(data) == 2:
            rType(data[0], data[1], "00000", "00000", "001001")
        else:
            print("Invalid number of operands for 'jalr' instruction. Expected format: jalr $rd, $rs")
    elif op == "mfhi":
        if len(data) == 1:
            rType(data[0], "00000", "00000", "00000", "010000")
        else:
            print("Invalid number of operands for 'mfhi' instruction. Expected format: mfhi $rd")
    elif op == "mflo":
        if len(data) == 1:
            rType(data[0], "00000", "00000", "00000", "010010")
        else:
            print("Invalid number of operands for 'mflo' instruction. Expected format: mflo $rd")
    elif op == "mult":
        if len(data) == 2:
            rType("00000", data[0], data[1], "00000", "011000")
        else:
            print("Invalid number of operands for 'mult' instruction. Expected format: mult $rs, $rt")
    elif op == "multu":
        if len(data) == 2:
            rType("00000", data[0], data[1], "00000", "011001")
        else:
            print("Invalid number of operands for 'multu' instruction. Expected format: multu $rs, $rt")
    elif op == "div":
        if len(data) == 2:
            rType("00000", data[0], data[1], "00000", "011010")
        else:
            print("Invalid number of operands for 'div' instruction. Expected format: div $rs, $rt")
    elif op == "divu":
        if len(data) == 2:
            rType("00000", data[0], data[1], "00000", "011011")
        else:
            print("Invalid number of operands for 'divu' instruction. Expected format: divu $rs, $rt")
    elif op == "add":
        if len(data) == 3:
            rType(data[0], data[1], data[2], "00000", "100000")
        else:
            print("Invalid number of operands for 'add' instruction. Expected format: add $rd, $rs, $rt")
    elif op == "addu":
        if len(data) == 3:
            rType(data[0], data[1], data[2], "00000", "100001")
        else:
            print("Invalid number of operands for 'addu' instruction. Expected format: addu $rd, $rs, $rt")
    elif op == "sub":
        if len(data) == 3:
            rType(data[0], data[1], data[2], "00000", "100010")
        else:
            print("Invalid number of operands for 'sub' instruction. Expected format: sub $rd, $rs, $rt")
    elif op == "subu":
        if len(data) == 3:
            rType(data[0], data[1], data[2], "00000", "100011")
        else:
            print("Invalid number of operands for 'subu' instruction. Expected format: subu $rd, $rs, $rt")
    elif op == "and":
        if len(data) == 3:
            rType(data[0], data[1], data[2], "00000", "100100")
        else:
            print("Invalid number of operands for 'and' instruction. Expected format: and $rd, $rs, $rt")
    elif op == "or":
        if len(data) == 3:
            rType(data[0], data[1], data[2], "00000", "100101")
        else:
            print("Invalid number of operands for 'or' instruction. Expected format: or $rd, $rs, $rt")
    elif op == "xor":
        if len(data) == 3:
            rType(data[0], data[1], data[2], "00000", "100110")
        else:
            print("Invalid number of operands for 'xor' instruction. Expected format: xor $rd, $rs, $rt")
    elif op == "nor":
        if len(data) == 3:
            rType(data[0], data[1], data[2], "00000", "100111")
        else:
            print("Invalid number of operands for 'nor' instruction. Expected format: nor $rd, $rs, $rt")
    elif op == "slt":
        if len(data) == 3:
            rType(data[0], data[1], data[2], "00000", "101010")
        else:
            print("Invalid number of operands for 'slt' instruction. Expected format: slt $rd, $rs, $rt")
    elif op == "sltu":
        if len(data) == 3:
            rType(data[0], data[1], data[2], "00000", "101011")
        else:
            print("Invalid number of operands for 'sltu' instruction. Expected format: sltu $rd, $rs, $rt")
    else:
        print("Invalid instruction: " + op)

def rType(rd, rs, rt, sa, fn):
    if not register_dollar_check(rd) or not register_dollar_check(rs) or not register_dollar_check(rt):
        return

    print("000000 {:05d} {:05d} {:05d} {} {}".format(registerNumber(rs), registerNumber(rt), registerNumber(rd), sa, fn))


def jType(opc, label):
    print("{} {}".format(opc, label))


def iType(opc, rs, rt, data):
    if not register_dollar_check(rs) or not register_dollar_check(rt):
        return

    imm_value = parseImmediateValue(data)
    if imm_value is None:
        print("Invalid immediate value for 'iType' instruction.")
    else:
        print("{} {:05d} {:05d} {:016b}".format(opc, registerNumber(rs), registerNumber(rt), imm_value))


def iTypeLabel(opc, rs, rt, data):
    if not register_dollar_check(rs) or not register_dollar_check(rt):
        return

    label_address = parseLabel(data)
    if label_address is None:
        print("Invalid label '{}' for 'iTypeLabel' instruction.".format(data))
    else:
        print("{} {:05d} {:05d} {:016b}".format(opc, registerNumber(rs), registerNumber(rt), label_address))



def parseImmediateValue(imm_str):
    try:
        if imm_str.startswith("0x"):
            return int(imm_str, 16)
        elif imm_str.startswith("0b"):
            return int(imm_str, 2)
        else:
            return int(imm_str)
    except ValueError:
        return None


def parseLabel(label):
    labels = {
        "loop": 0x100,
        "start": 0x200,

    }
    if label in labels:
        return labels[label]
    else:
        return None


def check_Offset(offset_str):
    try:
        if offset_str.startswith("-"):
            offset = -int(offset_str[1:])
        elif offset_str.startswith("+"):
            offset = int(offset_str[1:])
        else:
            offset = int(offset_str)

        base = offset_str[offset_str.index("(") + 1: offset_str.index(")")]
        return offset, base
    except ValueError:
        return None, None


def register_dollar_check(r):
    if not r.startswith("$"):
        print("The register should start with '$' sign.")
        return False

    if r not in [
        "$zero", "$at", "$v0", "$v1", "$a0", "$a1", "$a2", "$a3", "$t0", "$t1",
        "$t2", "$t3", "$t4", "$t5", "$t6", "$t7", "$s0", "$s1", "$s2", "$s3",
        "$s4", "$s5", "$s6", "$s7", "$t8", "$t9", "$k0", "$k1", "$gp", "$sp",
        "$fp", "$ra"
    ]:
        print("Invalid register '{}'. Please use one of the MIPS registers.".format(r))
        return False

    return True


def registerNumber(r):
    register_map = {
        "$zero": 0, "$at": 1, "$v0": 2, "$v1": 3, "$a0": 4, "$a1": 5, "$a2": 6, "$a3": 7,
        "$t0": 8, "$t1": 9, "$t2": 10, "$t3": 11, "$t4": 12, "$t5": 13, "$t6": 14, "$t7": 15,
        "$s0": 16, "$s1": 17, "$s2": 18, "$s3": 19, "$s4": 20, "$s5": 21, "$s6": 22, "$s7": 23,
        "$t8": 24, "$t9": 25, "$k0": 26, "$k1": 27, "$gp": 28, "$sp": 29, "$fp": 30, "$ra": 31
    }

    return register_map[r]


main()
