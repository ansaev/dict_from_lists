dict_from_lists = lambda key_list, value_list: {
    key_list[i]: value_list[i] if i < len(value_list) else None
    for i in xrange(len(key_list))
    }
