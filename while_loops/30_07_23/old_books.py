searched_book = input()

checked_books = 0
book_found = False
input_line = input()
while input_line != 'No More Books':
    if input_line == searched_book:
        book_found = True
        break

    checked_books += 1
    input_line = input()

if book_found:
    print(f'You checked {checked_books} books and found it.')
else:
    print('The book you search is not here!')
    print(f"You checked {checked_books} books.")

