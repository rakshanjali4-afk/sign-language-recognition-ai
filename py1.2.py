def bubble_sort(listitem):
    for i in range(len(listitem)):
        for j in range(len(listitem) - i - 1):
            if listitem[j] > listitem[j + 1]:
                temp = listitem[j]
                listitem[j] = listitem[j + 1]
                listitem[j + 1] = temp
    print(f"The sorted list using bubble sort is {listitem}")


def main():
    itemtosort = input("Enter the items separated by spaces: ").split()
    listitem = []
    for i in itemtosort:
        listitem.append(int(i))  # ✅ using append
    bubble_sort(listitem)


if __name__ == "__main__":
    main()