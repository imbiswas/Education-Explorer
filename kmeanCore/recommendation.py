from kmeanCore import kmean
from kmeanCore import collegelist


class Recommendation(object):
    def __init__(self, district, faculty, rating, affilation, fee):
        self.district = district
        self.faculty = faculty
        self.rating = rating
        self.affilation = affilation
        self.fee = fee

    def rec(self):
        # district = input("Enter district:")
        # faculty = input("Enter Faculty:")
        # rating = input("Enter Rating:")
        # affilation = input("Enter Affilation:")
        # fee = input("Enter fee:")
        box = []
        st = []
        mov = []
        p = []
        rank1 = []
        rank2 = []
        rank3 = []
        rank4=[]
        rank5=[]
        rank6=[]
        rank7=[]
        rankedlist = []
        tasks = []



        scannr = kmean.Kmean(self.district, self.faculty, self.rating, self.affilation, self.fee)
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
            if self.district in lines[2] and self.faculty in lines[3] and self.affilation in lines[4]:
                rank = ['1']
                # print(rank)
                lines.extend(rank)
                # print(lines)
                p.append(lines)
            elif (self.district in lines[2] and self.faculty in lines[3]):
                rank = ['2']
                # print(rank)
                lines.extend(rank)
                # print(lines)
                p.append(lines)
            elif (self.faculty in lines[3] and self.affilation in lines[4]) or (self.district in lines[2] and self.affilation in lines[4]) :
                rank=['3']
                lines.extend(rank)
                # print(lines)
                p.append(lines)

            elif self.faculty in lines[3]:
                rank = ['4']
                # print(rank)
                lines.extend(rank)
                # print(lines)
                p.append(lines)
            elif self.district in lines[2]:
                rank = ['5']
                # print(rank)
                lines.extend(rank)
                # print(lines)
                p.append(lines)
            elif self.affilation in lines[4]:
                rank = ['6']
                # print(rank)
                lines.extend(rank)
                # print(lines)
                p.append(lines)
            else:
                rank=['7']
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
            elif counter[-1] is '4':
                rank4.append(counter)
            elif counter[-1] is '5':
                rank5.append(counter)
            elif counter[-1] is '6':
                rank6.append(counter)
            else:
                rank7.append(counter)

        rankedlist = rank1 + rank2 + rank3+rank4+rank5+rank6+rank7
        print(rankedlist)
        return rankedlist





