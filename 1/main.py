
def convertLine(line):

    return line.replace("zero", "0").replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9")


def solution_a1():
    sum = 0
    str_sum = ""
    with open("H:/AdventOfCode/1a/inp.txt", "r") as data:
        for line in data:
            a = ''
            b = ''
            str_sum = ""
            print(line)

            for char in line:
                if (char.isdigit()):
                    a = char
                    break
                
            for char in line:
                if (char.isdigit()):
                    b = char
            

            str_sum = a+b
            print (str_sum)

            if (str_sum):
                sum += int(str_sum)
        print(sum)

def checkPrev(input):
    if (input.find("zero") != -1):
        return '0'
    elif (input.find("one") != -1):
        return '1'
    elif (input.find("two") != -1):
        return '2'
    elif (input.find("three") != -1):
        return '3'
    elif (input.find("four") != -1):
        return '4'
    elif (input.find("five") != -1):
        return '5'
    elif (input.find("six") != -1):
        return '6'
    elif (input.find("seven") != -1):
        return '7'
    elif (input.find("eight") != -1):
        return '8'
    elif (input.find("nine") != -1):
        return '9'
    
    return ''


def solution_a2():
    sum = 0
    str_sum = ""
    with open("H:/AdventOfCode/1a/inp.txt", "r") as data:
        for line in data:
            a = ''
            b = ''
            tmp_a = ""
            tmp_b = ""
            str_sum = ""
            print(line)

            for i in range(0, len(line), 1):
                tmp_a = tmp_a + line[i]
                if (line[i].isdigit()):
                    a = line[i]
                    break
                else:
                    a = checkPrev(tmp_a)
                    if (a != ''):
                        break
                
            for i in range(len(line)-1, -1, -1):
                tmp_b = line[i] + tmp_b
                if (line[i].isdigit()):
                    b = line[i]
                    break
                else:
                    b = checkPrev(tmp_b)
                    if (b != ''):
                        break

            str_sum = a+b
            print (str_sum)

            if (str_sum):
                sum += int(str_sum)
        print(sum)



if __name__ == "__main__":
    
    solution_a2()