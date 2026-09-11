with open(r'C:\Users\Георгий\Desktop\MIPT\Второй семинар\input.txt', 'r') as f:
    prepinanie = {'! ', '? ', '. '} 
    text = f.read()
    
    count = 0
    for znak in prepinanie:
        sentences = list(text.split(znak))

    #    print(len(sentences)-1)
        count += (len(sentences)-1)
    #    print(sentences)

    print(count+1)





