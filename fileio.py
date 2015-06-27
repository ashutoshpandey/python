lineCount = 0

# with will automatically close file
with open('d:/test.txt', mode='w', encoding='utf-8') as file:
    file.write('Copy and paste is a design error.')
    file.write('\nThis is another line')
    file.write('\nThis is last line')

with open('d:/test.txt', encoding='utf-8') as file:
    for line in file:
        lineCount += 1
        print('{:<5} {}'.format(lineCount, line.rstrip()))