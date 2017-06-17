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
            if self.district in lines[1] and self.faculty in lines[2] and self.affilation in lines[3]:
                rank = ['1']
                # print(rank)
                lines.extend(rank)
                # print(lines)
                p.append(lines)
            elif (self.district in lines[1] and self.faculty in lines[2]):
                rank = ['2']
                # print(rank)
                lines.extend(rank)
                # print(lines)
                p.append(lines)
            elif (self.district in lines[1] and self.affilation in lines[3]) or (self.faculty in lines[2] and self.affilation in lines[3]):
                rank=['3']
                lines.extend(rank)
                # print(lines)
                p.append(lines)

            elif self.district in lines[1] or self.faculty in lines[2] or self.affilation in lines[3]:
                rank = ['4']
                # print(rank)
                lines.extend(rank)
                # print(lines)
                p.append(lines)
            else:
                rank=['5']
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
            elif counter[-1] is '3':
                rank4.append(counter)
            else:
                rank5.append(counter)

        rankedlist = rank1 + rank2 + rank3+rank4+rank5
        #print(rankedlist)
        return rankedlist





