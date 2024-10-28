import random

def son_top(x=10):
    taxminiy_son = random.randint(1, x)
    print("Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")
    taxminlar = 0
    
    while True:
        taxminlar += 1
        taxmin = int(input('>>>'))
        
        if taxmin < taxminiy_son:
            print("Men o'ylagan son bundan katta. Yana harakat qiling!")
        elif taxmin > taxminiy_son:
            print("Men o'ylagan son bundan kichik. Yana harakat qiling!") 
        else:
            break
        
    print(f"Siz {taxminlar} ta taxmin bilan yutdingiz!")
    return taxminlar
        
def son_top_pc(x=10):
    input("Siz 1 dan {x} gacha son o'ylang. Topishga harakat qilaman."
          "Istalgan tugmani bosing!")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = print(f"Siz {taxmin} sonini o'yladingiz." 
                      f"Topgan bo'lsam (t) ni bosing, o'ylagan son bundan kattaroq (+),"
                      f"o'ylagan son bundan kattaroq (-)".lower())
        if javob == '-':
            yuqori = taxmin - 1
        elif javob == '+':
            quyi = taxmin + 1
        else: 
            break
    print(f"Men {taxminlar} ta taxmin bilan yutdim!")    
    return taxminlar       
    
        
    
    