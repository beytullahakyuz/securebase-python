## TR

SecureBase kütüphanesi standart base64 algoritmasına ek olarak gizli anahtar seçeneği sunmaktadır. Böylelikle kütüphaneyi kullanan projelere özgü base64 işlemi gerçekleşir. Her projenin gizli anahtarı farklı olacağından oluşan base64 çıktısıda gizli anahtara bağlı olarak değişir.

Detaylı bilgi için aşağıdaki kaynağı inceleyiniz.

[SecureBase Wiki](https://beytullahakyuz.gitbook.io/securebase)

## Kullanım/Örnek

```python
from SecureBase import SecureBase, SBEncoding
#enc = SBEncoding.UNICODE
enc = SBEncoding.UTF8
sb = SecureBase(encoding=enc)
sb.set_secret_key("set-secret-key")

#Text to Base64
encoded = sb.encode(inputdata)

#Base64 to Text
decoded = sb.decode(inputdata)
```

## EN

The SecureBase library offers a secret key option in addition to the standard base64 algorithm. Since the secret key will be different in each project, the base64 output will also vary depending on the secret key.

For detailed information, please review the source below.

[SecureBase Wiki](https://beytullahakyuz.gitbook.io/securebase)

## Using/Example

```python
from SecureBase import SecureBase, SBEncoding
#enc = SBEncoding.UNICODE
enc = SBEncoding.UTF8
sb = SecureBase(encoding=enc)
sb.set_secret_key("set-secret-key")

#Text to Base64
encoded = sb.encode(inputdata)

#Base64 to Text
decoded = sb.decode(inputdata)
```