def sdbm(plain_text: str) -> str:
    """
    Function implements sdbm hash, easy to use, great for bits scrambling.
    iterates over each character in the given string and applies function to each of
    them.
    """
    hash = 0
    for plain_chr in plain_text:
        #ord ascll码               左移6位      左移16位
        hash = ord(plain_chr) + (hash << 6) + (hash << 16) - hash
        # print(hash)
    return hash&0x7FFFFFFF

if __name__ == '__main__':
    # print(sdbm("fancylee"))
    # print(sdbm("fancylee"))

    print(sdbm("fancyleeqqllladwiaoidwia"),"a")
    # print(ord("a"))
    # print(1<<6)
    str_hash=sdbm("www")
    print(str_hash)
    page_offset = str_hash % 2000
    print(page_offset)
