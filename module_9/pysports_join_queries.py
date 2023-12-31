import mysql.connector
from mysql.connector import errorcode
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host":"127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
db=mysql.connector.connect(**config)
print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

#inner join query
#connect player and team via team_id
#display the results

try:
    db = mysql.connector.connect(**config) 
    cursor = db.cursor()
    #inner join query
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()
    print ("\n\n-- DISPLAYING PLAYER RECORDS --")

    #print newly updated player table
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))
    input("Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)

finally:
   #close existing database connection
    db.close()