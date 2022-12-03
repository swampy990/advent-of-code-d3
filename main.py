data = []
group = []
N=0

def alphabet_position(text):

    dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11',
    'l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21',
    'v':'22','w':'23','x':'24','y':'25','z':'26','A':'27','B':'28','C':'29','D':'30','E':'31','F':'32',
    'G':'33','H':'34','I':'35','J':'36','K':'37','L':'38','M':'39','N':'40','O':'41','P':'42','Q':'43',
    'R':'44','S':'45','T':'46','U':'47','V':'48','W':'49','X':'50','Y':'51','Z':'52'
    }
    #text = text.lower()
    for i in text:
        if i in dict:
            new_text = text.replace(i, dict[i])
    return new_text

# Get all the lines
for line in open("rucksack.txt", "r"):
    # calculate the length and halve it
    s = int(len(line.strip())/2)

    search_set1 = set(line[0:s])
    search_set2 = set(line[s:])

    for element01 in search_set1:
        for element02 in search_set2:
            if element01 == element02:
                data.append(int(alphabet_position(element01)))

print(sum(data))

for line in open("rucksack.txt", "r"):


    if N == 0:
        badge_set0 = set(line.strip())

    if N == 1:
        badge_set1 = set(line.strip())

    if N == 2:
        badge_set2 = set(line.strip())

    N = N + 1
    if N == 3:
        N = 0
        test = badge_set0.intersection(badge_set1)
        result = test.intersection(badge_set2)
        group.append(int(alphabet_position(str(''.join(result)))))

print(sum(group))












