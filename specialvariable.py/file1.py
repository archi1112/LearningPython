# __name__ is special variable used to check whether the first statement running is from this file if yes this will print __main__ else will print filename which imported
print("File1 - " , __name__)
if __name__ == "__main__":
    print("file1 running by self")
else:
    print("file1 is inported")