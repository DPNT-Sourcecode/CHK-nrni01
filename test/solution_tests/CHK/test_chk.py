from solutions.CHK import checkout_solution


class TestChk():
    def test_chk_a(self):
        assert checkout_solution.checkout("A") == 50

    def test_chk_b(self):
        assert checkout_solution.checkout("B") == 30

    def test_chk_c(self):
        assert checkout_solution.checkout("C") == 20

    def test_chk_d(self):
        assert checkout_solution.checkout("D") == 15

    def test_chk_a_deal(self):
        assert checkout_solution.checkout("AAA") == 130

    def test_chk_b_deal(self):
        assert checkout_solution.checkout("BB") == 45

    def test_chk(self):
        assert checkout_solution.checkout("AABCDAB") == 130 + 45 + 20 + 15

    def test_chk_mixed(self):
        assert checkout_solution.checkout("AABCDABAB") == 130 + 45 + 20 + 15 + 50 + 30

    def test_chk_e_deal_no_b(self):
        assert checkout_solution.checkout("EE") == 80

    def test_chk_e_deal(self):
        assert checkout_solution.checkout("EEBB") == 80 + 30

