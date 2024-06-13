import sqlite3
import os
import time

conn = sqlite3.connect('artists.db')

cursor = conn.cursor()

os.system("clear")

print("Welcome to the Musical Artist Database")
time.sleep(3)
os.system("clear")

def get_artists_by_placement():
  order = input("a or d? (Ascending or Descending)\n\n>").lower().strip()
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
  print("|Artist\t\t|Gender\t\t|Home Country\t|Curr. Placement|Peak Placement\t|Mth. Listeners\t|Peak Listeners\t|Studio Albums|\n|---------------|---------------|---------------|---------------|---------------|---------------|---------------|-------------|")
  for get_artists_by_placement in get_artists_by_placement:
    if len(get_artists_by_placement[1]) < 8:
        if len(get_artists_by_placement[6]) < 7:
            print(f"|{get_artists_by_placement[1]}   \t|{get_artists_by_placement[7]}\t\t|{get_artists_by_placement[6]}\t\t|#{get_artists_by_placement[0]}\t\t|#{get_artists_by_placement[3]}\t\t|{get_artists_by_placement[2]}\t|{get_artists_by_placement[4]}\t|{get_artists_by_placement[5]}\t      |")
        else:
           print(f"|{get_artists_by_placement[1]}   \t|{get_artists_by_placement[7]}\t\t|{get_artists_by_placement[6]}\t|#{get_artists_by_placement[0]}\t\t|#{get_artists_by_placement[3]}\t\t|{get_artists_by_placement[2]}\t|{get_artists_by_placement[4]}\t|{get_artists_by_placement[5]}\t      |")
    else:
       if len(get_artists_by_placement[6]) < 7:
            print(f"|{get_artists_by_placement[1]}\t|{get_artists_by_placement[7]}\t\t|{get_artists_by_placement[6]}\t\t|#{get_artists_by_placement[0]}\t\t|#{get_artists_by_placement[3]}\t\t|{get_artists_by_placement[2]}\t|{get_artists_by_placement[4]}\t|{get_artists_by_placement[5]}\t      |")
       else:
           print(f"|{get_artists_by_placement[1]}\t|{get_artists_by_placement[7]}\t\t|{get_artists_by_placement[6]}\t|#{get_artists_by_placement[0]}\t\t|#{get_artists_by_placement[3]}\t\t|{get_artists_by_placement[2]}\t|{get_artists_by_placement[4]}\t|{get_artists_by_placement[5]}\t      |")



def get_artists_by_peak_listeners():
  order = input("a or d? (Ascending or Descending)\n\n>").lower().strip()
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
  print("|Artist\t\t|Gender\t\t|Home Country\t|Curr. Placement|Peak Placement\t|Mth. Listeners\t|Peak Listeners\t|Studio Albums|\n|---------------|---------------|---------------|---------------|---------------|---------------|---------------|-------------|")
  for get_artists_by_peak_listeners in get_artists_by_peak_listeners:
     if len(get_artists_by_peak_listeners[1]) < 8:
        if len(get_artists_by_peak_listeners[6]) < 7:
            print(f"|{get_artists_by_peak_listeners[1]}   \t|{get_artists_by_peak_listeners[7]}\t\t|{get_artists_by_peak_listeners[6]}\t\t|#{get_artists_by_peak_listeners[0]}\t\t|#{get_artists_by_peak_listeners[3]}\t\t|{get_artists_by_peak_listeners[2]}\t|{get_artists_by_peak_listeners[4]}\t|{get_artists_by_peak_listeners[5]}\t      |")
        else:
           print(f"|{get_artists_by_peak_listeners[1]}   \t|{get_artists_by_peak_listeners[7]}\t\t|{get_artists_by_peak_listeners[6]}\t|#{get_artists_by_peak_listeners[0]}\t\t|#{get_artists_by_peak_listeners[3]}\t\t|{get_artists_by_peak_listeners[2]}\t|{get_artists_by_peak_listeners[4]}\t|{get_artists_by_peak_listeners[5]}\t      |")
     else:
        if len(get_artists_by_peak_listeners[6]) < 7:
            print(f"|{get_artists_by_peak_listeners[1]}\t|{get_artists_by_peak_listeners[7]}\t\t|{get_artists_by_peak_listeners[6]}\t\t|#{get_artists_by_peak_listeners[0]}\t\t|#{get_artists_by_peak_listeners[3]}\t\t|{get_artists_by_peak_listeners[2]}\t|{get_artists_by_peak_listeners[4]}\t|{get_artists_by_peak_listeners[5]}\t      |")
        else:
           print(f"|{get_artists_by_peak_listeners[1]}\t|{get_artists_by_peak_listeners[7]}\t\t|{get_artists_by_peak_listeners[6]}\t|#{get_artists_by_peak_listeners[0]}\t\t|#{get_artists_by_peak_listeners[3]}\t\t|{get_artists_by_peak_listeners[2]}\t|{get_artists_by_peak_listeners[4]}\t|{get_artists_by_peak_listeners[5]}\t      |")



