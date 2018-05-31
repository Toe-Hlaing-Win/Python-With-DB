from multiprocessing import Pool, TimeoutError
import time
import os
import string
import random
import psycopg2

allchar = string.ascii_letters
allnum = string.digits



def f(x):
    print "process %s run " % x
    print x * 100000 , '==>' , ( x + 1 ) * 100000
    i = x * 100000 
    j = ( x + 1 ) * 100000
    con  = psycopg2.connect("host='localhost' dbname='testdb' user='postgres' password='  22'")
    cur = con.cursor()
    print "c0nn g00d"
    while i < j:
        name = "".join(random.choice(allchar) for x in range(16))
        items = ['Yankin', 'South Okkalapa', 'South Dagon', 'North Dagon', 'North Okkalapa', 'Tarmwe']
        place = random.choice(items)
        or_price = random.randint(100,1100)
        s_price = or_price + 200
        cur.execute("INSERT INTO products(Id, name, place, original_price,sell_price ) VALUES(%s,%s,%s,%s,%s )", (i , name, place, or_price, s_price))
        i = i + 1
    con.commit()


if __name__ == '__main__':
    pool = Pool(processes=10)


    pool.map(f, [0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15 ,16 ,17 ,18 ,19 ,20 ,21 ,22 ,23 ,24 ,25 ,26 ,27 ,28 ,29 ,30 ,31 ,32 ,33 ,34 ,35 ,36 ,37 ,38 ,39 ,40 ,41 ,42 ,43 ,44 ,45 ,46 ,47 ,48 ,49 ,50 ,51 ,52 ,53 ,54 ,55 ,56 ,57 ,58 ,59 ,60,61 ,62 ,63 ,64 ,65 ,66 ,67 ,68 ,69 ,70 ,71 ,72 ,73 ,74 ,75 ,76 ,77 ,78 ,79 ,80 ,81 ,82 ,83 ,84 ,85 ,86 ,87 ,88 ,89 ,90 ,91 ,92 ,93 ,94 ,95 ,96 ,97 ,98 ,99 ])


