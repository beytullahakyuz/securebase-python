import dearpygui.dearpygui as dp

def blue_button_theme():
    with dp.theme() as blue_button:
        with dp.theme_component(dp.mvButton):
            dp.add_theme_color(dp.mvThemeCol_Button, (50, 150, 250, 255))
            dp.add_theme_color(dp.mvThemeCol_ButtonHovered, (30, 120, 220, 255))
            dp.add_theme_color(dp.mvThemeCol_ButtonActive, (20, 100, 200, 255))
            dp.add_theme_style(dp.mvStyleVar_FrameRounding, 10)
            dp.add_theme_style(dp.mvStyleVar_FramePadding, 5, 5)
    return blue_button

def green_button_theme():
    with dp.theme() as blue_button:
        with dp.theme_component(dp.mvButton):
            dp.add_theme_color(dp.mvThemeCol_Button, (66, 159, 70, 255))
            dp.add_theme_color(dp.mvThemeCol_ButtonHovered, (56, 142, 60, 255))
            dp.add_theme_color(dp.mvThemeCol_ButtonActive, (46, 125, 50, 255))
            dp.add_theme_style(dp.mvStyleVar_FrameRounding, 10)
            dp.add_theme_style(dp.mvStyleVar_FramePadding, 5, 5)
    return blue_button