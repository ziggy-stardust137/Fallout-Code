import random 
import string
from random_word import RandomWords

r = RandomWords()

kelime_sayisi = 12
kelime_uzunlugu = 6

kelimeler = []

while len(kelimeler) < kelime_sayisi:
    
    yeni_kelime = r.get_random_word()

    if yeni_kelime and len(yeni_kelime) == kelime_uzunlugu:
        yeni_kelime_ust = yeni_kelime.upper()
        if yeni_kelime_ust not in kelimeler:
            kelimeler.append(yeni_kelime_ust)
    

gizli_sifre = random.choice(kelimeler)

print("\n" + "="*40)
print("ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM")
print("ENTER PASSWORD NOW")
print("="*40 + "\n")

for kelime in kelimeler:
    semboller = string.punctuation
    satir_genisligi = 25

    satir = list("".join(random.choices(semboller, k=satir_genisligi)))
    baslangic_index = random.randint(0, satir_genisligi - kelime_uzunlugu)
    satir[baslangic_index: baslangic_index + kelime_uzunlugu] = list(kelime)


    on_ek = "".join(random.choices(semboller, k=10))
    arka_ek = "".join(random.choices(semboller, k=10))
    adres = hex(random.randint(0x1000, 0xFFFF)).upper()

    print(f"{adres}  {''.join(satir)}")

    

deneme_hakki = 4

while deneme_hakki > 0:
    print(f"\n({deneme_hakki} ATTEMPT(S) LEFT)")
    tahmin = input("ENTER PASSWORD: ").upper()

    if tahmin == gizli_sifre:
        print("\n>>> [[ACCESS GRANTED] <<<")
        break
    elif tahmin not in kelimeler:
        print("!!! ERROR: INVALID WORD. PLEASE SELECT FROM THE LIST !!!")
    else:

        likeness = 0
        for i in range(kelime_uzunlugu):
            if tahmin[i] == gizli_sifre[i]:
                likeness += 1
        deneme_hakki -= 1
        print(f"Entry Denied. Likeness={likeness}")

if deneme_hakki == 0:
    print(f"\nTERMINAL LOCKED. CORRECT PASSWORD: {gizli_sifre}")

          

