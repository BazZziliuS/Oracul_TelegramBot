def batched(get_list: list, count: int) -> list:
    return [get_list[i:i + count] for i in range(0, len(get_list), count)]

def clear_list(get_list: list) -> list:
    while "" in get_list:
        get_list.remove("")
    while " " in get_list:
        get_list.remove(" ")
    while "," in get_list:
        get_list.remove(",")
    while "\r" in get_list:
        get_list.remove("\r")
    return get_list