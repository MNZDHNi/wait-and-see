import os

"""
屏幕模块，包含GameScreen和GameFrame类。
GameScreen负责管理屏幕的显示和刷新，GameFrame负责管理当前帧的内容。
"""
class GameScreen:
    def __init__(self, InitConfig):
        self.width = InitConfig.width
        self.height = InitConfig.height
        self.have_new_frame = False

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def update_frame(self, new_frame):
        if new_frame is not None:
            self.have_new_frame = new_frame

    def refresh(self):
        if not self.have_new_frame:
            return
        
        self.clear()
        print("/", "-" * self.width, "\\", sep="")

        for i in range(self.height):
            print("|", end="")
            for j in range(self.width):
                if self.have_new_frame is not None:
                    print(self.have_new_frame.picture[i][j], end="")
                else:
                    print(" ", end="")
            print("|")

        print("\\", "-" * self.width, "/", sep="")
        self.have_new_frame = False


class GameFrame:
    def __init__(self, InitConfig):
        self.width = InitConfig.width
        self.height = InitConfig.height
        self.picture = [[" " for _ in range(self.width)] for _ in range(self.height)]

    def draw(self, position, content):
        x, y = position
        if content["sharp"] is None:
            # 添加无sharp方法，以便于绘制非矩阵文本
            return
        i, j = content["sharp"]

        for line in range(i):
            for col in range(j):
                if 0 <= x + line < self.height and 0 <= y + col < self.width:
                    self.picture[x + line][y + col] = content["Content"][line][col]
                else:
                    # 超出边界时抛出异常
                    raise ValueError("Content exceeds frame boundaries.")