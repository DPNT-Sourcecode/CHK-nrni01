from solutions.CHK import checkout_solution


class TestChk():
    def test_chk_a(self):
        assert checkout_solution.checkout("A") == 50
    def test_chk_b(self):
        assert checkout_solution.checkout("B") == 30
    def test_chk_c(self):
        assert checkout_solution.checkout("C") == 20
    def test_chk_d(self):
        assert checkout_solution.checkout("D") == 12