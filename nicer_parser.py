import os

test_file = "temp.pml.trail"
test_exec = "./a.out"
output_file = "tempfile.txt"

def get_trail_out(executable, trail):
    system_command = "{} -r -S {} > {}".format(executable, trail, output_file)
    os.system(system_command)

def parse_trail_out():
    file = open(output_file)
    lines = file.readlines()
    file.close()

    li = []
    last = ""

    for line in lines:
        spl = line.split()
        if spl[0] == "pan:1:" and spl[1] == "assertion" and spl[2] == "violated" : # end of trail.
            elem = ["WIN", spl[-1][:-1]]
            li.append(elem)
            return li

        elif spl[1] == "-":

            if spl[0] == last:
                #add a skip to other
                if spl[0] == "Opponent":
                    add = ["Avatar", "Skip"]
                else:
                    add = ["Opponent", "Skip"]
                li.append(add)

            elem = [spl[0], spl[-1]]
            last = spl[0]
            li.append(elem)

        elif spl[0] == "MSC:":
            continue

        else:
            elem = ["LOSE", "-1"]
            return li

    delete_command = "rm {}".format(output_file)
    os.system(delete_command)

def print_playback(moves):
    if len(moves) == 0:
        print("LOST - LOST")
    for move in moves:
        print("{} - {}".format(move[0], move[1]))

def record_bot_moves(moves):
    if len(moves) == 0:
        #Throw exception, delete bot moves


if __name__ == "__main__":
    get_trail_out(test_exec, test_file) #passed
    #print_playback(parse_trail_out())
