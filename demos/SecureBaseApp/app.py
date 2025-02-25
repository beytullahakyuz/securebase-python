import dearpygui.dearpygui as dpg
from SecureBase import SecureBase, SBEncoding
from dearpygui.dearpygui import maximize_viewport

import functions as fnc
import themes as theme

dpg.create_context()

with dpg.window(tag="winmain", label="SecureBaseApp", menubar=True, no_resize=True, width=480, height=525):
    with dpg.menu_bar():
        with dpg.menu(label="Dil", tag="mlang"):
            dpg.add_menu_item(label="TR", callback=fnc.menuClicked, tag="mTurkish")
            dpg.add_menu_item(label="EN", callback=fnc.menuClicked, tag="mEnglish")

    with dpg.group(horizontal=True, height=50):
        dpg.add_text("Gizli anahtar:", color=(0, 229, 255, 255), tag="lblsecretkey")
        dpg.add_input_text(tag="secretkey", width=240)
        dpg.add_combo(["unicode", "utf-8"], tag="cmbencoding", use_internal_label=False, width=75)
    dpg.add_spacer(height=5)

    with dpg.tab_bar():
        with dpg.tab(label="Kodlama", tag="page_encode"):
            dpg.add_text(default_value="Veri;", tag="enc_lbldata")
            dpg.add_input_text(tag="enc_inputdata", height=100, width=400, multiline=True, no_horizontal_scroll=False)
            dpg.add_text(default_value="Base64;", tag="enc_lblbase64")
            dpg.add_input_text(tag="enc_inputbase64", height=100, width=400, multiline=True, no_horizontal_scroll=False)
            dpg.add_spacer(height=5)
            btn1 = dpg.add_button(label="Kodlama", width=400, height=25, tag="btnEncode", callback=fnc.btnClicked)
            dpg.bind_item_theme(btn1, theme.blue_button_theme())

        with dpg.tab(label="Kodlama çözme", tag="page_decode"):
            dpg.add_text(default_value="Base64;", tag="dec_lblbase64")
            dpg.add_input_text(tag="dec_inputbase64", height=100, width=400, multiline=True, no_horizontal_scroll=False)
            dpg.add_text(default_value="Veri;", tag="dec_lbldata")
            dpg.add_input_text(tag="dec_resultdata", height=100, width=400, multiline=True, no_horizontal_scroll=False)
            dpg.add_spacer(height=5)
            btn1 = dpg.add_button(label="Kodlama çözme", width=400, height=25, tag="btnDecode", callback=fnc.btnClicked)
            dpg.bind_item_theme(btn1, theme.green_button_theme())

with dpg.font_registry():
    font = dpg.add_font("roboto-regular.ttf", 14)
dpg.bind_font(font)

dpg.create_viewport(title="SecureBaseApp #python", width=435, height=430, resizable=False)
dpg.set_viewport_resizable(False)

dpg.set_primary_window("winmain", value=True)
dpg.set_value("cmbencoding", "utf-8")
fnc.changeLang("mEnglish")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()