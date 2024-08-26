import random


def generate_random_iccid(length=20):
    iccid = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return iccid


random_iccid = generate_random_iccid()
print(f"Generated ICCID: {random_iccid}")
