import nacl.utils

def random() -> bytes:
  return nacl.utils.random()

def main():
  print(random())

if __name__ == "__main__":
  # for i in range(10):
  #   print("i: ",i)
  main()