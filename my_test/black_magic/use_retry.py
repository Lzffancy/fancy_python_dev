from tenacity import retry

@retry()
def test_retry():
    print("重试！")
    # raise Exception

test_retry()
