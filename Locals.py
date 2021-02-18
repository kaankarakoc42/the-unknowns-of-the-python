def hi(name=""):
    print("hi",name)

#if you want to run function from their names as string you can do this
locals().get("hi")("kaan")
