import math
import random
import time

#Συνάρτηση παραγωγής τυχαίου αριθμού με 100 bits
def get_random_100_bits():
    while True:
        N = random.getrandbits(100)
        if N.bit_length() == 100:
            break
    return N

def lehman_algorithm(N):
    start_time = time.time()
    found_divisor = False
    #Ευκολα παρατήσουμε ότι στις διαιρέσεις μας παίρνουμε το ακαριαίο μέρος τους(//) καθώς δεν μπορούμε να έχουμε δεκαδικό μέσα στη for
    for k in range(1, int(N ** (1/3)) + 1):
        for a in range(int((4 * k * N) ** (1/2)) + 1, int(( 4 * k * N) ** (1/2) + ((N ** (1/6)) / (4 * (k ** (1/2))) ) + 1 ) ):
            b = (a**2 - 4 * k * N) ** (1/2)
            #Έλεγχος αν έχει περάσει τα 10 δευτερόλεπτα και σταματάει τον εσωτερικό βρόχο κάνοντας και την μεταβλητή found_divisor True
            if int(b.real)== b:
                divisor = math.gcd(a - int(b), N)
                elapsed_time = time.time() - start_time
                if (elapsed_time > 10):
                    found_divisor = True
                    break
                if divisor != 1 and divisor != N:
                    return divisor
        #Ελέγχει αν η μεταβλητή έχει γίνει True με σκοπό να σταματήσει και η δεύτερη εντολή επανάληψης και να επιστραφεί η τιμή None
        if found_divisor:
            break
    return None

Successful = 0
Fail = 0
i = 0
while (i < 1000):
    N = get_random_100_bits()
    result = lehman_algorithm(N)
    i += 1
    print(i)
    if (result == None):
        Fail += 1
    else:
        Successful += 1

print('Succesful', Successful )
print('Fail', Fail)
