import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from db_config import get_connection
import queries

# Password to access the main program
APP_PASSWORD = "uefa2025"  # You can change this!

def open_main_app():
    login_window.destroy()  # Close the login window
    launch_main_app()       # Open the main query GUI

def check_password():
    entered = password_entry.get()
    if entered == APP_PASSWORD:
        open_main_app()
    else:
        messagebox.showerror("Access Denied", "Incorrect password. Try again.")

# LOGIN WINDOW SETUP
login_window = tk.Tk()
login_window.title("Login: UEFA Champions League")
login_window.geometry("400x120")
login_window.resizable(False, False)

tk.Label(login_window, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
password_entry = tk.Entry(login_window, show="*", width=25)
password_entry.pack()
tk.Button(login_window, text="Login", command=check_password).pack(pady=10)

login_window.mainloop()


# Create ONE root window
app = tk.Tk()
app.title("UEFA Champions League Database")
app.geometry("550x800")
## app.iconbitmap("uefa_icon.ico")  # Optional: if you have an .ico file

# Load and display the logo
logo = PhotoImage(file="uefa_logo.png")
logo_label = tk.Label(app, image=logo)
logo_label.pack(pady=10)

# Title above the queries
tk.Label(
    app,
    text="Select a query to run:",
    font=("Helvetica", 14, "bold"),
    fg="#003366"  # dark blue hex code
).pack(pady=10)


#3er Version
def display_results(data, headers):
    result_window = tk.Toplevel()
    result_window.title("UEFA Results")

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Helvetica", 10, "bold underline"))

    tree = ttk.Treeview(result_window, columns=headers, show='headings')
    for header in headers:
        tree.heading(header, text=header)
        tree.column(header, width=320, anchor="center") #center the resuts

    # Convert each row value to string, even if multiple columns
    for row in data:
        clean_row = tuple(str(item) for item in row)
        tree.insert("", tk.END, values=clean_row)

    tree.pack(fill='both', expand=True)


def run_query(query_func, headers):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        data = query_func(cursor)
        display_results(data, headers)
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Add Player to the database

def open_add_player_window():
    def submit_player():
        name = entry_name.get()
        position = entry_position.get()
        dob = entry_dob.get()
        team_id = entry_team.get()

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Player (Name, Position, DOB, TeamID) VALUES (?, ?, ?, ?)",
                (name, position, dob, team_id)
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Player '{name}' added successfully.")
            add_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    add_window = tk.Toplevel()
    add_window.title("Add New Player")
    add_window.geometry("300x250")

    tk.Label(add_window, text="Player Name:").pack(pady=5)
    entry_name = tk.Entry(add_window)
    entry_name.pack()

    tk.Label(add_window, text="Position:").pack(pady=5)
    entry_position = tk.Entry(add_window)
    entry_position.pack()

    tk.Label(add_window, text="Date of Birth (YYYY-MM-DD):").pack(pady=5)
    entry_dob = tk.Entry(add_window)
    entry_dob.pack()

    tk.Label(add_window, text="Team ID:").pack(pady=5)
    entry_team = tk.Entry(add_window)
    entry_team.pack()

    tk.Button(add_window, text="Add Player", command=submit_player).pack(pady=10)


# Query buttons
btn1 = tk.Button(app, text="Referees Without Matches", command=lambda: run_query(queries.referees_without_matches, ["Name"]))
btn1.pack(pady=5)

btn2 = tk.Button(app, text="Players Born 2000 or Teams After 2000", command=lambda: run_query(queries.players_born_2000_or_teams_after_2000, ["Name"]))
btn2.pack(pady=5)

btn3 = tk.Button(app, text="Top Goal Scorers", command=lambda: run_query(queries.top_goal_scorers, ["Player", "Goals"]))
btn3.pack(pady=5)

btn4 = tk.Button(app, text="Total Goals Per Team", command=lambda: run_query(queries.team_goal_totals, ["Team", "Goals"]))
btn4.pack(pady=5)

btn5 = tk.Button(app, text="Goals by Team & Player (OLAP)", command=lambda: run_query(queries.olap_goals_by_team_and_player, ["Team", "Player", "Goals"]))
btn5.pack(pady=5)

btn_add = tk.Button(app, text="➕ Add New Player", command=open_add_player_window)
btn_add.pack(pady=10)

# Run the app
app.mainloop()