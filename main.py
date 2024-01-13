import tkinter as tk

class Player:
    def __init__(self, name):
        self.name = name
        with open('players.txt', 'a')as n:
            n.write(self.name)
            n.write("\n")
        self.scores = []

    def record_score(self, score):
        self.scores.append(score)

    def total_score(self):
        return sum(self.scores)

    def average_score(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)

class BowlingLane:
    def __init__(self, lane_number):
        self.lane_number = lane_number
        self.players = {}

    def add_player(self, name):
        if name not in self.players:
            self.players[name] = Player(name)

    def record_score(self, name, score):
        if name in self.players:
            self.players[name].record_score(score)

class BowlingAlleyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diamond Bowling")

        self.lanes = [BowlingLane(lane_number) for lane_number in range(1, 11)]

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Player Name:").grid(row=0, column=0)
        self.player_name_entry = tk.Entry(self.root)
        self.player_name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Lane Number (1-10):").grid(row=1, column=0)
        self.lane_number_entry = tk.Entry(self.root)
        self.lane_number_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Score:").grid(row=2, column=0)
        self.score_entry = tk.Entry(self.root)
        self.score_entry.grid(row=2, column=1)

        tk.Button(self.root, text="Add Player", command=self.add_player).grid(row=0, column=2)
        tk.Button(self.root, text="Record Score", command=self.record_score).grid(row=1, column=2)
        tk.Button(self.root, text="View Stats", command=self.view_stats).grid(row=2, column=2)

        self.result_text = tk.Text(self.root, height=10, width=40)
        self.result_text.grid(row=3, column=0, columnspan=3)
    def add_player(self):
        name = self.player_name_entry.get()
        lane_number = int(self.lane_number_entry.get())

        if 1 <= lane_number <= 10:
            lane = self.lanes[lane_number - 1]
            lane.add_player(name)
            self.result_text.insert(tk.END, f"{name} has been added to Lane {lane_number}.\n")
        else:
            self.result_text.insert(tk.END, "Invalid lane number. Please choose a lane between 1 and 10.\n")

    def record_score(self):
        name = self.player_name_entry.get()
        lane_number = int(self.lane_number_entry.get())
        score = int(self.score_entry.get())

        if 1 <= lane_number <= 10:
            lane = self.lanes[lane_number - 1]
            lane.record_score(name, score)
            self.result_text.insert(tk.END, f"Score of {score} recorded for {name} on Lane {lane_number}.\n")
        else:
            self.result_text.insert(tk.END, "Invalid lane number. Please choose a lane between 1 and 10.\n")

    def view_stats(self):
        name = self.player_name_entry.get()
        lane_number = int(self.lane_number_entry.get())

        if 1 <= lane_number <= 10:
            lane = self.lanes[lane_number - 1]

            if name in lane.players:
                player = lane.players[name]
                self.result_text.insert(tk.END, f"Stats for {name} on Lane {lane_number}:\n")
                self.result_text.insert(tk.END, f"Total Score: {player.total_score()}\n")
                self.result_text.insert(tk.END, f"Average Score: {player.average_score()}\n")
            else:
                self.result_text.insert(tk.END, f"{name} is not on Lane {lane_number}. Please add them first.\n")
        else:
            self.result_text.insert(tk.END, "Invalid lane number. Please choose a lane between 1 and 10.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = BowlingAlleyApp(root)
    root.mainloop()
