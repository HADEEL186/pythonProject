

def longestword(filetext):
    with open(filetext, "r") as file:
        readword= file.read().split()
        longword = len(max(readword , key=len))
        for word in readword:
            if len(word) == longword:
                result = word
        return result
x= longestword("results.txt")
print(x)

def numlines(filetext):
    with open(filetext, "r") as file:
        file.read()
        file.seek(0)
        lines = len(file.readlines())
        return lines

y= numlines("results.txt")
print(y)

def main():
    with open("originalfile.txt","a") as file:
        file.write("\n\n")
        file.write((longestword("results.txt").upper()+" "))*(numlines("results.txt")+1)
        file.write("\n")

        for i in range(0,7):
            for j in range(0, 7):
                if (i == j or j == 7 - 1 - i):
                   print('*', end='')
                else:
                    print(' ', end='')
            print()
if __name__=="__main__":
    main()
