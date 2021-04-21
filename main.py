def main():
    start = '<h3>'
    end = '</h3>'
    source_file = open('source.txt', mode='r', encoding='utf-8')
    txt = source_file.read()

    for _ in range(76):
        print(txt[int(txt.find(start)) + len(start):int(txt.find(start)) + int(txt[int(txt.find(start)):].find(end))])
        txt = txt[int(txt.find(start)) + int(txt[int(txt.find(start)):].find(end)) + len(end):]


if __name__ == '__main__':
    main()
