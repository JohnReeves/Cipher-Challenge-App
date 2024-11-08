import random
import string
from collections import Counter

ciphertext = "RACMR HEASL BBADG BOESS ERTTE MERAT YBLRO EENLN DONDM OEYRT EACSA ERHSL UIRON DEIRN TWHRE HKRIR SAAED SHNEI TRONA UESWG AAUEC SSCMS ESUAE NDRTI ROMEF SIOPD MLCHY AOTGE HUSLS NOSTI ROMEF SNLTI LEGCE IENUU ROEGT OSSKP AETEN LTBHG OATSH UAIBI IMOTT EONRS ERHVM EJTEA YSNID ASHNR TIEET TISHN SCUEO BTEIN NNWMA TOSEA TRNHV EIEND ISTTC IETAL HRTIH ASEMO AAFNI UNSLG RLWAL INIDA SHERS DEIOT ETASL HIBIS PIEMA RASRL AMIIN SSHOS RWADR YUTGL OLBLC AMNPO YAASS WSARD TEMER HEOAT OENNH CIMSE AAOAF NNMIE NYRTS ATENS IHNDA THEET MRNDD IMEOH FEEWT OSANT TUHEG OUINH KLOTU EARIR TCNUR NIFDE EKRHA RSIEI SRAET RRHET EKONN RSEEU HEATV TRNYE EONSO KIWIS STPUC HTEAT WTHTE AEURV ROOCP THIDE BANEE UWHLO HEADM VDUEA RSTEO ETBEI PHNRI LPCIA TLENO RURTC IOENA MONFN FOCEB IUETT SRHID ANYAI CNMNP OYAOW RFOAA VNMOS COEIB THREE DANND AHISM CIPON SYAUI PTEST CATTH IIIOM SSPIE BSFLR NTOAU EMLTY YEHAD URBDA SWNLA LIMIA BSWLA TLOEA PHPIY ASTDA RWNTU HIRSR IIPNS STUGL BTAYE SWBTL AOERS EPOSR EQUSU ISOTA NOTUB HTIEM ERPAH LIISM TEPWN LALIM IIIDD SHEBR VEYTI TSNOE ORTGR TEEAR HKSAR EIANL RGOHI ETNLS UYESO GSGUT EDTWE HIUTE QISNO SONCE IRCNN TBHGA ERTER HLFII ENRMH EGACI ASNNM TCHDA ETDRR GIDIE EGSAT NNHDA WNEES SESRM EDSAE USEND RDAEU RPASI TVSOE LHLAO WIESL NTDTY EHERU EESJA WFTHE ULROA SEERT FWNUD IROEE LSSVN LAUEB OCRTA ELIAL NSLNE GNIVI AOOTI HNNET EGSDN IEKRH ARSSE IERTS HNIUS AMANC OETND BUEBO DTIOS HMCIE TMNMT HOTET XBHEI IIIOT SNALR PLALO EENDY TBLHY TTOAH FDREE PAIEN RACDO INRWY ATRTH UOROV GRENE NMMHI TTGED SBUEE YDCHB SACIR HAINM NDEIN TTSOI FYLWS UHLLO TYHDR EAYLE BLCSO EINEN RDGIT NRASA TNLAT ACRPI TAEHR NISAH TPETO OSCFT UWRON OAFNM AUTEU CRRTT HSDAE OSOTN ETESO MEBTM EONET ISHIT RPOIT GHFRE AXTEH EBIII OTOHN NETSE SIOUS UEFRC TFYIT OEISH PHEWN MITLM ILTAO EDRRV CEAYF RLHLU EYAAS WRCFN UEOLT NOTDI CEAIA TYNCN CORNN EOORR PUTAU ATBNM GTEAO DNIQE RUDCI ERSEY TEALO TUBHT CPOEA MYWSN NORNR AGAMT EESNE KRHAR SWEIA RONPS IEHPI NRSIF SAOET PHROE TUSRT AOTRH YIUPT BOSEL AKETG ATNSH OIUYG MTPEH EXTOA CUBTS HTUEE ORPRI UIAQT LOMFY EAINC RSACI UETRA ARYNR ENMGT EHTIS INGAT NTHHA ETRCO DHGBA EENEC SRHEU RTUOG OUHIJ TTOSR YNUIE HKITW NCTAE ANETI KHTTW HAAEN AOSWT RFEAK OTIEA NSEIS VGTTN IASOH HIWBC ISNRM GTYOE FMNPA IOLNA TIWIK HEOIT MNOSI RGFTN IODEA NTLED RTDAE ESRDS OBUTO SHOFT MRIWS MASNH ERESA ESHPD RDTAF ERVLO EIPLO RWOTH HIETN NTITE OFNIE OANMX IIGET NIHPI EMARA SRLCM RFGAO OHSER ERFOT LUHHM IGUAS EUNWR AHTHE SXCPE TETIO SNFLU EDSTO TPHHE TESAR HTNUE SRIST WOHEI TMNHU FSGUE TUOLR OEBLD EIAOT RNIWH ISMTF DOYEN TGRSA EDDSR AA"

POPULATION_SIZE = 100
GENERATIONS = 200
CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.1

def initialize_population():
    return [random.sample(string.ascii_uppercase, 26) for _ in range(POPULATION_SIZE)]

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        valid_words = set(word.strip().lower() for word in file)
    return valid_words

