#------------------------------------------------------------------------
import N10X

#------------------------------------------------------------------------
# Open the current file in Visual Studio
# For documentation on ExecuteVSCommand see EnvDTE.ExecuteCommand on MSDN
def OpenInVS():
    file = N10X.Editor.GetCurrentFilename()
    if file:
        N10X.Editor.ExecuteVSCommand("Edit.GoTo", str(N10X.Editor.GetCursorPos()[1] + 1))

