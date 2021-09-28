def main():
    #write your code below this line
    nums = []
    while True:
        num = int(input())
        if (num == -1):
            break
        else:
            nums.append(num)
    sum = 0
    count = 0
    for number in nums:
        sum += number
        count += 1
    print("Average: " + str(sum / count))

if __name__ == '__main__':
    main()
