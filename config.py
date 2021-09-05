#Librerías

import os
import subprocess

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, extension, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# from libqtile.utils import guess_terminal

# Definición de variables generales (mod, terminal)

mod = "mod4"
# mod1 = "alt"
mod2 = "control"
terminal = "xfce4-terminal" # guess_terminal()

#Colores

colors = [["#2b303b", "#2b303b"], # 0. Negro
          ["#65737e", "#65737e"], # 1. Gris
          ["#c0c5ce", "#c0c5ce"], # 2. Blanco
          ["#bf616a", "#bf616a"], # 3. Rojo
          ["#a3be8c", "#a3be8c"], # 4. Verde
          ["#ebcb8b", "#ebcb8b"], # 5. Amarillo
          ["#8fa1b3", "#8fa1b3"], # 6. Azul
          ["#b48ead", "#b48ead"], # 7. Magenta
          ["#96b5b4", "#96b5b4"], # 8. Cyan
          ["#ffffff", "#ffffff"]] # 9. Blanco 100%

# Ventanas

keys = [
    
    # Cambio entre ventanas en un mismo espacio de trabajo
    
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Mover ventanas en un espacio de trabajo

    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Cambiar tamaño de las ventanas

    Key([mod], "o", lazy.layout.grow()),
    Key([mod], "i", lazy.layout.shrink()),
    #Key([mod], "=", lazy.layout.normalize()),
    #Key([mod], ">", lazy.layout.maximize()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    
    
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "p", lazy.spawncmd()),
    
    # Lanzadores de apps

    Key([mod], "v", lazy.spawn("/opt/visual-studio-code/code --no-sandbox --unity-launch")),
    Key([mod], "f", lazy.spawn("firefox")),
    Key([mod], "b", lazy.spawn("brave")),
    Key([mod], "e", lazy.spawn("nemo")),
    Key([mod], "m", lazy.spawn(
        "dmenu_run -p '$ :: ' -l 50 -fn 'JetBrains Mono SemiBold-12' -nb '#2b303b' -sb '#bf616a' -sf '#2b303b' -nf '#c0c5ce'")),
    Key([mod], "t", lazy.spawn("mousepad")),
    Key([mod], "c", lazy.spawn("mailspring")),
    Key([mod], "r", lazy.spawn("/usr/bin/rstudio-bin")),
    Key([mod], "g", lazy.spawn("/usr/bin/steam-runtime")),
    Key([mod], "w", lazy.spawn("rofi -show window")),
        
    ]

# Grupos

__groups = {
    1: Group("  "),
    2: Group(" 爵 ", matches=[Match(wm_class=["firefox", "brave-browser"])]),
    3: Group("  ", matches=[Match(wm_class=["code", "rstudio"])]),
    4: Group("  ", matches=[Match(wm_class=["foxitreader"])]),
    5: Group("  ", matches=[Match(wm_class=["mailspring"])]),
    6: Group("  ", matches=[Match(wm_class=["nemo"])]),
    7: Group("  "),
    8: Group("  ", matches=[Match(wm_class=["vlc"])]),
    9: Group("  "),
    0: Group("  ")
}
groups = [__groups[i] for i in __groups]


def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]


for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1+shift+letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(get_group_key(i.name)),
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])


# Layouts

layouts = [
    # layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    layout.MonadTall(
        margin = 8,
        single_margin=8,
        border_normal="#2b303b",
        border_focus="#ebcb8b",
        border_width=3,
    ),
    layout.Max(),
    layout.Floating(
        border_normal="#2b303b",
        border_focus="#ebcb8b",
        border_width=3,

    ),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Widgets :: default settings

widget_defaults = dict(
    font='JetBrainsMono Nerd Font Semibold',
    fontsize=11,
    padding=6,
    background=colors[0],
)

extension_defaults = widget_defaults.copy()

# Widgets :: Listado completo

