"""
M01

Toteuta alla oleviin funktiopohjiin Caesar-salaus. Modulin
pääohjelmaan on toteutettu testi, jonka avulla voit testata
ja suunnitella toteutustasi.

1) Salaamaton viesti sisältää kirjaimia a-z tai A-Z sekä välilyöntejä
   ja muita erikoismerkkejä
2) Kaikki kirjaimet muutetaan isoiksi kirjaimiksi ennen salausta
3) Välilyönnit ja erikoismerkit jätetään sellaisenaan salattuun viestiin
4) Oikealla avaimella purettu viesti on identtinen alkuperäisen
   salaamattoman viestin kanssa, lukuun ottamatta sitä, että kaikki
   kirjaimet ovat muuttuneet isoiksi.
"""

N_ALPHABETS=26

#Palauttaa salatun vietin, K=avain, M=salattava viesti
def E(K, M):

    #Your code here

    return C


#Palauttaa salaamattoman vietin, K=avain, C=salattu viesti
def D(K, C):

    #Your code here

    return M


#Don't modify test code
if __name__=="__main__":
    M='Et osaa murtaa tata!'
    K=16
    print(f'M = "{M}"')
    print(f'K = {K}')

    C=E(K, M)
    print(f'C = "{C}"')
    
    M_received=D(K, C)
    print(f'M_received = "{M_received}"')
    assert M.upper()==M_received.upper()

    print('Test passed')
