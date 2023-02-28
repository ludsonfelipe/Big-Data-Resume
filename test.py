import gradio as gr
from comtypes import CLSCTX_ALL
from comtypes import cast
from comtypes import POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import comtypes
import pyautogui
import os

def pause():
    pyautogui.press('space')

def desliga_pc():
    os.system('shutdown /l')

def volume(variavel, pause_video, os):
    # Get default audio device using PyCAW
    print(variavel)
    comtypes.CoInitialize()
    devices = AudioUtilities.GetSpeakers()

    if devices:
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        
        # Set volume to 50% (0.5)
        volume.SetMasterVolumeLevel(variavel, None)
    else:
        print("No audio devices found.")
    
    if pause_video==True:
        pause()
    
    if os==True:
        desliga_pc()
        return 'Desligou'


# Create the Gradio interface
inputs = gr.inputs.Slider(minimum=-50, maximum=-1, step=-1, default=-20, label="Volume Level")
outputs = gr.outputs.Textbox(label="Status")

pause_video = gr.inputs.Checkbox(label='Pausa o video')
unpause = gr.outputs.Textbox(label='Pausou')

os_input = gr.inputs.Checkbox(label='Desliga o PC')
os_return = gr.outputs.Textbox(label='Desligou')


# Run the app
iface = gr.Interface(fn=volume, inputs=[inputs, pause_video, os_input], outputs=[outputs, unpause, os_return], title="Adjust Volume", layout="vertical")
iface.launch(share=True)