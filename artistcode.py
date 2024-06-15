#Imports necessary modules to effectively code the project
import sqlite3
import os
import time

#Connects VSCode to the database and welcomes the user
conn = sqlite3.connect('artists.db')
cursor = conn.cursor()
os.system("clear")
print("Welcome to the Musical Artist Database")
time.sleep(3)



#Allows the user to get all artists and orders them from their placement on the top 15 of most monthly listeners.
#Also asks the user if they want it in ascending or descending order. There are length checks to ensure the formatting is clean.
#.strip() and .lower() used for convenience and gives the user "Invalid choice" message as a fail safe if they enter something wrong.
def get_artists_by_placement():
  order = input("a or d? (Ascending or Descending)\n\n> ").lower().strip()
  if order == "a":
    os.system("clear")
    cursor.execute('SELECT * FROM Artists;')
  elif order == "d":
    os.system("clear")
    cursor.execute('SELECT * FROM Artists ORDER BY ID DESC;')
  else:
    os.system("clear")
    print("Invalid choice")
    time.sleep(2)
    os.system("clear")
    return

  get_artists_by_placement = cursor.fetchall()

  print("\nAll information has been updated as of Auguest 31st 2023\n")
  print("|Artist\t\t|Gender\t\t|Home Country\t|Curr. Placement|Peak Placement\t|Curr. Listeners|Peak Listeners\t|Studio Albums  |\n|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|")
  for get_artists_by_placement in get_artists_by_placement:
    if len(get_artists_by_placement[1]) < 8:
        if len(get_artists_by_placement[6]) < 7:
            print(f"|{get_artists_by_placement[1]}   \t|{get_artists_by_placement[7]}\t\t|{get_artists_by_placement[6]}\t\t|#{get_artists_by_placement[0]}\t\t|#{get_artists_by_placement[3]}\t\t|{get_artists_by_placement[2]}\t|{get_artists_by_placement[4]}\t|{get_artists_by_placement[5]}\t        |")
        else:
           print(f"|{get_artists_by_placement[1]}   \t|{get_artists_by_placement[7]}\t\t|{get_artists_by_placement[6]}\t|#{get_artists_by_placement[0]}\t\t|#{get_artists_by_placement[3]}\t\t|{get_artists_by_placement[2]}\t|{get_artists_by_placement[4]}\t|{get_artists_by_placement[5]}\t        |")
    else:
       if len(get_artists_by_placement[6]) < 7:
            print(f"|{get_artists_by_placement[1]}\t|{get_artists_by_placement[7]}\t\t|{get_artists_by_placement[6]}\t\t|#{get_artists_by_placement[0]}\t\t|#{get_artists_by_placement[3]}\t\t|{get_artists_by_placement[2]}\t|{get_artists_by_placement[4]}\t|{get_artists_by_placement[5]}\t        |")
       else:
           print(f"|{get_artists_by_placement[1]}\t|{get_artists_by_placement[7]}\t\t|{get_artists_by_placement[6]}\t|#{get_artists_by_placement[0]}\t\t|#{get_artists_by_placement[3]}\t\t|{get_artists_by_placement[2]}\t|{get_artists_by_placement[4]}\t|{get_artists_by_placement[5]}\t        |")



