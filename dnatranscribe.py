def main():
    dnastr = input(str("Please input the dna string to be transcribed: ")) # holds dna as str
    
    dnaArr = [] # create empty array to move dna into

    for i in range(len(dnastr)):
        dnaArr.append(dnastr[i])

    rnaArr = [] # empty array to hold rna transcription

    # replace all t's with u's as that is how rna differs from dna
    for i in range(len(dnastr)):
        if dnaArr[i] == 'T':
            rnaArr.append('U')
        else:
            rnaArr.append(dnaArr[i])
    # print rna string
    print("---------Rna String----------")
    for i in range(len(rnaArr)):
        print(rnaArr[i], end="")
    # print newline
    print()

main()