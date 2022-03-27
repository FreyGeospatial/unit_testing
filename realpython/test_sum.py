# sum can accept any iterable as its first argumenty
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

# when calling module, run one of its functions
if __name__ == "__main__":
    print("test_sum:")
    print("\n")
    print("\n")
    test_sum()
    print("test_sum_tuple:")
    test_sum_tuple()
    print("Everything passed")