#Allows the user to get all artists and orders them from their placement on the top 15 of the highest peak monthly listeners.
#Also asks the user if they want it in ascending or descending order. There are length checks to ensure the formatting is clean.
#.strip() and .lower() used for convenience and gives the user "Invalid choice" message as a fail safe if they enter something wrong.
def get_artists_by_peak_listeners():
  order = input("a or d? (Ascending or Descending)\n\n> ").lower().strip()
  if order == "a":
    os.system("clear")
    query = "SELECT * FROM Artists ORDER BY PeakListeners;"
  elif order == "d":
    os.system("clear")
    query = "SELECT * FROM Artists ORDER BY PeakListeners DESC;"
  else:
    os.system("clear")
    print("Invalid choice")
    time.sleep(2)
    os.system("clear")
    return

  cursor.execute(query)

  get_artists_by_peak_listeners = cursor.fetchall()

  print("\nAll information has been updated as of Auguest 31st 2023\n")
  print("|Artist\t\t|Gender\t\t|Home Country\t|Curr. Placement|Peak Placement\t|Curr. Listeners|Peak Listeners\t|Studio Albums  |\n|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|")
  for get_artists_by_peak_listeners in get_artists_by_peak_listeners:
     if len(get_artists_by_peak_listeners[1]) < 8:
        if len(get_artists_by_peak_listeners[6]) < 7:
            print(f"|{get_artists_by_peak_listeners[1]}   \t|{get_artists_by_peak_listeners[7]}\t\t|{get_artists_by_peak_listeners[6]}\t\t|#{get_artists_by_peak_listeners[0]}\t\t|#{get_artists_by_peak_listeners[3]}\t\t|{get_artists_by_peak_listeners[2]}\t|{get_artists_by_peak_listeners[4]}\t|{get_artists_by_peak_listeners[5]}\t        |")
        else:
           print(f"|{get_artists_by_peak_listeners[1]}   \t|{get_artists_by_peak_listeners[7]}\t\t|{get_artists_by_peak_listeners[6]}\t|#{get_artists_by_peak_listeners[0]}\t\t|#{get_artists_by_peak_listeners[3]}\t\t|{get_artists_by_peak_listeners[2]}\t|{get_artists_by_peak_listeners[4]}\t|{get_artists_by_peak_listeners[5]}\t        |")
     else:
        if len(get_artists_by_peak_listeners[6]) < 7:
            print(f"|{get_artists_by_peak_listeners[1]}\t|{get_artists_by_peak_listeners[7]}\t\t|{get_artists_by_peak_listeners[6]}\t\t|#{get_artists_by_peak_listeners[0]}\t\t|#{get_artists_by_peak_listeners[3]}\t\t|{get_artists_by_peak_listeners[2]}\t|{get_artists_by_peak_listeners[4]}\t|{get_artists_by_peak_listeners[5]}\t        |")
        else:
           print(f"|{get_artists_by_peak_listeners[1]}\t|{get_artists_by_peak_listeners[7]}\t\t|{get_artists_by_peak_listeners[6]}\t|#{get_artists_by_peak_listeners[0]}\t\t|#{get_artists_by_peak_listeners[3]}\t\t|{get_artists_by_peak_listeners[2]}\t|{get_artists_by_peak_listeners[4]}\t|{get_artists_by_peak_listeners[5]}\t        |")



#Allows the user to get all artists and orders them from the amount of studio albums they have released.
#Also asks the user if they want it in ascending or descending order. There are length checks to ensure the formatting is clean.
#.strip() and .lower() used for convenience and gives the user "Invalid choice" message as a fail safe if they enter something wrong.
def get_artists_by_albums():
  order = input("a or d? (Ascending or Descending)\n\n> ").lower().strip()
  if order == "a":
    os.system("clear")
    query = "SELECT * FROM Artists ORDER BY StudioAlbums;"
  elif order == "d":
    os.system("clear")
    query = "SELECT * FROM Artists ORDER BY StudioAlbums DESC;"
  else:
    os.system("clear")
    print("Invalid choice")
    time.sleep(2)
    os.system("clear")
    return

  cursor.execute(query)

  get_artists_by_albums = cursor.fetchall()

  print("\nAll information has been updated as of Auguest 31st 2023\n")
  print("|Artist\t\t|Gender\t\t|Home Country\t|Curr. Placement|Peak Placement\t|Curr. Listeners|Peak Listeners\t|Studio Albums  |\n|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|")
  for get_artists_by_albums in get_artists_by_albums:
     if len(get_artists_by_albums[1]) < 8:
        if len(get_artists_by_albums[6]) < 7:
            print(f"|{get_artists_by_albums[1]}   \t|{get_artists_by_albums[7]}\t\t|{get_artists_by_albums[6]}\t\t|#{get_artists_by_albums[0]}\t\t|#{get_artists_by_albums[3]}\t\t|{get_artists_by_albums[2]}\t|{get_artists_by_albums[4]}\t|{get_artists_by_albums[5]}\t        |")
        else:
           print(f"|{get_artists_by_albums[1]}   \t|{get_artists_by_albums[7]}\t\t|{get_artists_by_albums[6]}\t|#{get_artists_by_albums[0]}\t\t|#{get_artists_by_albums[3]}\t\t|{get_artists_by_albums[2]}\t|{get_artists_by_albums[4]}\t|{get_artists_by_albums[5]}\t        |")
     else:
        if len(get_artists_by_albums[6]) < 7:
            print(f"|{get_artists_by_albums[1]}\t|{get_artists_by_albums[7]}\t\t|{get_artists_by_albums[6]}\t\t|#{get_artists_by_albums[0]}\t\t|#{get_artists_by_albums[3]}\t\t|{get_artists_by_albums[2]}\t|{get_artists_by_albums[4]}\t|{get_artists_by_albums[5]}\t        |")
        else:
           print(f"|{get_artists_by_albums[1]}\t|{get_artists_by_albums[7]}\t\t|{get_artists_by_albums[6]}\t|#{get_artists_by_albums[0]}\t\t|#{get_artists_by_albums[3]}\t\t|{get_artists_by_albums[2]}\t|{get_artists_by_albums[4]}\t|{get_artists_by_albums[5]}\t        |")



