from gmssl import sm2

# 生成密钥对
private_key = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D'
public_key = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'

sm2_crypt = sm2.CryptSM2(
    public_key=public_key, private_key=private_key)
data = b"Hello, SM2!"
# 加密
enc_data = sm2_crypt.encrypt(data)
# 解密
dec_data = sm2_crypt.decrypt(enc_data)

print(f"原始数据: {data}")
print(f"加密后的数据: {enc_data.hex()}")
print(f"解密后的数据: {dec_data}")

"""
拉卡拉账号:djiwsd@lakala.com 密码:fjkwJKs=23
邦得数字账号:bangdeng234 密码:jerjiod334@#
user:jkewe@lakala.com pass:sdkke@304
user:dfjke@bonddigit.com pass:erl3934#
user:jower@kinorsoft.com pass:wejk3*3
"""

# # 签名和验证
# random_hex_str = sm2_crypt.get_random_hex_str(sm2_crypt.para_len)
# sign = sm2_crypt.sign(data, random_hex_str)
# verify = sm2_crypt.verify(sign, data)
# print(f"签名: {sign}")
# print(f"验证结果: {verify}")
