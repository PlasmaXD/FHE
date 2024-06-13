
from seal import SEALContext, EncryptionParameters, scheme_type
params = EncryptionParameters(scheme_type.BFV)
context = SEALContext.Create(params)
print("SEAL context:", context)
