import string
import secrets

#パスワードを生成する関数
def Create_pass(length):
    n_pass = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(n_pass) for x in range(length))
    return password

c_number = 10 #パスワードの生成回数
length = 12 #パスワードの長さ

#長さlengthのパスワードをc_number回表示する。
for x in range(c_number):
    one_pass = Create_pass(length)
    print(one_pass)
    