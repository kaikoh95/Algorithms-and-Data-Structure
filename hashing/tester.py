from spelling import *

dictionary = load_dict_words("words_latin-1.txt")
document = load_doc_words("sherlock.txt")

#spellcheck_with_list(document, dictionary)

# see http://www.bigprimes.net/archive/prime/
# for a big list of prime numbers
# prime sized hashtables help modulo hashing spread hash values evenly
# prime sizing is also important for quadratic probing to work effectively,
# especially with high load factors

    
#spellcheck_with_hashtable(document, dictionary, 'Chaining', 11)
#spellcheck_with_hashtable(document, dictionary, 'Chaining', 1000003)
#spellcheck_with_hashtable(document, dictionary, 'Linear', 2000003)
#spellcheck_with_hashtable(document, dictionary, 'Quadratic', 1000003)
#spellcheck_bin(document, dictionary)

#You can use print statements between store commands
#to see how the hashtable fills up.
#For example:
#hash_table = ChainingHashTable(5)
#hash_table.store('Paul')
#print(hash_table)
#hash_table.store('Peter')
#print(hash_table)
#hash_table.store('Paula')
#print(hash_table)
#hash_table.store('David')
#print(hash_table)
#hash_table.store('Bobby')
#print(hash_table)
#hash_table.store('Dianne')
#print(hash_table)


#hash_table = ChainingHashTable(5)
#hash_table.store('George')
#hash_table.store('Bungle')
#hash_table.store('Zippy')
#hash_table.store('Jane')
#hash_table.store('Rod')
#hash_table.store('Freddy')

#hash_table = LinearHashTable(7)
#hash_table.store('Tennis')
#print(hash_table)
#hash_table.store('Cricket')
#print(hash_table)
#hash_table.store('Swimming')
#print(hash_table)
#hash_table.store('Underwater Motorbike Hockey')
#print(hash_table)
#hash_table.store('Soccer')
#print(hash_table)


#hash_table = QuadraticHashTable(7)
#hash_table.store('Paul')
#print(hash_table)
#hash_table.store('Peter')
#print(hash_table)
#hash_table.store('Paula')
#print(hash_table)
#hash_table.store('David')
#print(hash_table)
#hash_table.store('Bobby')
#print(hash_table)
#hash_table.store('Dianna')
#print(hash_table)
#hash_table.store('Dick')
#print(hash_table)
#hash_table.store('Bob')
#print(hash_table)
#hash_table.store('Bart')
#print(hash_table)


hash_table = QuadraticHashTable(7)
hash_table.store('Aby')
hash_table.store('Ken')
hash_table.store('Nat')
hash_table.store('Jim')
hash_table.store('Bob')
print(hash_table)

#hash_table = LinearHashTable(7)
#hash_table.store('Aby')
#hash_table.store('Ken')
#hash_table.store('Nat')
#hash_table.store('Jim')
#hash_table.store('Bob')
#print(hash_table)

'''
hash_table = ChainingHashTable(5)
hash_table.store('Paul')
hash_table.store('Peter')
hash_table.store('Paula')
hash_table.store('David')
hash_table.store('Bob')
hash_table.store('Di')
print(hash_table)
'''
