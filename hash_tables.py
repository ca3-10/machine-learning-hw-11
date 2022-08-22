class HashTable: 
    def __init__(self, num_of_buckets):
        self.num_of_buckets = num_of_buckets
        self.buckets = [[] for i in range(num_of_buckets)]
    
    def hash(self,string):
        alphabet = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5,
                    "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
                    "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17,
                    "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23,
                    "y": 24, "z": 25}
        list_of_letters = list(string)
        sum = 0
        for letters in string:
            sum += alphabet[letters]
        return sum % self.num_of_buckets

    def insert(self,key,value):
            bucket_index = self.hash(key)
            self.buckets[bucket_index].append((key,value))

    def find(self,key):
            bucket_index = self.hash(key)
            for bucket in self.buckets[bucket_index]:
                if bucket[0] == key:
                    return bucket[1]


ht = HashTable(3)
ht.buckets
[[], [], []]
assert (ht.hash('cabbage')) == 2

ht.insert('cabbage', 5)
assert(ht.buckets) == [[],[],[('cabbage', 5)]]

ht.insert('cab', 20)
assert(ht.buckets) == [[('cab',    20)],[],[('cabbage', 5)]
]

ht.insert('c', 17)
assert ht.buckets == [[('cab',    20)],[],[('cabbage', 5), ('c', 17)]]

ht.insert('ac', 21)
assert ht.buckets == [[('cab',    20)],[],[('cabbage', 5), ('c', 17), ('ac', 21)]]

assert ht.find('cabbage') == 5

assert ht.find('cab') == 20

assert ht.find('c') == 17
17
assert ht.find('ac') == 21