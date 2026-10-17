import time
import random


def read_choice(prompt, allowed):
    while True:
        value = input(prompt).strip().lower()
        if value in allowed:
            return value
        print("Неверный ввод. Допустимые варианты: " + ", ".join(allowed))


health = 100
max_health = 100
coins = 20
potions = 3
rooms = 0
damage_bonus = 0
has_hat = False
accessory = False
wearit =  False
has_sword = False

POTION_PRICE = 10
SWORD_PRICE = 30
SWORD_BONUS = 12

print("кол-во начального здоровья: 100 HP, баланс: 20, зелье лечения: 3 штуки по 25 HP")
while health > 0:
    print("\n1 — идти дальше")
    print("2 — выпить зелье")
    print("3 — посмотреть статус")
    print("4 — магазин")

    choice = input("Твой выбор: ")
    if choice == "1":
        room_type = random.choice(["монстр", "сундук", "монеты", "ничего"])
        rooms += 1
        print("переходим в следующую комнату...")
        time.sleep(2)
        if room_type == "монстр":
            monster_hp = random.randint(60, 80)
            potion_sickness = False
            while monster_hp > 0 and health > 0:
                print("Монстр атакует! ты выберешь: атака/зелье/сбежать")
                answer = input()
                if answer == "атака":
                    damage = random.randint(30, 45)
                    monster_damage = random.randint(30, 45)
                    monster_hp -= damage
                    print("ты успешно атаковал и нанес", damage, " урона, количество хп у противника: ", monster_hp)
                    time.sleep(2)
                    if monster_hp <= 0:
                        reward = random.randint(5, 15)
                        coins += reward
                        print("Монстр побеждён!")
                        print("Ты получил", reward, "монет. Теперь у тебя", coins, "монет.")
                        break
                    health = health - monster_damage
                    print("он атакует. . . снял у тебя ", monster_damage, "HP! количество лечебных зелий:", potions, "\n текущее здоровье:", health)
                    time.sleep(1.5)
                elif answer == "зелье":
                    if potions > 0:
                        potions -= 1
                        health = min(100, health + 25)
                        potion_sickness = True
                        print("Ты выпил зелье. HP:", health)
                        print("Послезельевая болезнь: урон снижен на 8 до конца боя.")
                    else:
                        print("Зелья закончились!")
                elif answer == "сбежать":
                    health = health - 20
                    print("пока вы бежали, монстр нанес вам 20 урона в спину, тем не менее, вы скрылись без награды.")

        elif room_type == "сундук":
            print("вы нашли сундук! открываем. . .")
            time.sleep(2)
            item_type = random.choice(["шляпа", "амулет", "мешок", "мантия"])
            if item_type == "шляпа":

                print("Ты нашёл сундук! в нем есть загадочный артефакт, открываем . . .")
                if not has_hat:
                    has_hat = True
                    damage_bonus += 10
                    print("Ты надел шляпу! Урон навсегда увеличился на 10.")
                else:
                    sell_coins = random.randint(15, 30)
                    coins = coins + sell_coins
                    print("Ты нашёл ещё одну шляпу, но одна у тебя уже надета. Ты продал второй экземпляр и поручил выручку в ", sell_coins, "/n баланс: ", coins)
                time.sleep(2)
            elif item_type == "амулет":
                if not accessory:
                    accessory = True
                    max_health = 125
                    health = max_health
                    print("вы нашли амулет! ваше максимальное значение хп повышено. новое значение: 125. Вы были излечены до предела!")
                else:
                    new_sell = random.randint(15, 30)
                    coins = coins + new_sell
                    print("вы нашли амулет, но 1 у вас уже есть. Амулет был продан, вы получили ", new_sell, "/n баланс: ", coins)
            elif item_type == "мешок":
                take_coins = random.randint(50, 60)
                coins = coins + take_coins
                print("вы нашли мешок золота! его можно получать беск. кол-во раз, в отличие от других предметов сундука. вы получили", take_coins, "баланс: ", coins)
                time.sleep(2)

            elif item_type == "мантия":
                max_health += 10
                health = max_health
                damage_bonus += 5
                found_coins = random.randint(15, 30)
                coins = coins + found_coins

                print("Вы нашли мантию! Умеренное повышение статистики, урон был увеличен на 5, макс. здоровье на 10, в карманах нашли", coins, "монет, баланс: ", coins)
                time.sleep(2)

            else:
                lost_coins = random.randint(3, 5)
                coins = coins - lost_coins
                print("Комната пустая, ты потерял по дороге", lost_coins, " монет. Не отчаивайся, лол.")
                time.sleep(2)

        elif room_type == "ничего":
            health = health - 10
            print("вы ничего не нашли в комнате, лишь зря прошли ловушки, хп понижено на 10,здоровье: ", health)
            time.sleep(2)

        elif room_type == "монеты":
            coins += 10
            print("вы нашли 10 золота в комнате! баланс:", coins)
            time.sleep(2)
    elif choice == "2":
        health = min(100, health + 25)
        print("зелье успешно выпито. HP:", health)

    elif choice == "3":
        print('статистика на текущее время:', '\nздоровье: ', health,
              "\nмаксимальный запас: ", max_health, "\nбаланс:", coins, "\n кол-во лечебных зелий: ", potions, "\n пройдено комнат: ", rooms)

    elif choice == "4":
        while True:
            print("\nМагазин. У тебя", coins, "монет.")
            print("1 — лечебное зелье (+25 HP при использовании):", POTION_PRICE, "монет")
            print("2 — меч (+12 к урону, один раз):", SWORD_PRICE, "монет")
            print("3 — выйти из магазина")
            purchase = read_choice("Что купить? ", ("1", "2", "3"))

            if purchase == "1":
                if coins >= POTION_PRICE:
                    coins -= POTION_PRICE
                    potions += 1
                    print("Зелье куплено. Теперь зелий:", potions, "Монет:", coins)
                else:
                    print("Недостаточно монет для покупки зелья.")
            elif purchase == "2":
                if has_sword:
                    print("Меч уже куплен и надет. Второй купить нельзя.")
                elif coins < SWORD_PRICE:
                    print("Недостаточно монет для покупки меча.")
                else:
                    coins -= SWORD_PRICE
                    has_sword = True
                    damage_bonus += SWORD_BONUS
                    print("Ты купил и надел меч! Урон увеличен на", SWORD_BONUS, ". Монет:", coins)
            else:
                break




