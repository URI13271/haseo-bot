import random

def dice():
    n = random.randrange(1,7)
    m = random.randrange(1,7)

    if n > m:
        return "졌음 ㅋ", 0xFF0000, str(n), str(m)
    
    elif n == m:
        return "무승부?... ㄷ..",0xFAFA00, str(n), str(m)

    elif n < m:
        return "승리; ㅠ..",0x00ff56, str(n), str(m)