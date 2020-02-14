import os

test_string = "564:	proc  3 (opponent) tryit.pml:158 (state 57)	[(((win==0)&&(dead==0)))]"
test_string2 = "global vars:"
test_exec = "../test1/a.out"
test_trail = "../test1/tryit.pml1.trail"

def parse_line(line):
    print(line)
    spl = line.split()

    proc = 'SKIP'
    state = 'SKIP_'
    for asd in spl:

        if asd == "MSC:":
            return ['START','START']
        elif asd == "global":
            return ['END', 'END']
        elif asd == "proc":
            proc =  spl[spl.index(asd) + 1]
        elif asd == "(state":
            state = spl[spl.index(asd) + 1]

    return [proc, state[:-1]]

def parse_file(execu, trail):
    exec_string = "{} -r {} > {}".format(execu, trail, "states_file")
    os.system(exec_string)


    file = open('states_file', 'r')
    lines = file.readlines()
    file.close()

    os.system('rm states_file')

    li = []

    for line in lines:
        elem = parse_line(line)
        if elem == ['-1', '-1']:
            break
        li.append(elem)

    return li

def ret_state_trans_list(execu, trail):
    qwe = parse_file(execu, trail)
    ret = []
    for elem in qwe:
        if elem == ["END", "END"]:
            break
        elif elem[0] == "START" or elem[0] == "SKIP" or elem[1] == "START" or elem[1] == "SKIP":
            continue
        ret.append(elem)

    return ret


if __name__ == "__main__":

    #print parse_line(test_string) #passed functional test
    #print parse_line(test_string2) #passed functional test

    #print parse_file(test_exec, test_trail) #passed functional test

    print(ret_state_trans_list(test_exec, test_trail)) #passed functional test
