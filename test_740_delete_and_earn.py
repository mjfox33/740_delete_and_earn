import code_740_delete_and_earn as c1

def test_base_case():
    s = c1.Solution()
    assert s.deleteAndEarn([3,4,2]) == 6

def test_base_case_2():
    s = c1.Solution()
    assert s.deleteAndEarn([2,2,3,3,3,4]) == 9

def test_base_case_3():
    s=c1.Solution()
    assert s.deleteAndEarn([1,1,1,2,4,5,5,5,6]) == 18