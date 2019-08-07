
print("Hello")

print("__name value__: ", __name__)
print("name value:",__name__)


def main():
    print("python main function")


#if __name__ == '__main__':
#if __name__=="__main__":
main()


try:
    print(x)
except NameError:
    print ("not defined")
except:
    print("defined")      


try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