def get_artists_by_albums():
  order = input("a or d? (Ascending or Descending)\n\n>").lower().strip()
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
  print("|Artist\t\t|Gender\t\t|Home Country\t|Curr. Placement|Peak Placement\t|Mth. Listeners\t|Peak Listeners\t|Studio Albums|\n|---------------|---------------|---------------|---------------|---------------|---------------|---------------|-------------|")
  for get_artists_by_albums in get_artists_by_albums:
     if len(get_artists_by_albums[1]) < 8:
        if len(get_artists_by_albums[6]) < 7:
            print(f"|{get_artists_by_albums[1]}   \t|{get_artists_by_albums[7]}\t\t|{get_artists_by_albums[6]}\t\t|#{get_artists_by_albums[0]}\t\t|#{get_artists_by_albums[3]}\t\t|{get_artists_by_albums[2]}\t|{get_artists_by_albums[4]}\t|{get_artists_by_albums[5]}\t      |")
        else:
           print(f"|{get_artists_by_albums[1]}   \t|{get_artists_by_albums[7]}\t\t|{get_artists_by_albums[6]}\t|#{get_artists_by_albums[0]}\t\t|#{get_artists_by_albums[3]}\t\t|{get_artists_by_albums[2]}\t|{get_artists_by_albums[4]}\t|{get_artists_by_albums[5]}\t      |")
     else:
        if len(get_artists_by_albums[6]) < 7:
            print(f"|{get_artists_by_albums[1]}\t|{get_artists_by_albums[7]}\t\t|{get_artists_by_albums[6]}\t\t|#{get_artists_by_albums[0]}\t\t|#{get_artists_by_albums[3]}\t\t|{get_artists_by_albums[2]}\t|{get_artists_by_albums[4]}\t|{get_artists_by_albums[5]}\t      |")
        else:
           print(f"|{get_artists_by_albums[1]}\t|{get_artists_by_albums[7]}\t\t|{get_artists_by_albums[6]}\t|#{get_artists_by_albums[0]}\t\t|#{get_artists_by_albums[3]}\t\t|{get_artists_by_albums[2]}\t|{get_artists_by_albums[4]}\t|{get_artists_by_albums[5]}\t      |")



def get_artists_by_alphabetical_order():
  order = input("a or d? (Ascending or Descending)\n\n>").lower().strip()
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
  print("|Artist\t\t|Gender\t\t|Home Country\t|Curr. Placement|Peak Placement\t|Mth. Listeners\t|Peak Listeners\t|Studio Albums|\n|---------------|---------------|---------------|---------------|---------------|---------------|---------------|-------------|")
  for get_artists_by_alphabetical_order in get_artists_by_alphabetical_order:
     if len(get_artists_by_alphabetical_order[1]) < 8:
        if len(get_artists_by_alphabetical_order[6]) < 7:
            print(f"|{get_artists_by_alphabetical_order[1]}   \t|{get_artists_by_alphabetical_order[7]}\t\t|{get_artists_by_alphabetical_order[6]}\t\t|#{get_artists_by_alphabetical_order[0]}\t\t|#{get_artists_by_alphabetical_order[3]}\t\t|{get_artists_by_alphabetical_order[2]}\t|{get_artists_by_alphabetical_order[4]}\t|{get_artists_by_alphabetical_order[5]}\t      |")
        else:
           print(f"|{get_artists_by_alphabetical_order[1]}   \t|{get_artists_by_alphabetical_order[7]}\t\t|{get_artists_by_alphabetical_order[6]}\t|#{get_artists_by_alphabetical_order[0]}\t\t|#{get_artists_by_alphabetical_order[3]}\t\t|{get_artists_by_alphabetical_order[2]}\t|{get_artists_by_alphabetical_order[4]}\t|{get_artists_by_alphabetical_order[5]}\t      |")
     else:
        if len(get_artists_by_alphabetical_order[6]) < 7:
            print(f"|{get_artists_by_alphabetical_order[1]}\t|{get_artists_by_alphabetical_order[7]}\t\t|{get_artists_by_alphabetical_order[6]}\t\t|#{get_artists_by_alphabetical_order[0]}\t\t|#{get_artists_by_alphabetical_order[3]}\t\t|{get_artists_by_alphabetical_order[2]}\t|{get_artists_by_alphabetical_order[4]}\t|{get_artists_by_alphabetical_order[5]}\t      |")
        else:
           print(f"|{get_artists_by_alphabetical_order[1]}\t|{get_artists_by_alphabetical_order[7]}\t\t|{get_artists_by_alphabetical_order[6]}\t|#{get_artists_by_alphabetical_order[0]}\t\t|#{get_artists_by_alphabetical_order[3]}\t\t|{get_artists_by_alphabetical_order[2]}\t|{get_artists_by_alphabetical_order[4]}\t|{get_artists_by_alphabetical_order[5]}\t      |")



while True:
  choice = input("\n1. Get artists by current placement\n2. Get artists by peak listeners\n3. Get artists by albums released\n4. Get artists by alphabetical order\n5. Exit\n\n> ").strip()
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
    break
  else:
    os.system("clear")
    print("Invalid choice")
    time.sleep(2)
    os.system("clear")


conn.commit()
conn.close()

