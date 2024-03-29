# Задачи со второго семинара. Односвязные списки


## 1. Проверка наличия цикла

__Условие:__ Дан односвязный список. Необходимо проверить, является ли этот список циклическим.

__Прим.:__ Циклическим (кольцевым) списком называется список у которого последний узел ссылается на один из предыдущих узлов.

[Решение здесь](./check_cycle.py)

## 2. Развернуть односвязный список

__Условие:__ Необходимо написать функцию, которая принимает на вход односвязный список и возвращает список со значениями в обратном порядке.

[Решение здесь](./reverse.py)


## 3. Найти середину списка

__Условие:__ Дан связный список. Необходимо найти середину списка. Сделать это необходимо за O(n) без дополнительных аллокаций.

[Решение здесь](./find_middle.py)

## 4. Удалить элемент по значению из списка

__Условие:__ Необходимо написать функцию, которая принимает на вход односвязный список и некоторое целое число val. Необходимо удалить узел(-ы) из списка, значение(-я) которого(-ых) равно(-ы) val.

[Решение здесь](./delete.py)

## 5. Слияние 2 отсортированных списков

__Условие:__ Необходимо написать функцию, которая на вход принимает 2 отсортированных списка и собирает их в 1 отсортированный список. Сложость по памяти O(1). Сложность по времени O(n).


**Пример 1**

**In:**
```
[3, 6, 8]
[4, 7, 9, 11]
```
**Out:**
```
[3, 4, 6, 7, 8, 9, 11]
```

[Решение здесь](./merge.py)
