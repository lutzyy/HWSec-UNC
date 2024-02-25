from main_trisha import Dictionary

def test_add() -> None:
    mainDic = Dictionary()
    mainDic.add("wistoria", 7)
    mainDic.add("cats", 8)

def test_add_empty() -> None:
    mainDic = Dictionary()
    mainDic.add("", 0)

def test_retrieve() -> None:
    mainDic = Dictionary()
    mainDic.add("wistoria", 7)
    mainDic.add("cats", 8)
    mainDic.retrieve("dogs")

def test_retrieve_empty() -> None:
    mainDic = Dictionary()
    mainDic.add("", 0)
    mainDic.retrieve("")

def test_product() -> None:
    mainDic = Dictionary()
    mainDic.add("wistoria", 7)
    mainDic.add("cats", 8)
    mainDic.retrieve("dogs")
    assert "56" == str(mainDic.product("wistoria", "cats"))