#Allows the user to get all artists and orders them from the alphabetical order of their names. 
#Also asks the user if they want it in ascending or descending order. There are length checks to ensure the formatting is clean.
#.strip() and .lower() used for convenience and gives the user "Invalid choice" message as a fail safe if they enter something wrong.
def get_artists_by_alphabetical_order():
  order = input("a or d? (Ascending or Descending)\n\n> ").lower().strip()
  if order == "a":
    os.system("clear")
    query = "SELECT * FROM Artists ORDER BY Name;"
  elif order == "d":
    os.system("clear")
    query = "SELECT * FROM Artists ORDER BY Name DESC;"
  else:
    os.system("clear")
    print("Invalid choice")
    time.sleep(2)
    os.system("clear")
    return

  cursor.execute(query)

  get_artists_by_alphabetical_order = cursor.fetchall()

  print("\nAll information has been updated as of Auguest 31st 2023\n")
  print("|Artist\t\t|Gender\t\t|Home Country\t|Curr. Placement|Peak Placement\t|Curr. Listeners|Peak Listeners\t|Studio Albums  |\n|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|")
  for get_artists_by_alphabetical_order in get_artists_by_alphabetical_order:
     if len(get_artists_by_alphabetical_order[1]) < 8:
        if len(get_artists_by_alphabetical_order[6]) < 7:
            print(f"|{get_artists_by_alphabetical_order[1]}   \t|{get_artists_by_alphabetical_order[7]}\t\t|{get_artists_by_alphabetical_order[6]}\t\t|#{get_artists_by_alphabetical_order[0]}\t\t|#{get_artists_by_alphabetical_order[3]}\t\t|{get_artists_by_alphabetical_order[2]}\t|{get_artists_by_alphabetical_order[4]}\t|{get_artists_by_alphabetical_order[5]}\t        |")
        else:
           print(f"|{get_artists_by_alphabetical_order[1]}   \t|{get_artists_by_alphabetical_order[7]}\t\t|{get_artists_by_alphabetical_order[6]}\t|#{get_artists_by_alphabetical_order[0]}\t\t|#{get_artists_by_alphabetical_order[3]}\t\t|{get_artists_by_alphabetical_order[2]}\t|{get_artists_by_alphabetical_order[4]}\t|{get_artists_by_alphabetical_order[5]}\t        |")
     else:
        if len(get_artists_by_alphabetical_order[6]) < 7:
            print(f"|{get_artists_by_alphabetical_order[1]}\t|{get_artists_by_alphabetical_order[7]}\t\t|{get_artists_by_alphabetical_order[6]}\t\t|#{get_artists_by_alphabetical_order[0]}\t\t|#{get_artists_by_alphabetical_order[3]}\t\t|{get_artists_by_alphabetical_order[2]}\t|{get_artists_by_alphabetical_order[4]}\t|{get_artists_by_alphabetical_order[5]}\t        |")
        else:
           print(f"|{get_artists_by_alphabetical_order[1]}\t|{get_artists_by_alphabetical_order[7]}\t\t|{get_artists_by_alphabetical_order[6]}\t|#{get_artists_by_alphabetical_order[0]}\t\t|#{get_artists_by_alphabetical_order[3]}\t\t|{get_artists_by_alphabetical_order[2]}\t|{get_artists_by_alphabetical_order[4]}\t|{get_artists_by_alphabetical_order[5]}\t        |")



