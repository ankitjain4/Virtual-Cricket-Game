import sqlite3
mygame=sqlite3.connect('Fantasy.db')
mycur=mygame.cursor()
mycur.execute('''CREATE TABLE Match
                (Player text(20),
                 Scored integer,
                 Faced integer,
                 Fours integer,
                 Sixes integer,
                 Bowled integer,
                 Maiden integer,
                 Given integer,
                 Wickets integer,
                 Catches integer,
                 Stumping integer,
                 Ro integer );''')

mycur.execute('''CREATE TABLE TEAM
              (Name text(20),
              Players text(200),
              Value integer);''')

mycur.execute('''CREATE TABLE Stats
              (Player text(20),
               Matches integer,
               Runs integer,
               Century integer,
               Half_Century integer,
               value integer,
               ctg text(15));''')


mycur.execute("INSERT INTO match VALUES('Kohli',102,98,8,2,0,0,0,0,0,0,1);")
mycur.execute("INSERT INTO match VALUES('Yuvray',12,20,1,0,48,0,36,1,0,0,0);")
mycur.execute("INSERT INTO match VALUES('Rahane',49,75,3,0,0,0,0,0,1,0,0);")
mycur.execute("INSERT INTO match VALUES('Dhawan',32,35,4,0,0,0,0,0,0,0,0);")
mycur.execute("INSERT INTO match VALUES('Dhoni',56,45,3,1,0,0,0,0,3,2,0);")
mycur.execute("INSERT INTO match VALUES('Axar',8,4,2,0,48,2,35,1,0,0,0);")
mycur.execute("INSERT INTO match VALUES('Pandya',42,35,3,3,30,0,25,0,1,0,0);")
mycur.execute("INSERT INTO match VALUES('Jadeja',18,10,1,1,60,3,50,2,1,0,1);")
mycur.execute("INSERT INTO match VALUES('Kedar',65,60,7,0,24,0,24,0,0,0,0);")
mycur.execute("INSERT INTO match VALUES('Ashwin',23,42,3,0,60,2,45,6,0,0,0);")
mycur.execute("INSERT INTO match VALUES('Umesh',0,0,0,0,54,0,50,4,1,0,0);")
mycur.execute("INSERT INTO match VALUES('Bumrah',0,0,0,0,60,2,49,1,0,0,0);")
mycur.execute("INSERT INTO match VALUES('Bhuwaneshwar',15,12,2,0,60,1,46,2,0,0,0);")
mycur.execute("INSERT INTO match VALUES('Rohit',45,65,5,1,0,0,0,0,1,0,0);")
mycur.execute("INSERT INTO match VALUES('Kartick',29,42,3,0,0,0,0,0,2,0,1);")

mycur.execute("INSERT INTO stats VALUES('Virat',189,8257,28,43,120,'BAT');")
mycur.execute("INSERT INTO stats VALUES('Yuvraj',86,3589,10,21,100,'BAT');")
mycur.execute("INSERT INTO stats VALUES('Rahane',158,5346,11,31,100,'BAT');")
mycur.execute("INSERT INTO stats VALUES('Dhawan',25,565,2,1,85,'AR');")
mycur.execute("INSERT INTO stats VALUES('Dhoni',78,2573,3,19,75,'WK');")
mycur.execute("INSERT INTO stats VALUES('Axar',67,206,0,0,100,'BWL');")
mycur.execute("INSERT INTO stats VALUES('Pandya',70,77,0,0,75,'BWL');")
mycur.execute("INSERT INTO stats VALUES('Jadeja',16,1,0,0,85,'BWL');")
mycur.execute("INSERT INTO stats VALUES('Kedar',111,675,0,1,90,'BWL');")
mycur.execute("INSERT INTO stats VALUES('Ashwin',136,1914,0,10,100,'AR');")
mycur.execute("INSERT INTO stats VALUES('Umesh',296,9496,10,64,110,'BWL');")
mycur.execute("INSERT INTO stats VALUES('Bumrah',73,1365,0,8,60,'BWL');")
mycur.execute("INSERT INTO stats VALUES('Bhuwaneshwar',17,289,0,2,75,'AR');")
mycur.execute("INSERT INTO stats VALUES('Rohit',304,8701,14,52,85,'BAT');")
mycur.execute("INSERT INTO stats VALUES('Kartick',11,111,0,0,75,'WK');")


