"""
素材类
"""
class Picture:
    def __init__(self, content):
        self.content = content
        self.sharp = None

    def get_content(self):
        return self.content
    
    def init_sharp(self):
        # 目前不能调用
        self.sharp = (0,0)