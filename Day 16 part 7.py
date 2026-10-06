def show_info(**info):

    for key,value in info.items():
        print(key, ":", value)
show_info(
    name = "Ali",
    age = 22,
    city = "Lahore"
)