import csv
from collections import Counter


def main():
    file_path = input("Input file path: ")
    print("Start parsing file...")
    objects = []
    with open(file_path, 'r', newline='') as csvfile:
        spam_reader = csv.reader(csvfile, delimiter=',')
        for row in spam_reader:
            a = row[-2]
            if a == "B":
                objects.append(row)

    print("Start writing...")
    with open('data.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(objects)
    print("Writing complete!")
    # print([k for k, v in Counter(objects).items() if v > 1])


if __name__ == '__main__':
    main()
