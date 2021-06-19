def get_random_list_harakat(len):
    from pyarabic import araby as ar 
    import random
    harakat = [ar.FATHA, ar.DAMMA, ar.FATHATAN, ar.KASRA, ar.SUKUN, ar.DAMMATAN, ar.SHADDA, ar.KASRATAN]
    list_of_random_harakat = random.sample(harakat, len)
    return list_of_random_harakat





def get_random_tash_lines(num, text):
    import pyarabic.araby as ar
    lines = []
    list_word = text.split(' ')
    
    for _ in range(0,num):
        line = ""
        for word in list_word:
            line +=  ar.joint(word, get_random_list_harakat(len(word))) + " "
        lines.append(line)
    return lines




def random_tash(lineNums):
    from pyarabic.araby import strip_shadda, strip_diacritics, strip_harakat, reduce_tashkeel, strip_lastharaka
    

    import mishkal.tashkeel
    vocalizer = mishkal.tashkeel.TashkeelClass()
    with open(input_file, 'r', encoding='utf-8') as file1:
        text = file1.read()
        lines = get_random_tash_lines(lineNums, text)
        
        full_taskil_text = vocalizer.tashkeel(text)
        text_without_shdaa = strip_shadda(full_taskil_text)
        text_littel_tashkeel = reduce_tashkeel(full_taskil_text)
        text_strip_lastharaka = strip_lastharaka(full_taskil_text)
        text_remove_diacritics = strip_diacritics(full_taskil_text)
        text_without_harakat = strip_harakat(full_taskil_text)
    
        with open(output_file, 'w', encoding='utf8') as file2:

            file2.writelines("\n" + "="* 30)
            file2.writelines("\n" + "التشكيل الاصلي" + "\n")
            file2.writelines("="* 30+ "\n")
            file2.writelines(full_taskil_text + "\n")

            
            file2.writelines("\n" + "="* 30)
            file2.writelines("\n" + "اختزال التشكيل الاصلي" + "\n")
            file2.writelines("="* 30+ "\n")
            file2.writelines(text_without_shdaa + "\n")
            file2.writelines(text_littel_tashkeel + "\n")
            file2.writelines(text_strip_lastharaka + "\n")
            file2.writelines(text_remove_diacritics + "\n")
            file2.writelines(text_without_harakat + "\n")

            file2.writelines("\n" + "="* 30)
            file2.writelines("\n" +"التشكيل العشوائي"+ "\n")
            file2.writelines("="* 30+ "\n")
            for line in lines:
                file2.writelines(line + "\n")





print('\n\n\t\t' + '*'*22)
print('\t\t\t' + 'WELLCOME')
print('\t\t' + '*'*22 + '\n\n')

if __name__ == "__main__":
    input_file = 'input.txt' 
    output_file = 'output.txt' 
    lines_num = 1
    default_file_names = False


    ans = input('use default file names (y/n) : ')
    if ans == 'y' or ans == 'Y' or ans == "yes" or ans == "YES":
        pass
    else:
        input_file = input('read from file name (e.g. file1.txt) : ')
        output_file = input('write to file name (e.g. file2.txt) : ')
    
    lines_num = int(input('Enter number of times you want to random tashkeel (e.g. 5) : '))

    random_tash(lines_num)

