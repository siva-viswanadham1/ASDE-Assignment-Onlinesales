import csv

if __name__ == '__main__':
    file_path=input("Enter file path")
    mode='r'
    with open(file=file_path,mode=mode) as myfile:
        csv_reder=csv.reader(myfile)
        departments=list(csv_reder)
        for line in departments:
            for word in line:
                print(word,'/t',end=' ')
                print()





