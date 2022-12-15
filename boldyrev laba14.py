A="hkfkhgfkghf" #строка для которой выводится хеш таблица

# функция, на вход которой подается пустая хеш таблица, ключ и элемент, для заполлнения хеш таблицы
def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table) 
    key_exists = False
    bucket = hash_table[hash_key]   
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True 
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))


hash_table=[[] for _ in range(len(A))] #создает хеш таблицу в виде массива и подмассивов в нем
for i in range(len(A)):
    insert(hash_table, i, A[i])

print (hash_table) #выводит хеш таблицу в консоль