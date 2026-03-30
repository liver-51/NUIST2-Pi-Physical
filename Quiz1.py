# 作者：xieyuhan zhangliwen
# 日期：2026/3/30
# 描述：question~score~result
def quiz():
    print("Welcome to the Animal Quiz!")
    print("Answer the following questions:")
    # 问题列表
    questions = [
        "1. What is the largest animal on Earth?: a. Blue Whale, b. Mouse, c. Cat\n",
        "2. Which bird can fly backwards?: a. Cuckoo,b.Eagle, c.Hummingbird\n",
        "3. What is the only mammal capable of flight?: a. Bat, b. Squirrel, c.Dolphin\n"
    ]
    # 答案列表（与问题一一对应，小写适配输入判断）
    answers = [
        "blue whale",
        "hummingbird",
        "bat"
    ]
    score = 0
    # 循环提问
    for i in range(len(questions)):
        user_answer = input(questions[i]).strip().lower()
        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    # 输出最终分数
    print("\nQuiz completed!")
    print(f"You got {score}/{len(questions)} questions correct.")

# 运行测验函数
quiz()
