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
print("Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
try:
    db = mysql.connector.connect(**config)
    cursor=db.cursor()
    #establish variables for insert query
    sql = "INSERT INTO player(first_name, last_name, player_id, team_id) values(%s, %s, %s, %s)"
    val = ("Smeagol", "Shire Folk", "21", "1")
    #run and commit insert to database
    cursor.execute(sql, val)
    db.commit()

    #inner join query
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()
    print ("\n\n-- DISPLAYING PLAYERS AFTER INSERT --")

    #print table with newly inserted record
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))
    
    print("\n\n-- DISPLAYING PLAYERS AFTER UPDATE --")

    #establish variables for update query
    update = ("UPDATE player SET team_id=2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    #run and commit record update to database
    cursor.execute(update)
    db.commit()
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()

    #print table with newly updated record
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))
    
    #delete query
    delete = ("DELETE from PLAYER WHERE first_name='Gollum'")
    #run and commit delete to database
    cursor.execute(delete)
    db.commit()
    
    #display player table with deleted record
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()
    print ("\n\n-- DISPLAYING PLAYERS AFTER DELETE --")

    #print table with newly inserted record
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))

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