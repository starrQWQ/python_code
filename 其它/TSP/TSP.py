from City import City
from random import shuffle,random,randint
from Individual import Individual
import matplotlib.pyplot as plt

def loadfile(filename):
    # read the file
    cities = []
    try:
        fp = open(filename,"r")
        for line in fp.readlines():
            line = line.strip('\n').split(',',2);
            line[1] = float(line[1])
            line[2] = float(line[2])
            cities.append(City(line[0],line[1],line[2]))
    except FileNotFoundError as e:
        print(e)
    finally:
        fp.close()
    
    return cities


def init_group(number_of_city):
    # 100 indivdual / group
    group = []
    
    city_seq = []
    for i in range(number_of_city):
        city_seq.append(i)
    
    i = 0
    while(i < number_of_indiv):
        shuffle(city_seq)
        for added_individual in group:
            if added_individual.get_seq()  == city_seq:
                continue
        group.append(Individual(city_seq,cities))
        i += 1
    return group




def choose(group):
    
    # dictionary  
    # probability:[individual,times to be chosen]
    d = {}
    
    # roulette wheel
    sum_p = 0
    pos = 0
    selected = []
    
    for individual in group:
        sum_p += individual.get_fit()
        
    for individual in group:
        p = individual.fit / sum_p
        individual.setP(p)
        pos += p
        d[pos] = [individual,0]
    
    positions = []  
    for k in d.keys():
        positions.append(k)
    positions.sort();
    
    # begin the wheel
    for i in range(number_of_indiv):
        pointer = random()  # the pointer
        for i in range(len(positions)):
            if positions[i] >= pointer:
                break
        d[positions[i-1]][1] += 1   # individual d[l[i-1]][0] was selected
        

    for (individual,chosentimes) in d.values():
        if chosentimes > 0:
            for i in range(chosentimes):
                selected.append(Individual(individual.get_seq(),cities,individual.get_fit()))
    return selected


def cross(selected):
    
    shuffle(selected)
    
    for i in range(0 , int(number_of_indiv * pc) // 2 , 2):
        (ind1,ind2) = selected[i:i+2]
        
        cities1 = ind1.get_seq()
        cities2 = ind2.get_seq()
        
        r = randint(1,number_of_city-2)
        tmp = cities1[r:]
        cities1[r:] = cities2[r:]
        cities2[r:] = tmp
    
        for city1 in cities1[:r]:
            try:
                index_city1 = cities1[r:].index(city1)
                tmp = cities1[index_city1]
                cities1[index_city1] = cities2[index_city1]
                cities2[index_city1] = tmp
            except:
                continue
            
def mut(new_group):
    n = int(number_of_indiv * pm)
    if n < 1:
        return
    while(n):
        r1 = randint(0,number_of_indiv - 1)
        r2 = randint(0,number_of_city - 1)
        r3 = randint(0,number_of_city - 1)
        
        city_seq = new_group[r1].get_seq().copy()
        tmp = city_seq[r2]
        city_seq[r2] = city_seq[r3]
        city_seq[r3] = tmp
        
        new_indiv = Individual(city_seq,cities)
        if new_indiv.get_fit() > new_group[r1].get_fit():
            del(new_group[r1])
            new_group.append(new_indiv)
            n -= 1
            
        
        
def search_bestroute(group):
    global bestroute
    
    for indiv in group:
        fit = indiv.get_fit()
        if fit > bestroute[1]:
            bestroute[0] = indiv.get_seq().copy()
            bestroute[1] = fit
            bestroute[2] = indiv.get_dis()
    


if __name__ == "__main__":
    global cities
    global number_of_indiv
    global pc
    global pm
    global bestroute
    
    cities = loadfile("data.txt")
    number_of_indiv = 100
    pc = 0.01
    pm = 0.1
    
    number_of_city = len(cities)
    #   number_of_city : number of cities
    
#    for i in range(number_of_city):
#        print(cities[i].name,end=',')
#    print()
    
    
    
    group = init_group(number_of_city);
#    for individual in group:
#        for i in individual.get_seq():
#            print(cities[i].name,end=',')
#        print('\n')
    
    bestroute = [[],0,0]    #[route,fit,distance]
    search_bestroute(group)
    times = int(input("how many generations?:"))
    new_group = group
    while(times):
        tmp = new_group
        new_group = choose(new_group)
    #    for indiv in new_group:
    #        print(indiv.get_seq())
    #    print(len(new_group))
        
        cross(new_group)
    
        mut(new_group)
        
        search_bestroute(new_group)
        
        del(tmp)
        times -= 1
        
    plt.xlim(90,130)
    plt.ylim(20,50)
    x = []
    y = []
    
    for i in bestroute[0]:
#        print(cities[i].name,end = ',')
#        print()
#        print("distance:",bestroute[2])
        x.append(cities[i].lon)
        y.append(cities[i].lat)
        
        
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus']=False
        plt.text(cities[i].lon,cities[i].lat,cities[i].name)
    plt.plot(x,y,'go-')
    plt.text(120,23,str(bestroute[2]) + 'km')
    


