# Creating youtube manager app using sqlite3 database
import sqlite3

conn = sqlite3.connect('manager.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time TEXT NOT NULL,
        url TEXT NOT NULL
    )
''')
def add_video(name, time, url):
    cursor.execute('''
        INSERT INTO videos (name, time, url) VALUES (?, ?, ?)
    ''', (name, time, url))
    conn.commit()
    print(f"Video '{name}' added successfully.")

def list_videos():
    cursor.execute('SELECT * FROM videos')
    videos = cursor.fetchall()
    if videos:
        for video in videos:
            print(f"ID: {video[0]}, Name: {video[1]}, Time: {video[2]}, URL: {video[3]}")
    else:
        print("No videos found.")

def update_video(video_id, name, time, url):

    cursor.execute('''
        UPDATE videos SET name = ?, time = ?, url = ? WHERE id = ?''', 
        (name, time, url, video_id)
    )
    conn.commit()


def delete_video():
    list_videos()
    video_id = input("Enter the ID of the video to delete: ")
    cursor.execute('DELETE FROM videos WHERE id = ?', (video_id,))
    conn.commit()
    print(f"Video with ID {video_id} deleted successfully.")

def main():
    while True:
        print("*" * 60)
        print("\n Youtube Manager | Choose an option ")
        print("1. List all youtube videos")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app \n")
        print("*" * 60 )

        choice = input("Enter your choice : ")

        match choice: 
            case '1':
                list_videos()
            case '2':
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                url = input("Enter video URL: ")
                add_video(name, time, url)
            case '3':               
                print("*" * 80)
                list_videos()
                print("*" * 80)

                video_id = input("Enter the ID of the video to update: ")
                name = input("Enter new video name: ")
                time = input("Enter new video time: ")
                url = input("Enter new video URL: ")
                update_video(video_id, name, time, url)
            case '4':
                delete_video()
            case '5':
                print("Exiting the app...")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()