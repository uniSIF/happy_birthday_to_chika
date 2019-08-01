import math
from enum import Enum, auto
from random import randint
import time

class Rarity(Enum):
    # 部員のレアリティを表す列挙型クラス
    UR = auto()
    SSR = auto()
    SR = auto()
    R = auto()

class Klab:
    # KLabが提供するスクフェスのサービスをまとめたクラス
    @staticmethod
    def scout():
        # 1回分の勧誘結果を返す関数
        tmp = randint(1,100)
        if(tmp > 99):
            return Rarity.UR
        elif(tmp > 95):
            return Rarity.SSR
        elif(tmp > 80):
            return Rarity.SR
        else:
            return Rarity.R

    @staticmethod
    def scout11(stones):
        # 11連の結果と使った石の数を返す関数

        # 石を50個持っていない貧乏人にはお引き取り願う
        if(stones < 50):
            scout_result = []
            used_stones = 0
            return (scout_result, used_stones)
        
        scout_result = []
        used_stones = 50
        # 11回勧誘を実施する
        for i in range(11):
            scout_result.append(Klab.scout())
        
        # 顧客満足度を向上するため、勧誘結果が全てRだった場合は1枚をSRにする
        if(scout_result.count(Rarity.R) == 11):
            scout_result[0] = Rarity.SR

        return (scout_result, used_stones)

    @staticmethod
    def sellStones(money):
        # ラブカストーン5000円分を可能な限り売りつける関数
        return math.floor(money / 5000) * 86

    @staticmethod
    def calcEarnedMoney(stones):
        # 儲けた金額を計算する関数
        return math.ceil(stones / 86) * 5000

    @staticmethod
    def printHateMessage():
        # URを引かれて悔しいメッセージを表示する関数
        print('!!!!! URを引いてしまいました !!!!!!')

    @staticmethod
    def fuxkYou():
        # URを2枚も引かれた恨みのメッセージを表示する関数
        print('!!!!! 残念 !!!!!')

    @staticmethod
    def printSuperUltraHappyMessage():
        # URが引けないのに20万円も課金する養分がいることを喜ぶメッセージを表示する関数
        print('♩♩♩♩♩ おめでとうございます！ ♩♩♩♩')
        print('==== HAPPY HAPPY BIRTHDAY! to Takami Chika! \'19.08.01🍊 ====')

if(__name__ == '__main__'):
    money = 195000  # 所持金195000円
    bought_stones = Klab.sellStones(money)  # 購入した石の数
    stones = bought_stones  # 現在の石の数
    ur_count = 0  # 引いたURの数
    scout_count = 0  # 回した11連の回数

    print('勧誘スタート！')
    while(True):
        # 11連を回す
        (scout_result, used_stones) = Klab.scout11(stones)
        stones -= used_stones
        scout_count += 1
        print('\r{0}回目　残りの石{1}個'.format(scout_count, stones), end='')
        time.sleep(0.1)
        
        # URを引いた場合は枚数をカウントする
        if(Rarity.UR in scout_result):
            print('')  # 改行を挿入
            for i in range(scout_result.count(Rarity.UR)):
                ur_count += 1
                Klab.printHateMessage()

        # 引いたURが2枚以上の場合はゲームオーバー
        if(ur_count >= 2):
            Klab.fuxkYou()
            total_used_stones = bought_stones - stones
            wastedMoney = Klab.calcEarnedMoney(total_used_stones)
            print('使ったラブカストーン{0}個（{1}円）'.format(total_used_stones, wastedMoney))
            break

        # URを2枚以上引けないまま11連を回せなくなったらゲームクリア
        if(len(scout_result) == 0):
            print('')  # 改行を挿入
            Klab.printSuperUltraHappyMessage()
            break
