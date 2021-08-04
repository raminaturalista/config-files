#Librerías

import os
import subprocess

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, extension, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# Definición de variables generales (mod, terminal)

mod = "mod4"
mod1 = "alt"
mod2 = "control"
terminal = guess_terminal()

# Ventanas

keys = [
    
    # Cambio entre ventanas en un mismo espacio de trabajo
    
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

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
    Key([mod], "m", lazy.spawn("rofi -show run")),
    Key([mod], "t", lazy.spawn("mousepad")),
    Key([mod], "c", lazy.spawn("thunderbird")),
    Key([mod], "r", lazy.spawn("/usr/bin/rstudio-bin %F")),

        
    ]

# Grupos

__groups = {
    1: Group("term"),
    2: Group("web", matches=[Match(wm_class=["firefox"])]),
    3: Group("dev"),
    4: Group("doc"),
    5: Group("mail", matches=[Match(wm_class=["thunderbird"])]),
    6: Group("dir", matches=[Match(wm_class=["nemo"])]),
    7: Group("game"),
    8: Group("vlc"),
    9: Group("off"),
    0: Group("moc")
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


# Layouts

layouts = [
    # layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    layout.MonadTall(
        margin = 5,
        single_margin=8,
        border_normal="#2b303b",
        border_focus="#ebcb8b",
        border_width=3,
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
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
    font='JetBrains Mono Medium',
    fontsize=12,
    padding=6,
    background=colors[0],
)

extension_defaults = widget_defaults.copy()

# Widgets :: Listado completo

screens = [
    Screen(
        top=bar.Bar(
            [


                
                # widget.CurrentLayoutIcon(scale=0.8, padding=6,),


                widget.GroupBox(
                block_highlight_text_color=colors[9],
                rounded=False,
                highlight_method='block',
                this_current_screen_border=colors[8],
                inactive=colors[1],
                active=colors[9],
                urgent_border=colors[5],
                # urgent_text=colors[6],
                ),

                # widget.WindowName(),

                widget.Prompt(
                    prompt="$ :: "
                ),
                # widget.WindowName(),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Spacer (),
                widget.Systray(),
                
                # Separador power line

                widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[0],
                       padding = 0,
                       fontsize = 20,
                       ),

                # widget.Wlan(interface="wlp1s0", format="{essid}"),

                # Separador power line

                widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[4],
                       padding = -1,
                       fontsize = 58
                       ),

                widget.Volume(
                    background=colors[4],
                ),

                # Separador power line

                widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = -1,
                       fontsize = 58
                       ),

                # Reloj
                
                widget.Clock(
                    background=colors[5],
                    foreground=colors[9],
                    format='%I:%M %p'),
                
                # Notificaciones

                widget.Notify(),


                # Separador power line

                widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[6],
                       padding = -1,
                       fontsize = 58
                       ),

                       
                # MOC

                widget.Moc(
                    background=colors[6],
                    play_color=colors[0],
                    no_play_color=colors[0],
                ),
                
                # Separador power line

                widget.TextBox(
                       text = '',
                       background = colors[6],
                       foreground = colors[7],
                       padding = -1,
                       fontsize = 58
                       ),
                
                # Batería

                widget.Battery (
                    charge_char="+",
                    discharge_char="-",
                    format='{char} {percent:2.0%} ',
                    background=colors[7],
                    foreground=colors[9],
                    show_short_text=False,
                    ),
                
                # Separador power line

                widget.TextBox(
                       text = '',
                       background = colors[7],
                       foreground = colors[8],
                       padding = -1,
                       fontsize = 58
                       ),
                
                # Salir

                widget.QuickExit(
                    background=colors[8], 
                    foreground=colors[9],
                    default_text='cerrar ',
                    countdown_format='[ {} ]'),
            ], # Widgets
            24, # Ancho
        opacity=0.9), # Opacidad
    ), # Screen
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


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

autostart = [
        "nitrogen --restore",
        "picom --no-vsync &",
        "nm-applet &",
        # "volumeicon &",
]

for x in autostart:
    os.system(x)
