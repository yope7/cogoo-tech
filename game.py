import numpy as np

def guess_the_number():
    # 1から100までのランダムな整数を生成
    secret_number = np.random.randint(1, 101)
    
    attempts = 0

    print("=== 数当てゲーム ===")
    print("1から100までの整数を当ててください。")

    while True:
        # ユーザーに入力を求める
        user_guess = int(input("予想した数を入力してください: "))
        
        # 入力回数をカウント
        attempts += 1

        # 入力した数と秘密の数を比較
        if user_guess == secret_number:
            print(f"おめでとうございます！ {attempts} 回で正解しました。")
            break
        elif user_guess < secret_number:
            print("もっと大きい数です。")
        else:
            print("もっと小さい数です。")

if __name__ == "__main__":
    guess_the_number()
