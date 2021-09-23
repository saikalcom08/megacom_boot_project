def get_lists(lists):
    list_dictionary = {x: x for x in lists}
    #for i in lists:
        #list_dictionary = dict.fromkeys(lists)
    return list_dictionary


lists = [45, 54, 78, 45, 32, 21, 23]
print(get_lists(lists))