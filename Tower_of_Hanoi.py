# Towers of Hanoi - 64 ddisks 3 poles


from_pole = "P1"
to_pole = "P3"
spare_pole = "P2"

count = 0


def printMove(fr, to):
    print("move the top disk from ", fr, "to", to)


def Towers(n, fr, to, spare):

    if n == 1:
        printMove(fr, to)
        global count
        count += 1
    else:
        Towers(n - 1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n - 1, spare, to, fr)

    return count


size = int(input("Enter no of disks:\t"))
print("We are moving the disks from P1 to P3.\n")
print("\nNo of moves = ", Towers(size, from_pole, to_pole, spare_pole))