#Allows the user to get the average amount of either current monthly listeners, peak monthly listeners, or amount of albums released.
#After calculating the average across all 15 artists, it gives the user a statement with the results.
#.strip() used for convenience and gives the user "Invalid choice" message as a fail safe if they enter something wrong.
def get_averages_of_statistics():
   statistic = input("1. Average of current listeners\n2. Average of peak listeners\n3. Average of albums released\n\n> ").strip()
   if statistic == "1":
    os.system("clear")
    time.sleep(0.5)
    query = "SELECT ROUND(AVG(MonthlyListeners)) FROM Artists;"
    cursor.execute(query)
    get_averages_of_statistics = cursor.fetchall()
    print(f"The average monthly listeners across all 15 artists as of August 2023 is " + str(int(get_averages_of_statistics[0][0])) + ".")
   elif statistic == "2":
    os.system("clear")
    time.sleep(0.5)
    query = "SELECT ROUND(AVG(PeakListeners)) FROM Artists;"
    cursor.execute(query)
    get_averages_of_statistics = cursor.fetchall()
    print(f"The average of the peak monthly listeners across all 15 artists as of August 2023 is " + str(int(get_averages_of_statistics[0][0])) + ".")
   elif statistic == "3":
    os.system("clear")
    time.sleep(0.5)
    query = "SELECT ROUND(AVG(StudioAlbums)) FROM Artists;"
    cursor.execute(query)
    get_averages_of_statistics = cursor.fetchall()
    print(f"The average of studio albums released across all 15 artists as of August 2023 is " + str(int(get_averages_of_statistics[0][0])) + ".")
   else:
    os.system("clear")
    print("Invalid choice")
    time.sleep(2)
    os.system("clear")



#Allows the user to delete an artist from the database. This is useful to create custom data tables such as only females or only artists from the United Kingdom.
#Getting rid of artists using this function also changes the outcome of the averages function.
#Has a fail safe to ensure the user does not break the program.
def delete_artist():
   while True:
      get_artists_by_placement()
      try:
         option = int(input("\nEnter the current placement of the artist you want to delete\n\n> "))
         option = str(option)
         query = "SELECT * FROM Artists WHERE ID = " + option + ";"
         cursor.execute(query)
         delete_artist = cursor.fetchall()
         if len(delete_artist) > 0:
            break
         else:
            os.system("clear")
            print("Invalid choice")
            time.sleep(2)
            os.system("clear")
      except:
            os.system("clear")
            print("Invalid choice")
            time.sleep(2)
            os.system("clear")
   cursor.execute("DELETE FROM Artists WHERE ID = " + option + ";")
   print("Succesfully removed artist.")



#Ensures the user is immediately asked what they want to do at the start of the program and after each function is complete.
#Gives clear options of what the user can do and also gives them the choice to stop the program. 
while True:
  choice = input("\n1. Get artists by current placement\n2. Get artists by peak listeners\n3. Get artists by albums released\n4. Get artists by alphabetical order\n5. Get averages of statistics\n6. Delete an artist\n7. Exit\n\n> ").strip()
  if choice == "1":
    os.system("clear")
    time.sleep(0.5)
    get_artists_by_placement()
  elif choice == "2":
    os.system("clear")
    time.sleep(0.5)
    get_artists_by_peak_listeners()
  elif choice == "3":
    os.system("clear")
    time.sleep(0.5)
    get_artists_by_albums()
  elif choice == "4":
    os.system("clear")
    time.sleep(0.5)
    get_artists_by_alphabetical_order()
  elif choice == "5":
    os.system("clear")
    time.sleep(0.5)
    get_averages_of_statistics()
  elif choice == "6":
    os.system("clear")
    time.sleep(0.5)
    delete_artist()
  elif choice == "7":
    break
  else:
    os.system("clear")
    print("Invalid choice")
    time.sleep(2)
    os.system("clear")

#Closes the program when the user chooses to exit the program. Rollback ensures the data the user deleted from the database is restored for next time.
conn.rollback()
conn.commit()
conn.close()

