


class cherryjam():
    count = score.jam_count
    price = round(15*1.1**count())
    buff = 5

print(cherryjam.count, cherryjam.price)

class autoscore():
    total = cherryjam.buff*cherryjam.count()

