import numpy as np

if __name__ == "__main__":
    num = input("Input the number of list: ")
    file = input("Input the file name: ")
    nums = np.random.randint(0, 300, int(num))
    nums.sort()

    with open(file, 'w') as f:
        for num in nums:
            f.write('deskImage_' + ( '00000' + str(num))[-5:] + '\n')
