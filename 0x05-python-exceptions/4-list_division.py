def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            my_list_1[i] / my_list_2[i]
    except TypeError:
        new_list.append(0)
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")
    else:
        for i in range(list_length):
            new_list.append(my_list_1[i] / my_list_2[i])
    finally:
        return new_list
