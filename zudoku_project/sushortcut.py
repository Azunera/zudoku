import os
import win32com.client

def create_shortcut():
    desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    shortcut_path = os.path.join(desktop, "zudoku.lnk")
    target = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sudoku.exe")

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = target
    shortcut.WorkingDirectory = os.path.dirname(target)

    # Set a standard icon from shell32.dll (index 42 for example)
    shortcut.IconLocation = "shell32.dll, 42"

    shortcut.save()

if __name__ == "__main__":
    create_shortcut()
