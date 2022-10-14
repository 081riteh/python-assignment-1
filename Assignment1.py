Hawaiian_char=['p','k','h','l','m','n','w','a','e','i','o','u',' ','\'']
vowel_combination={
    'a':'ah',
    'e':'eh',
    'i':'ee',
    'o':'oh',
    'u':'oo',
    'ai':'eye',
    'ae':'eye',
    'ao':'ow',
    'au':'ow',
    'ei':'ay',
    'eu':'eh-oo',
    'iu':'ew',
    'oi':'oy',
    'ou':'ow',
    'ui':'ooey'
}


def check_word(str):
    for i in str:
        if i not in Hawaiian_char:
            return i

    return 'true'

def convert(str):
    ans=""
    i=0
    while(i<len(str)):
        if(str[i] not in vowel_combination.keys()):
            if i>0 and str[i]=='w' and str[i-1] in ['i','e']: 
                ans +='v'
            elif(str[i]==' ' or str[i]=='\''):
                if(ans[-1]=='-'):
                    ans=ans[:-1] 
                    ans +=str[i]
                else:
                    ans +=str[i]
                    
            else:
               ans +=str[i]
            i +=1
        else:
            if i<len(str)-1 and (str[i]+str[i+1]) in vowel_combination.keys():
                ans +=vowel_combination[(str[i]+str[i+1])]+'-'
                i +=2
            else:
                ans +=vowel_combination[str[i]]+'-'
                i +=1
    if(ans[-1]=='-'):
        return ans[:-1]
    return ans


choice='y'
while(choice=='y' or choice=='yes'):
    print("\n")
    word=input("Enter a hawaiian word to pronounce ==>  ").lower()
    flag=check_word(word)
    if(flag!='true'):
        print(flag.upper()+"  is not a valid hawaiian character")
        continue
    else:
        print(word.upper()+" is pronounced "+convert(word).capitalize())
        choice=input("Do you want to enter another word? Y/YES/N/NO ==> ").lower()
        while(choice not in ['y','yes','n','no']):
            print("Enter Y, YES, N or NO")
            choice=input("Do you want to enter another word? Y/YES/N/NO ==> ").lower()