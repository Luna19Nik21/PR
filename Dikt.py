print("hello world")
user = {
    "userneme":"Luna",
    "password": 666,
    "robux": 0,
    "age": 19,
    "gender":"женский"
}
print("имя пользователя",user["userneme"])
print("у вас:",user["robux"],"робуксов")

print("до манипуляции",user)
# user.clear()
# print("после clear",user)

print(user.get("gender"))
print(user.items()) #возвращает вместо себя массив котержей
print(user.keys()) #создаёт массив из ключей
print(user.pop("robux"))
print(user)
print(user.values()) #создаёт массив из значений

print(user)
player ={
    "neme":"Luna",
    "HP": 120,
    "damage": 20
}
enemy = {
    "neme":"Nik",
    "HP": 120,
    "damage":15
}
def Fight(player,enemy):
    print(f'Игрок {player["neme"]} атакует {enemy["neme"]} и наносит {player["damage"]}')
    enemy["HP"] = player["damage"]
    print(f'У {enemy["neme"]} осталось {enemy["HP"]} здоровья')
Fight(player,enemy)
Fight(player,enemy)