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

    def test_chk_a_2nd_deal(self):
        assert checkout_solution.checkout("AAAAA") == 200

    def test_chk_b_deal(self):
        assert checkout_solution.checkout("BB") == 45

    def test_chk_e_deal_no_b(self):
        assert checkout_solution.checkout("EE") == 80

    def test_chk_e_deal(self):
        assert checkout_solution.checkout("EEBB") == 80 + 30

    def test_chk_f_deal(self):
        assert checkout_solution.checkout("FFF") == 20

    def test_chk_h_deal(self):
        assert checkout_solution.checkout("HHHHH") == 45

    def test_chk_h_2nd_deal(self):
        assert checkout_solution.checkout("HHHHHHHHHH") == 80

    def test_chk_k_deal(self):
        assert checkout_solution.checkout("KK") == 120

    def test_chk_n_deal_no_m(self):
        assert checkout_solution.checkout("NNN") == 120

    def test_chk_n_deal(self):
        assert checkout_solution.checkout("NNNMM") == 120 + 15

    def test_chk_p_deal(self):
        assert checkout_solution.checkout("PPPPP") == 200

    def test_chk_Q_deal(self):
        assert checkout_solution.checkout("QQQ") == 80

    def test_chk_r_deal_no_q(self):
        assert checkout_solution.checkout("RRR") == 150

    def test_chk_r_deal(self):
        assert checkout_solution.checkout("RRRQQ") == 150 + 30

    def test_chk_u_deal(self):
        assert checkout_solution.checkout("UUUU") == 120

    def test_chk_v_deal(self):
        assert checkout_solution.checkout("VV") == 90

    def test_chk_v_2nd_deal(self):
        assert checkout_solution.checkout("VVV") == 130

    def test_chk(self):
        assert checkout_solution.checkout("AABCDABEEBFF") == 130 + 45 + 20 + 15 + 80 + 20

    def test_chk_mixed(self):
        assert checkout_solution.checkout("AABCDABABEEFFF") == 130 + 45 + 20 + 15 + 50 + 80 + 20

