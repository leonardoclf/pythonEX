# def find(word, letter, start):
#     index = start
#     while index < len(word) - start:
#         if word[index - start] == letter:
#             return index
#         index = index + 1
#     return "not found"
#
#
# find("hello", "e", 1)


# fin = open("words.txt")
#
# for line in fin:
#     if len(line) > 20:
#         word = line.strip()
#         print(word)
#
# def has_no_e(strg):
#     count = 0
#     for l in strg:
#         if l == "e":
#             count = count + 1
#     if count == 0:
#         return True
# else:
#     return False


# fin = open("words.txt")
#
# withE = 0
# without = 0
# for line in fin:
#     if has_no_e(line):
#         withE += 1
#         print(line)
#     else:
#         without += 1
#
# Totalperc = (withE * 100) / (withE + without)
#
# print("\nTotal with E: " + str(withE))
# print("Total without E: " + str(without))
# print("Total % with letter E: " + str(round(Totalperc)) + "%")


# def avoid(word, forbidden):
#     count = 0
#     for letter in word:
#         if letter in forbidden:
#             count += 1
#     return count == 0
#
#
# fin = open("words.txt")
# askForbidden = input("Enter a string that you don't want to see: ")
#
# countA = 0
# for line in fin:
#     if avoid(line, askForbidden):
#         countA += 1
#         print(line)
# print(countA)


# def use_only(word, allow):
#     listallow = []
#     for letter in word:
#         if letter in allow:
#             listallow.append(letter)
#     a = ''.join(listallow)
#     return a == allow
#
# fin = open("words.txt")
# allowWord = input("Enter a string that you desire to see: ")
#
# countP = 0
# for line in fin:
#     if use_only(line, allowWord):
#         print(line)
#         countP += 1
# print(countP)

# t = ["d", "e", "f", "b", "a", "c"]
#
# t.sort()
#
# print(t)


# Exemplo de variavel acumuladora
# def add_all(t):
#     total = 0
#     for x in t:
#         total += x
#     return total(

# nested_sum = [[1, 2], [3], [4, 5, 6]]


# def nested_sum(lista):
#     total = 0
#     for t in lista:
#         total += sum(t)
#     return total
#
#
# print(nested_sum(
#     [[1, 2], [3], [4, 5, 6]]
# ))


# t = [1, 2, 3, 4]


# def middle(lista):
#     del lista[0]
#     del lista[len(lista) - 1]
#     return lista
#
#
# print(middle(
#     [1, 2, 3, 4]
# ))


# strg = "abcdefghi"
#
# lista = []
#
# # lista.append(strg[0:2])
# #
# # lista.append(strg[1:3])
# #
# # lista.append(strg[2:4])
# #
# # lista.append(strg[3:5])
#
# z = (len(strg))
# y = range(int(len(strg) / 2))
#
# for i in y:
#     lista.append(strg[i * 2: 2 + (i * 2)])
#
# print(lista)


# def solution(s):
#     lista = []
#     if len(s) % 2 != 0:
#
#     y = range(int(len(s) / 2))
#     print(s)
#     for i in y:
#         lista.append(s[i * 2 : 2 + (i * 2)])
#
#     return lista
#
# print(solution("asdfads"))


# def histogram(s):
#     d = dict()
#     for c in s:
#         print(d.get(c,0))
#         d[c] = 1 + d.get(c, 0)
#     return d


# def find_screen_height(width, ratio):
#     x = ratio.split(":")[0]
#     y = ratio.split(":")[1]
#     height = (int(y) * width) // int(x)
#     return "{}x{}".format(width, height)
#
#
# print(find_screen_height(1024, "4:3"))

# sizes = [4, 4, 4, 3, 3, 10, 20,30]
# hd = 12
# counter = []
# for i in range(len(sizes)):
#     counter.append(sizes[i])
#     if sum(counter) > hd:
#         counter.remove(sizes[i])
#
# print(len(counter))


# def save(sizes, hd):
#     check_size = []
#     for i in range(len(sizes)):
#         check_size.append(sizes[i])
#         if sum(check_size) > hd:
#             check_size.remove(sizes[i])
#             break
#     print(hd)
#     print(check_size)
#     return len(check_size)
#
# print(save([4,4,4,3,3],11))

lista = [4, 1, 2, 3]

lista.sort()
diferenca = []
for i in lista:
    if i + 2 in lista:
        diferenca.append([i, i + 2])

print(diferenca)