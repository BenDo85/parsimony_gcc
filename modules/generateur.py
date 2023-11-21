import random

def gen_rand_seq(length : int, amount : int) -> list:
    seq_list = []
    
    for _ in range(amount):
        new_seq = ''.join(random.choice('CGTA') for _ in range(length))
        seq_list.append(new_seq)
        
    return seq_list

def gen_rand_com(origin_seq: str, amount: int, mutation_rate: float) -> list:
    seq_list = [origin_seq]
    length = len(origin_seq)
    
    while len(seq_list) < amount:
        index_seq = random.randint(0, len(seq_list) - 1)
        if random.random() < 1 - mutation_rate:
            while True:
                new_seq = ''
                for base in seq_list[index_seq]:
                    if random.random() < 1 / length:
                        new_base = random.choice(['A', 'C', 'G', 'T'])
                        new_seq += new_base
                    else:
                        new_seq += base
                if new_seq != seq_list[index_seq]:
                    seq_list.append(new_seq)
                    break            
        elif len(seq_list) > 1 :
            seq_list.pop(index_seq)
    return seq_list