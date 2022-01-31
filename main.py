from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


def unique_koala_facts(number):
    fact_list = []
    while (len(fact_list)) < number:
        fact = random_koala_fact()
        if fact not in fact_list:
            fact_list.append(fact)
    return fact_list


def num_joey_facts():
    init_fact = random_koala_fact()
    joey_list = []
    i = 0
    while i < 10:
        fact = random_koala_fact()
        if fact == init_fact:
            i = i+1
        if ('joey' in fact) and (fact not in joey_list):
            joey_list.append(fact)
    return len(joey_list)


def koala_weight():
    i = 1
    while i > 0:
        fact = random_koala_fact()
        if 'kg' in fact:
            i -= 1
            weight_fact = fact
    index_kg = weight_fact.find('kg')
    weight = weight_fact[(index_kg-2):index_kg]
    return weight


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())
    unique_koala_facts(3)
    num_joey_facts()
    koala_weight()
