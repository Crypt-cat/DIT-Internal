import sqlite3

conn = sqlite3.connect('artists.db')

cursor = conn.cursor()

cursor.execute('SELECT * FROM Artists;')

results = cursor.fetchall()

print(results)

def get_all_artists():
  
  cursor.execute('SELECT * FROM Artists;')

  Artists = cursor.fetchall()

  for Artists in Artists:
    print(f"{Artists[1]} | From: {Artists[6]} | Current: #{Artists[0]} | Peak: #{Artists[3]} | {Artists[2]} Monthly Listeners | {Artists[4]} Peak Listeners | Albums: {Artists[5]} ")


  
def get_artists_by_peak_listeners():
  query = "SELECT * FROM Artists ORDER BY PeakListeners DESC;"

  cursor.execute(query)

  get_artists_by_peak_listeners = cursor.fetchall()

  for get_artists_by_peak_listeners in get_artists_by_peak_listeners:
    print(f"{get_artists_by_peak_listeners[1]} | From: {get_artists_by_peak_listeners[6]} | Current: #{get_artists_by_peak_listeners[0]} | Peak: #{get_artists_by_peak_listeners[3]} | {get_artists_by_peak_listeners[2]} Monthly Listeners | {get_artists_by_peak_listeners[4]} Peak Listeners | Albums: {get_artists_by_peak_listeners[5]} ")
  



while True:
  choice = input("\n1. Get all artists\n2. Get by peak listeners\n3. Exit\n> ")
  if choice == "1":
    get_all_artists()
  elif choice == "2":
    get_artists_by_peak_listeners()
  elif choice == "3":
    break
  else:
    print("Invalid choice")

conn.commit()
conn.close()

