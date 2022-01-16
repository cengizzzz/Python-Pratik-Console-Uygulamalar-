# name ="cengiz"
# def changeName(name):
#     name=new=name
#     print(name)

# changeName("atila")
# print(name)

name ="global_string"
def greeting():
    name="atila"
    def hello():
        print("hello "+name)
    hello()
greeting()
print(name)