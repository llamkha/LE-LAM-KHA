import unittest

class Account:
    def __init__(self, balance=0):
        self.balance = balance

class ATM:
    def __init__(self, account, password):
        self.account = account
        self.password = password
        self.accounts = {}  # Giả sử đây là danh sách các tài khoản có trong ngân hàng

    def add_account(self, account_id, account):
        self.accounts[account_id] = account

    def check_password(self, password):
        return self.password == password

    def withdraw_cash(self, amount, password):
        if not self.check_password(password):
            raise ValueError("Sai mật khẩu")
        if amount > 200:
            raise ValueError("Số tiền rút vượt quá giới hạn $200")
        if self.account.balance < amount:
            raise ValueError("Số dư không đủ")
        
        self.account.balance -= amount
        return self.account.balance

    def transfer_money(self, amount, account_id):
        if account_id not in self.accounts:
            raise ValueError("Tài khoản đích không tồn tại")
        if amount > 1000:
            raise ValueError("Số tiền chuyển vượt quá giới hạn $1000")
        if self.account.balance < amount:
            raise ValueError("Số dư không đủ")
        
        self.account.balance -= amount
        self.accounts[account_id].balance += amount
        return self.account.balance, self.accounts[account_id].balance

class ATMTest(unittest.TestCase):
    def setUp(self):
        # Khởi tạo các tài khoản và ATM
        self.account = Account(balance=500)
        self.atm = ATM(self.account, password="1234")

        # Tạo thêm tài khoản cho mục đích kiểm tra chuyển khoản
        self.third_party_account = Account(balance=300)
        self.atm.add_account("third_party", self.third_party_account)

    # Kiểm tra chức năng rút tiền
    def test_withdraw_correct_credentials(self):
        # Đảm bảo rằng mật khẩu chính xác
        self.assertTrue(self.atm.check_password("1234"))
    
    def test_withdraw_insufficient_balance(self):
        # Kiểm tra rằng không thể rút tiền nếu không đủ số dư
        with self.assertRaises(ValueError, msg="Số dư không đủ"):
            self.atm.withdraw_cash(600, "1234")
    
    def test_withdraw_balance_update(self):
        # Kiểm tra rằng số dư được cập nhật sau khi rút tiền thành công
        self.atm.withdraw_cash(100, "1234")
        self.assertEqual(self.account.balance, 400)

    # Kiểm tra chức năng chuyển khoản
    def test_transfer_account_exists(self):
        # Đảm bảo tài khoản đích tồn tại
        self.assertIn("third_party", self.atm.accounts)

    def test_transfer_balance_update(self):
        # Kiểm tra rằng số dư của cả hai tài khoản được cập nhật sau khi chuyển khoản thành công
        self.atm.transfer_money(200, "third_party")
        self.assertEqual(self.account.balance, 300)
        self.assertEqual(self.third_party_account.balance, 500)

    def test_transfer_error_no_update(self):
        # Kiểm tra rằng nếu xảy ra lỗi, không có sự thay đổi số dư
        with self.assertRaises(ValueError):
            self.atm.transfer_money(1200, "third_party")  # Số tiền vượt quá giới hạn
        self.assertEqual(self.account.balance, 500)
        self.assertEqual(self.third_party_account.balance, 300)

if __name__ == "__main__":
    unittest.main()
