import os
import N10X
from Vim import * 

#------------------------------------------------------------------------
# VimUser - Comes with handlers to override default Vim bindings.
# Designed to be edited locally so users can avoid having to merge Vim.py
#------------------------------------------------------------------------

g_PaneSwap = False

"""
Key handler for command mode
"""
def UserHandleCommandModeKey(key: Key) -> UserHandledResult:
    global g_PaneSwap

    #
    # Testing/Examples
    #
    do_test = False
    if do_test:
        # Testing - pass ctrl+h back to 10x to open find and replace.
        if key == Key("H", control=True):
            return UserHandledResult.PASS_TO_10X
        
        # Testing - handle ctrl+u and print Hello World
        if key == Key("U", control=True):
            print("Hello World")
            return UserHandledResult.HANDLED

    #
    # Add own keybindings below
    #
    if key == Key("W", control=True):
        g_PaneSwap = True
        return UserHandledResult.HANDLED

    elif key == Key("H", control=True):
        if g_PaneSwap:
            N10X.Editor.ExecuteCommand("MovePanelFocusLeft")
            g_PaneSwap = False 
        else: 
            MoveToWordStart()
        return UserHandledResult.HANDLED

    elif key == Key("L", control=True):
        if g_PaneSwap: 
            N10X.Editor.ExecuteCommand("MovePanelFocusRight")
            g_PaneSwap = False
        else: 
            MoveToNextWordStart()
        return UserHandledResult.HANDLED

    elif key == Key("J", control=True):
        if g_PaneSwap: 
            N10X.Editor.ExecuteCommand("MovePanelFocusDown")
            g_PaneSwap = False
        else:
            MoveToNextParagraphEnd()
        return UserHandledResult.HANDLED
        
    elif key == Key("K", control=True):
        if g_PaneSwap: 
            N10X.Editor.ExecuteCommand("MovePanelFocusUp")
            g_PaneSwap = False
        else:
            MoveToPreviousParagraphBegin()
        return UserHandledResult.HANDLED

    elif key == Key("B", control=True):
        MoveToStartOfLine()
        return UserHandledResult.HANDLED

    elif key == Key("E", control=True):
        MoveToEndOfLine()
        return UserHandledResult.HANDLED

    #elif key == Key(":") or key == Key(";"):
    #    N10X.Editor.ExecuteCommand("ShowCommandPanel")
    #    N10X.Editor.SetCommandPanelText(":")
    #    return UserHandledResult.HANDLED

    elif key == Key("S", control=True):
        SaveFileAndFormat()
        return UserHandledResult.HANDLED

    elif key.key != "Control":
        # Reset pane swap only if next key was not just control
        g_PaneSwap = False

    # Default - do nothing
    return UserHandledResult.UNHANDLED

"""
Key handler for insert mode
"""
def UserHandleInsertModeKey(key: Key) -> UserHandledResult:
    global g_ExitInsertMode

    #
    # Testing/Examples
    #
    do_test = False
    if do_test:
        # Testing - pass ctrl+z back to 10x to undo
        if key == Key("v", control=True):
            return UserHandledResult.PASS_TO_10X

    #
    # Add own keybindings below
    #

    # Default - do nothing
    return UserHandledResult.UNHANDLED


"""
Command handler for commandline mode, e.g. :q, :w, etc.
"""
def UserHandleCommandline(command) -> UserHandledResult:

    #
    # Testing/Examples
    #
    do_test = False
    if do_test:
        # Testing - print current filename.
        if command == ":filename":
            print(N10X.Editor.GetCurrentFilename())
            return UserHandledResult.HANDLED
        
        # Testing - print Hello World
        if command == ":hello":
            print("Hello World")
            return UserHandledResult.HANDLED

    #
    # Add own commands below
    #
    if command == ":w" or command == ":W":
        SaveFileAndFormat()
        return UserHandledResult.HANDLED
        
    elif command == ":q!" or command == ":x!":
        N10X.Editor.ExecuteCommand("CloseAllTabs")
        #N10X.Editor.ExecuteCommand("CloseFile")
        
        return UserHandledResult.HANDLED


    # Default - do nothing
    return UserHandledResult.UNHANDLED

def SaveFileAndFormat():
    file_name = N10X.Editor.GetCurrentFilename()
    file_name, file_extension = os.path.splitext(file_name)

    handle_extension = [".h", ".cpp", ".c", ".cs"]
    if file_extension in handle_extension:
        N10X.Editor.ExecuteCommand("ClangFormatFile")

    N10X.Editor.ExecuteCommand("SaveFile")