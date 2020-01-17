import random

def main():
    print('typing game q=quit')
    choice = input('0 = words\n1 = random\n')
    if choice == '0':
        letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
        wordlen = 5
    else:
        letters = '''abcdefghijklmnopqrstuvwxyz0123456789'"?_,.:;()+-{[*%&/=@#%&üäö'''
        wordlen = 10
   
    # read wordlist source: https://github.com/first20hours/google-10000-english
    fin = open('typing_trainer.txt', encoding='latin-1')    
    word_list = fin.readlines()
    word_list = [s.strip() for s in word_list if len(s.strip())>3]
    fin.close()

    iCount = 0
    change_word = True

    while True:
        if change_word:
            if choice == '0':
                s0 = get_word(word_list)
            else:
                s0 = make_string(wordlen, letters)
            
        s1 = input(f'{s0}\n')
        if s1 == 'q':
            print(f'{iCount} groups played')
            break
        elif s0 == s1:
            iCount = iCount + 1
            print(f'>> {iCount}')
            change_word = True
        else:
            print('--- wrong ---')
            change_word = False

def make_string(l, letters):
    r = ''
    for n in range(l):
        r = r + random.choice(letters)
    return r

def get_word(word_list):
    return random.choice(word_list)
main()


