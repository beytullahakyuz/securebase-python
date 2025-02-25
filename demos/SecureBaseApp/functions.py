import dearpygui.dearpygui as dp
from SecureBase import SecureBase, SBEncoding

def btnClicked(sender, app_data):
    encodingstr = dp.get_value("cmbencoding")
    enc = SBEncoding.UTF8
    if (encodingstr == "unicode"):
        enc = SBEncoding.UNICODE
    else:
        enc = SBEncoding.UTF8
    sb = SecureBase(encoding=enc)
    secretkey = dp.get_value("secretkey")
    sb.set_secret_key(secretkey)
    if (sender == "btnEncode"):
        inputdata = dp.get_value("enc_inputdata")
        print("input data; \r\n" + inputdata)
        encoded = sb.encode(inputdata)
        dp.set_value("enc_inputbase64", encoded)
        print("encoded; \r\n" + encoded)
    if (sender == "btnDecode"):
        inputdata = dp.get_value("dec_inputbase64")
        print("input data; \r\n" + inputdata)
        decoded = sb.decode(inputdata)
        dp.set_value("dec_resultdata", decoded)
        print("decoded; \r\n" + decoded)
    print("------------------------------------------")

def changeLang(lang):
    if lang == "mTurkish":
        dp.set_item_label("mlang", "Dil")
        dp.set_value("enc_lbldata", "Veri;")
        dp.set_value("dec_lbldata", "Veri;")
        dp.set_value("lblsecretkey", "Gizli anahtar:")
        dp.set_item_label("btnEncode", "Kodlama")
        dp.set_item_label("btnDecode", "Kodlama çözme")
        dp.set_item_label("page_encode", "Kodlama")
        dp.set_item_label("page_decode", "Kod çözme")
    else:
        dp.set_item_label("mlang", "Language")
        dp.set_value("enc_lbldata", "Data;")
        dp.set_value("dec_lbldata", "Data;")
        dp.set_value("lblsecretkey", "Secret key:")
        dp.set_item_label("btnEncode", "Encode")
        dp.set_item_label("btnDecode", "Decode")
        dp.set_item_label("page_encode", "Encoding")
        dp.set_item_label("page_decode", "Decoding")

def menuClicked(sender, app_data, user_data):
    changeLang(sender)