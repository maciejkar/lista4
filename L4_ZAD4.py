from html.parser import HTMLParser
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
      
    def __str__(self):
        return str(self.items)

def checking_HTML_correctness(filename):
  """
  Funkcja ma za zadanie sprawdzać poprawność składni dokumentu HTML.
  Jako argument przyjmuje nazwę pliku, który ma sprawdzić.
  Zwraca True jeśli dokument jest poprawny składniowo i False jeśli nie jest.
  """
  without_close = ['link' ,'meta', 'BR' ,'br', 'img', 'hr' ]

  class Parse(HTMLParser):
    def __init__(self) :
      super().__init__()
      self.tags = []

    def handle_starttag(self, tag, attrs):
      if tag not in without_close:
        self.tags.append(tag)
      
    def handle_endtag(self, tag):
      if tag not in without_close:
        self.tags.append("/" + str(tag))

    def catched_tags(self):
        return self.tags
  

  stack = Stack()
  file_obj = open(filename, 'r')
  text = file_obj.read()
  parser = Parse()
  parser.feed(text)
  tags = parser.catched_tags()


  for tag in tags :
    if '/' not in tag:
      stack.push(tag)
    else:
      try:
        if tag.replace('/','') != stack.pop():
          return False
      except:
        return False
  return True


if __name__ == "__main__":
  print(checking_HTML_correctness("C:\\Users\\mkarc\\studia\\AISD\\lista4\\L4_ZAD4_sampleHTML_1.txt"))
  print(checking_HTML_correctness("C:\\Users\\mkarc\\studia\\AISD\\lista4\\L4_ZAD4_sampleHTML_2.txt"))
  print(checking_HTML_correctness("C:\\Users\\mkarc\\studia\\AISD\\lista4\\L4_ZAD4_sampleHTML_3.txt"))
  