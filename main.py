import sys

def main():
    start = '<h3>'
    end = '</h3>'
    source_file = open('source.txt', mode='r')
    txt = source_file.read()

    l = []

    for _ in range(76):
        line = txt[int(txt.find(start)) + len(start):
                   int(txt.find(start)) + int(txt[int(txt.find(start)):].find(end))].replace('\n', '')
        print(line)
        txt = txt[int(txt.find(start)) + int(txt[int(txt.find(start)):].find(end)) + len(end):]
        l.append(line + '\n')

    source_file.close()

    f = open("result.txt", "w")

    for i in l:
        f.writelines(i)

    f.close()


if __name__ == '__main__':
    main()
