# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
name="A"
contactNumber="B H" ## сначала имя потом номер
note="C"
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


class PhoneBook ():
    def __init__(self,name, contactNumber, note):
        pass
    def search(self,contactNumber,name):
        contactNumber.split()
        for i in range(len(contactNumber)):
            if contactNumber[i]==name:
                return contactNumber[i+1]


PhoneContact1=PhoneBook(name, contactNumber, note)

print(PhoneContact1.search(contactNumber,name))