def parse_int(string):
    new_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 
    'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
    'ten': 10, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 
    'hundred': 100, 'thousand': 1000, 'million': 1000000}
    kalem = string.replace('-', ' ')
    son = kalem.replace(' and ', ' ')
    if 'one million' in son:
        return 1000000
    elif 'thousand' in son:
        parts1 = son.split('thousand')
        parca = parts1[0].split('hundred')
        yuzluk = parca[0].split()
        gerikalan = parca[1].split()
        toplam1 = 0
        for i in yuzluk:
            toplam1 = toplam1 + (new_dict[i])
        toplam2 = 0
        for j in gerikalan:
            toplam2 = toplam2 + (new_dict[j])
        binlik = toplam1 * 100 + toplam2                         
        parts = parts1[1].split('hundred')
        yuzluk = parts[0].split()
        gerikalan = parts[1].split()
        toplam1 = 0
        for i in yuzluk:
            toplam1 = toplam1 + (new_dict[i])
        toplam2 = 0
        for j in gerikalan:
            toplam2 = toplam2 + (new_dict[j])
        return binlik * 1000 + toplam1 * 100 + toplam2   
    elif 'hundred' in son:
        parts = son.split('hundred')
        yuzluk = parts[0].split()
        gerikalan = parts[1].split()
        toplam1 = 0
        for i in yuzluk:
            toplam1 = toplam1 + (new_dict[i])
        toplam2 = 0
        for j in gerikalan:
            toplam2 = toplam2 + (new_dict[j])
        return toplam1 * 100 + toplam2            
    else:
        kelime = son.split()
        toplam = 0
        for sayi in kelime:
            toplam = toplam + (new_dict[sayi])
        return toplam
    

print(parse_int("nine hundred and eighty-seven thousand six hundred and fifty-four"))