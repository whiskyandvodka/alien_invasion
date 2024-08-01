import json
from pathlib import Path

class GameStatus:
    """跟踪游戏的统计信息"""
    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.setting
        self.reset_status()
        self.score = 0
        self.level = 1

        # 在任何情况下都不应重置最高分
        self.high_score = 0
        self.path = 'high_score.txt'
        self.load_high_score()

    def reset_status(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """加载历史最高分"""
        path = Path(self.path)
        if path.exists():
            contents = path.read_text()
            self.high_score = json.loads(contents)
        else:
            self.high_score = 0

    def save_high_score(self):
        """保存历史最高分到JSON文件中"""
        path = Path(self.path)
        contents = json.dumps(self.high_score)
        path.write_text(contents)

