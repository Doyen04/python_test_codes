import tkinter as tk
from random import randint


class Game(tk.Canvas):
    HEIGHT = 400
    WIDTH = 600
    GAP = 80

    def __init__(self):
        super().__init__(width=600, height=400, bg="black")
        self.pack(pady=100)
        self.init()

    def init(self):
        self.boxes = []
        self.coin = []
        self.speed = 80
        self.skip = -10
        self.On = False
        self.score = 0
        self.ply = {}
        self.contact = False
        self.draw_button()
        self.platform()

    def draw_button(self):
        dir = ['Up', 'Left', 'Right', 'Start']
        global doub_click
        doub_click = False
        i = 0
        for y in range(3):
            for x in range((y + 1) % 2, 3, 2):
                label = tk.Button(text=dir[i],
                                  fg='white',
                                  bg='red',
                                  width=5,
                                  height=3,
                                  border=2,
                                  highlightbackground="blue", )
                label.bind("<Double-Button-1>", self.key_)
                label.bind("<ButtonPress-1>", self.key_press)
                label.place(x=(150) + (95 * x), y=self.HEIGHT + 200 + (85 * y), )
                i += 1

    def action(self, event):
        global doub_click
        direc = event.widget['text']
        if self.On and direc == 'Up' and self.ply['jump']:
            if doub_click:
                self.ply['jump_val'] = 60
                doub_click = False
            else:
                self.ply['jump_val'] = 40
            self.ply['jump'] = False
        if direc == 'Start' and self.On == False:
            self.On = True
            self.start()
            self.jump()
            self.reduce()

    def key_(self, event):
        global doub_click
        doub_click = True

    def key_press(self, event):
        self.after(180, self.action, event)

    def jump(self):
        speed = m = 0
        if self.ply['jump_val'] > 0:
            self.ply['jump_val'] -= 5
            m = -5
        elif self.ply['jump_val'] <= 0:
            m = 5
        if self.check(m):
            self.move(self.ply['ply'], 0, m)
            self.ply['jump'] = False
        if self.check(m) == False:
            self.ply['jump'] = True
        if self.On:
            self.after(self.speed, self.jump)

    def platform(self):
        ply_pos = init = i = 0
        for key in range(4):
            x = randint(35, 40) * 5
            y = randint(60, 63) * 5
            if key == 0:
                i = 350
                ply_pos = y
            else:
                i = 0
            rect = self.create_rectangle(init, y, x + i + init, 400, fill='green', tag='rect')
            init = x + init + i + self.GAP
            self.boxes.append(rect)
            for coin in range(4):
                start = init + (coin * 70)
                to = start + 10
                can = self.create_oval(start, y - 30, to, y - 20, fill='white', tag='coin')
                self.coin.append(can)

        rect = self.create_rectangle(200, ply_pos - 50, 250, ply_pos, fill='red', )
        self.ply['ply'] = rect
        self.ply['jump'] = True
        self.ply['jump_val'] = 0

    def collide(self, ):
        ply_x = self.coords(self.ply['ply'])[2]
        ply_y = self.coords(self.ply['ply'])[3]
        x = [self.coords(key)[0] for key in self.boxes]
        y = [self.coords(key)[1] for key in self.boxes]
        for cx, cy in zip(x, y):
            if cx < ply_x and cy < ply_y and cx > 200:
                return True
        return False

    def check(self, m):
        ply_y = self.coords(self.ply['ply'])[3] + m
        y = [self.coords(key)[1] for key in self.boxes]
        x1 = [self.coords(key)[2] for key in self.boxes]
        x0 = [self.coords(key)[0] for key in self.boxes]
        for cood, x in zip(y, zip(x0, x1)):
            if ply_y > cood and x[0] <= 250 and x[1] >= 200:
                return False
        return True

    def slide(self):
        for key in self.boxes:
            self.move(key, self.skip, 0)
            nx = [self.coords(spt)[2] for spt in self.boxes]
            for nx, box in zip(nx, self.boxes):
                if nx < 0:
                    x = randint(35, 40) * 5
                    y = randint(60, 64) * 5
                    indx = self.boxes.index(box)
                    indx = self.boxes[indx - 1]
                    prex = self.coords(indx)[2] + self.GAP
                    self.coords(box, prex, y, prex + x, 400)

    def move_coin(self):
        for coin in self.coin:
            self.move(coin, self.skip, 0)
            nx = [self.coords(cin)[2] for cin in self.coin]
            for nx, coin in zip(nx, self.coin):
                if nx < 0:
                    y = randint(56, 58) * 5
                    index = self.coin.index(coin)
                    prev_c = self.coin[index - 1]
                    x = self.coords(prev_c)[2] + 70
                    self.itemconfigure(coin, fill='white')
                    self.coords(coin, x, y, x + 10, y + 10)

    def collide_coin(self):
        self.delete('scor')
        coinx = [self.coords(x)[2] for x in self.coin]
        coiny = [self.coords(y)[3] for y in self.coin]
        player = self.coords(self.ply['ply'])
        coord = list(zip(coinx, coiny))
        check = None
        for coord, coin in zip(coord, self.coin):
            if coord[0] <= player[2] and coord[1] <= player[3] and coord[0] > player[0]:
                check = True
                if self.contact == False and check:
                    self.score += 1
                    self.itemconfigure(coin, fill='black')
                    self.contact = True
        if self.contact and check == None:
            self.contact = False
        self.create_text(
            40, 20, text=f"Score : {self.score}", tag="scor", fill="white", font=('Helvetica 4 bold'))

    def reduce(self):
        self.speed -= 1
        if self.On:
            self.after(1200, self.reduce)

    def start(self):
        if self.collide():
            self.delete(tk.ALL)
            self.boxes = []
            self.On = False
            self.init()
        if self.On:
            self.slide()
            self.move_coin()
            self.collide_coin()
            self.after(self.speed, self.start)


win = tk.Tk()
win.config(bg='black')
g = Game()
win.mainloop()
