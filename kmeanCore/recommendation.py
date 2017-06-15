from kmeanCore import kmean
from kmeanCore import collegelist


def rec():
    district = input("Enter district:")
    faculty = input("Enter Faculty:")
    rating = input("Enter Rating:")
    affilation = input("Enter Affilation:")
    fee = input("Enter fee:")
    box = []
    st = []
    mov = []
    p = []
    rank1 = []
    rank2 = []
    rank3 = []
    rank4=[]
    rankedlist = []

    scannr = kmean.Kmean(district, faculty, rating, affilation, fee)
    scanresult = scannr.cluster()
    # print(scanresult)
    parser = collegelist.Collegelist(scanresult)
    correct = parser.cases()
    # print(correct)
    for line in correct:
        line = line.split(",")
        # print(line)
        for member in line:
            member = member.strip()
            # print(member)
            box.append(member)
        st = box
        box = []
        mov.append(st)
        # print(st)
    # print(mov)

    for lines in mov:
        if district in lines[1] and faculty in lines[2] and affilation in lines[3]:
            rank = ['1']
            # print(rank)
            lines.extend(rank)
            # print(lines)
            p.append(lines)
        elif (district in lines[1] and faculty in lines[2]) or (district in lines[1] and affilation in lines[3]) or (
                faculty in lines[2] and affilation in lines[3]):
            rank = ['2']
            # print(rank)
            lines.extend(rank)
            # print(lines)
            p.append(lines)
        elif district in lines[1] or faculty in lines[2] or affilation in lines[3]:
            rank = ['3']
            # print(rank)
            lines.extend(rank)
            # print(lines)
            p.append(lines)
        else:
            rank=['4']
            lines.extend(rank)
        # print(lines)
            p.append(lines)
    # print(p)
    for counter in p:
        if counter[-1] is '1':
            rank1.append(counter)
            # print(counter)
            # print(counter[-1])
            # print(rank1)
        elif counter[-1] is '2':
            rank2.append(counter)

        elif counter[-1] is '3':
            rank3.append(counter)
        else:
            rank4.append(counter)

    rankedlist = rank1 + rank2 + rank3+rank4
    print(rankedlist)


if __name__ == '__main__':
    rec()
