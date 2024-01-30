numbers1 = [13,31,23,53,63,75,213,34,57,86,123,45,75,34,456]

def aver(numbers):
    result = sum(numbers) / len(numbers)
    return result

aver(numbers1)
print(aver(numbers1))

text1 = "sfef soig dfaw sf dkjg dois fdjg usder omyi sdfw eiruw jdfsh vnx iay"

def find_h(text):
    count = 0
    hol = "aeiouyAEIOUY"
    for h in text:
        if h in hol:
            count += 1
    return count
    # print(count)

print(find_h(text1))
print(len(text1))


COMFORT = 25

def temp(carrent) -> int:
    if COMFORT > carrent:
        result = COMFORT - carrent
        print("За холодно. До комфортної температури збільште перемикач на:", result, "градуси")
    elif COMFORT < carrent:
        result = carrent - COMFORT
        print("За тепло. До комфортної температури зменште перемикач на:", result, "градуси")
    elif COMFORT == carrent:
        print("Зараз ідеально комфортна температура")
    return result

temp(44)


DEFAULT_LEVEL = 1

1-100
2-200
3-300
4-400
5-500

def upgrade(current, score):
    if(score > 0):
        result = 100 - score
        print("До нового рівня залишилось", result, "очок")

        if(score == 100):
            current += 1
            print("Новий рівень")
    elif (score < 0):
        print("Ви втратили", score, "очок")
        if (score == -100):
            current -= 1
            print("О ні, зменшення рівня")


upgrade(2, 19)