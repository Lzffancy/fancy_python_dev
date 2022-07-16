from functools import partial


def read_from_file(f_name, block_size=1024 * 8):
    with open(f_name, "rb") as fp:
        while True:
            chunk = fp.read(block_size)
            if not chunk:
                break
            yield chunk


def read_from_file01(f_name, block_size=1024 * 8):
    with open(f_name, "rb") as fp:
        for chunk in iter(partial(fp.read, block_size), b''):  # 如果iterator的_next_() 等于 b”“,则会stopiteration
            # if not chunk:
            #     break
            yield chunk


if __name__ == '__main__':
    content = read_from_file01("test_file.txt")
    print(content)
    for i in content:
        print(i)