screens = [
    Screen(
        top=bar.Bar(
            [

                widget.GroupBox(
                font = 'JetBrainsMono Nerd Font',
                fontsize = 15, 
                padding=2,
                block_highlight_text_color=colors[9],
                rounded=True,
                highlight_method='block',
                this_current_screen_border=colors[3],
                inactive=colors[1],
                active=colors[9],
                urgent_border=colors[5],
                # urgent_text=colors[6],
                ),

                widget.Spacer (),

                widget.Systray(),

                widget.TextBox(
                       text = '',
                       # font = 'JetBrainsMono Nerd Font Regular',
                       background = colors[0],
                       foreground = colors[0],
                       padding = -5,
                       fontsize = 44
                       ),
                              
                # Separador power line

                widget.TextBox(
                       text = '',
                       # font = 'JetBrainsMono Nerd Font Regular',
                       background = colors[0],
                       foreground = colors[4],
                       padding = -5,
                       fontsize = 44
                       ),

                # Volumen

                widget.TextBox(
                    text='',
                    fontsize=18,
                    background = colors[4],
                    foreground = colors[0],

                ),

                widget.Volume(
                    background = colors[4],
                    foreground = colors[0],
                    padding=10,
                ),

                # Separador power line
                
                widget.TextBox(
                       text = '',
                       # font = 'JetBrainsMono Nerd Font Regular',
                       background = colors[4],
                       foreground = colors[5],
                       padding = -5,
                       fontsize = 42
                       ),

                # Ícono del reloj

                widget.TextBox(
                    background=colors[5],
                    foreground=colors[0],
                    text="",
                    fontsize=18,
                ),
                
                # Reloj
                
                widget.Clock(
                    background=colors[5],
                    foreground = colors[0],
                    format='%a %d-%m %H:%M'),
                
                # Separador power line

                widget.TextBox(
                       text = '',
                       # font = 'JetBrainsMono Nerd Font Regular',
                       background = colors[5],
                       foreground = colors[6],
                       padding = -5,
                       fontsize = 42
                       ),

                       
                # MOC

                widget.Moc(
                    background=colors[6],
                    foreground = colors[0],
                    play_color=colors[0],
                    no_play_color=colors[0],
                    ),
                
                # Separador power line
                
                widget.TextBox(
                       text = '',
                       # font = 'JetBrainsMono Nerd Font Regular',
                       background = colors[6],
                       foreground = colors[7],
                       padding = -5,
                       fontsize = 42
                       ),

                # Batería

                widget.Battery (
                    charge_char="+",
                    discharge_char="-",
                    format='{char} {percent:2.0%} ',
                    background=colors[7],
                    foreground = colors[0],
                    show_short_text=False,
                    low_foreground = colors [9],
                    ),
                
                # Separador power line
                                
                widget.TextBox(
                       text = '',
                       # font = 'JetBrainsMono Nerd Font Regular',
                       background = colors[7],
                       foreground = colors[3],
                       padding = -5,
                       fontsize = 42
                       ),



                widget.CurrentLayout(
                       background = colors[3],
                       foreground = colors[0],
                       ),

                # Separador power line
                
                widget.TextBox(
                       text = '',
                       # font = 'JetBrainsMono Nerd Font Regular',
                       background = colors[3],
                       foreground = colors[8],
                       padding = -5,
                       fontsize = 42
                       ),

                # Salir

                widget.QuickExit(
                    background=colors[8], 
                    foreground = colors[0],
                    default_text='',
                    countdown_format='{}',
                    padding=12,
                    ),
            ], # Fin de los widgets
            28, # Ancho
            # margin=[8, 8, 2, 8], # Margen NESW
            opacity=0.95 # Opacidad            
            ) # Fin de la configuración de la barra
        
        ), # Fin de esta pantalla
    # Screen (), 
    
] # Screens

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# Nombre del gestor de ventanas

wmname = "Qtile"

autostart = [
        "nitrogen --restore",
        "picom --no-vsync &",
        "nm-applet &",
        "blueberry-tray",
        "numlockx",
        # "systemctl enable bluetooth",
        # "volumeicon &",
]

for x in autostart:
    os.system(x)