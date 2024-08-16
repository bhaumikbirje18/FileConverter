from nicegui import ui
from utils import fileflip_utils,Path
import psutil

utils = fileflip_utils()
process_names = [proc.name() for proc in psutil.process_iter()]
    
if Path(f"{Path.cwd()}/temp_files/input").exists() and Path(f"{Path.cwd()}/temp_files/output").exists():
     pass
else:
     Path(f"{Path.cwd()}/temp_files/input").mkdir(parents=True)
     Path(f"{Path.cwd()}/temp_files/output").mkdir(parents=True)

@ui.page('/')
def upload_ui():
    utils.render_upload_ui()

@ui.page('/convert')
def file_conversion_ui():
    utils.render_conversion_ui()

@ui.page('/download')
def download_ui():
    utils.render_download_ui()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(favicon=f"{Path.cwd()}/static/logo.ico")