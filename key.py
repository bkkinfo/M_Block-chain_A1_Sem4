from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import hashlib
def generate_keys():
    private = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )    
    public = private.public_key()
    return private, public

private, public = generate_keys()
private_, public_ = generate_keys()

pub_der = public.public_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)
pub_der_ = public_.public_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

print(hashlib.sha1(pub_der).hexdigest())
print(hashlib.sha1(pub_der_).hexdigest())