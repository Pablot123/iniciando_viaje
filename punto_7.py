text = 'thor lanzó su martillo#flash ha fallado por un pie! -gritó Loki Laufeyson#dos pies -le corrigió Hulk#flash menea la cabeza como disgustado...-agrega el comentarista'

#First split the text with the '#'
text_splited = text.split('#')
#Second capitalize each part
text_splited[0] = text_splited[0].capitalize()
text_splited[1] = text_splited[1].capitalize()
text_splited[2] = text_splited[2].capitalize()
text_splited[3] = text_splited[3].capitalize()

#Third, insert diferents characters that are not in the goal text, like '...' on the first line,
# '-' on the begining of each line, the '!' on the second line and period '.' in each line
first_line = text_splited[0].split()
first_line.append('...') # ['Thor', 'lanzó', 'su', 'martillo', '...']
first_line = " ".join(first_line[:3]) + ' ' + "".join(first_line[3:])
#print(first_line)

second_line = text_splited[1].split()
second_line.insert(0,'-¡')#['-¡', 'Flash', 'ha', 'fallado', 'por', 'un', 'pie!', '-gritó', 'loki', 'laufeyson']
second_line.append('.')
second_line = "".join(second_line[:2]) + ' ' + " ".join(second_line[2:-1]) + second_line[-1]
#print(second_line)

third_line = text_splited[2].split()
third_line.insert(0,'-')#['-', 'Dos', 'pies', '-le', 'corrigió', 'hulk']
third_line.append('.')
third_line = third_line[0] + " ".join(third_line[1:-1]) + third_line[-1]
#print(third_line)

fourth_line = text_splited[3].split()
fourth_line.insert(0, '-') #['-', 'Flash', 'menea', 'la', 'cabeza', 'como', 'disgustado...-agrega', 'el', 'comentarista']
fourth_line.append('.')
fourth_line = fourth_line[0] + " ".join(fourth_line[1:-1]) + fourth_line[-1]
#print(fourth_line)

#get the modified text together again with the eenter space
fixed_text = first_line +'\n'+ second_line +'\n'+ third_line +'\n'+ fourth_line
print(fixed_text)

goal_text = '''
Thor lanzó su martillo...
    -¡Flash ha fallado por un pie! -gritó LokiLaufeyson. 
    -Dos pies le corrigió Hulk.
    -Flash menea la cabeza como disgustado... -agrega el comentarista.
'''