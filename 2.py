import pandas as pd
from seal import EncryptionParameters, SEALContext, KeyGenerator, Encryptor, BatchEncoder, Plaintext, Ciphertext, scheme_type, CoeffModulus, Decryptor, Evaluator

# データセットの読み込み
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
data = pd.read_csv(url, names=columns, na_values=" ?", skipinitialspace=True)

# 年齢データの抽出
ages = data['age'].dropna().tolist()

# 暗号化パラメータの設定
parms = EncryptionParameters(scheme_type.BFV)
poly_modulus_degree = 8192
parms.set_poly_modulus_degree(poly_modulus_degree)
parms.set_coeff_modulus(CoeffModulus.BFVDefault(poly_modulus_degree))
parms.set_plain_modulus(256)

context = SEALContext.Create(parms)
keygen = KeyGenerator(context)
public_key = keygen.public_key()
secret_key = keygen.secret_key()

encoder = BatchEncoder(context)
encryptor = Encryptor(context, public_key)
decryptor = Decryptor(context, secret_key)
evaluator = Evaluator(context)

# 年齢データの暗号化
batch_size = encoder.slot_count()
plain = Plaintext()
cipher = Ciphertext()

# 平均年齢計算のための準備
total_sum = Ciphertext()
encryptor.encrypt(encoder.encode([0] * batch_size), total_sum)

for age in ages:
    plain = Plaintext()
    encoder.encode([age] * batch_size, plain)
    encryptor.encrypt(plain, cipher)
    evaluator.add_inplace(total_sum, cipher)

# 平均の計算（クライアント側で復号化するため、ここでは平均の計算を完了しません）
plain_result = Plaintext()
decryptor.decrypt(total_sum, plain_result)
sum_result = encoder.decode_int64(plain_result)[0]
average_age = sum_result / len(ages)

print("Average age:", average_age)

# PyDPを使用して差分プライバシを適用
from pydp.algorithms.laplacian import BoundedMean

dp_ages = BoundedMean(epsilon=1.0, lower_bound=0, upper_bound=120)
dp_ages.add_entry(average_age)
private_average_age = dp_ages.result()

print("Private average age:", private_average_age)
