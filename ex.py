shifr = list('ГШЫОЭЦМЪЩАВТХЯЬФУКЮРПСЗЖЛЁНДЕБЧИЙ')
alf = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
print(list(alf))
print(list(shifr))
secret = 'ГОД'
secret_list = list(secret)
secret_idx = []
unsecret = []
count = 0
while secret_list != unsecret:
    for v in secret:
        secret_idx.append(alf.index(v))

    for v in secret_idx:
        unsecret.append(shifr[v])
    count += 1
    secret_list = unsecret
    unsecret = []
print(count)