from modules.generateur import gen_rand_seq, gen_rand_com
import random

if __name__ == "__main__":
    # Pour rendre le hasard repoductible
    random.seed(0)
    # Génération de 10 séquences au hasard
    print(gen_rand_seq(5, 10))
    # Génération de 10 séquences à partir d'une originale
    # Le 3ème paramètre est le taux de mutation
    print(gen_rand_com("AAAAA", 10, 0.6))
