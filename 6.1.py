def is_palidrom(string):
  return string.lower() == string[::-1].lower()
is_palidrom(input("Введите текст: "))