def load_special_words(file_path=None):
    if file_path:
        with open(file_path, 'r') as file:
            special_words = set(word.strip().lower() for word in file)
    else:
        special_words = {"babbage", "lovelace", "palmerstone", "ada", "charles", "lord"}
    return special_words

def load_text_from_file(file_path):
    if file_path:
        with open(file_path, 'r') as file:
            cipher_text = file.read()
            text = ''.join(filter(str.isalpha, cipher_text)).upper()
            # text = file.read().replace("\n", "").replace("\r", "").strip().lower()
    return text

def decrypt(ciphertext, alphabet):
    decrypt_dict = str.maketrans(string.ascii_uppercase, ''.join(alphabet))
    return ciphertext.translate(decrypt_dict)

def word_segmentation(text):
    cleaned_text = ''.join(char for char in text.lower() if char in string.ascii_lowercase)
    n = len(cleaned_text)
    dp = [None] * (n + 1)
    dp[0] = []

    for i in range(1, n + 1):
        for j in range(i):
            word = cleaned_text[j:i]
            if word in special_words and dp[j] is not None:
                if dp[i] is None or len(dp[j]) + 1 < len(dp[i]):
                    dp[i] = dp[j] + [word]
            elif word in valid_words and dp[j] is not None:
                if dp[i] is None or len(dp[j]) + 1 < len(dp[i]):
                    dp[i] = dp[j] + [word]

    return dp[n] if dp[n] is not None else []


def fitness_function(decrypted_text):
    # words = decrypted_text.split()
    if not decrypted_text:
        return 0 
    match_count = sum(1 for word in decrypted_text if word.lower() in special_words or valid_words)
    return match_count #/ len(decrypt_text)

def select(population, fitness_scores):
    elite_index = fitness_scores.index(max(fitness_scores))
    return [population[elite_index]] + random.choices(
        population, weights=fitness_scores, k=1
    )

def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        crossover_point = random.randint(1, 25)
        child1 = parent1[:crossover_point] + [c for c in parent2 if c not in parent1[:crossover_point]]
        child2 = parent2[:crossover_point] + [c for c in parent1 if c not in parent2[:crossover_point]]
        return child1, child2
    return parent1[:], parent2[:]

def mutate(alphabet):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(26), 2)
        alphabet[i], alphabet[j] = alphabet[j], alphabet[i]
    return alphabet

def genetic_algorithm():
    population = initialize_population()
    print(population[:5])
    best_fitness_history = []
    
    for generation in range(GENERATIONS):
        fitness_scores = [fitness_function(decrypt(ciphertext, alphabet)) for alphabet in population]
        best_fit = max(fitness_scores)
        best_fitness_history.append(best_fit)
        
        if len(best_fitness_history) > 20 and best_fitness_history[-1] == best_fitness_history[-20]:
            break
        
        best_individual = population[fitness_scores.index(best_fit)]
        
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = select(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            if len(new_population) < POPULATION_SIZE:
                new_population.append(mutate(child2))
        
        population = new_population

    if generation % 10 == 0: 
        print(f"Generation {generation}, Best Fitness: {best_fit}")

    best_individual = population[fitness_scores.index(max(fitness_scores))]
    return ''.join(best_individual), decrypt(ciphertext, best_individual)


dictionary_path= "/usr/share/dict/words"
special_words_path= "special_words.txt"
text_path = "ga_test.txt"

valid_words = load_dictionary(dictionary_path)
special_words = load_special_words(special_words_path)
population = initialize_population()
text = load_text_from_file(text_path)

frequency_counts = Counter(text)
most_common = frequency_counts.most_common()

encoding_alphabet = "CUSTOMNPQRVWXYZABDEFGHIJKL"
decoding_alphabet = "PQARSTUVWXYZFGEHIJCDBKLMNO"


import heapq

fitness_history = []
for decoding_alphabet in population:

    decrypt_text = decrypt(text[:100], decoding_alphabet)
    segmentation_text = word_segmentation(decrypt_text)
    fitness = fitness_function(segmentation_text)
    fitness_history.append(fitness)
    

maxes = heapq.nlargest(2, fitness_history)
elite_index0 = fitness_history.index(maxes[0])
elite_index1 = fitness_history.index(maxes[1])

parent1 = population[elite_index0]
parent2 = population[elite_index1]

population=[]

for x in range(100):
    print(crossover(parent1, parent2))
    population.append(crossover(parent1, parent2))

print(population[:10])

fitness_history = []
for decoding_alphabet in population:
    print(type(decoding_alphabet), decoding_alphabet)
    decoding_alphabet = ''.join(decoding_alphabet)
    decrypt_text = decrypt(text[:100], decoding_alphabet)
    segmentation_text = word_segmentation(decrypt_text)
    fitness = fitness_function(segmentation_text)
    fitness_history.append(fitness)
    

maxes = heapq.nlargest(2, fitness_history)
elite_index0 = fitness_history.index(maxes[0])
elite_index1 = fitness_history.index(maxes[1])

parent1 = population[elite_index0]
parent2 = population[elite_index1]

children=[]

for x in range(100):
    children.append(crossover(parent1, parent2))

print(population[:10])


# best_alphabet, decoded_text = genetic_algorithm()
# print("Best alphabet found:", best_alphabet)
# print("Decoded text:", decoded_text[:500])  
