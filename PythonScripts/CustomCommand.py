#------------------------------------------------------------------------
import N10X

#------------------------------------------------------------------------
def ToggleBuildPanelOrBuild():
    open = N10X.Editor.IsBuildPanelOpen()
    if open:
        N10X.Editor.ExecuteCommand("CloseBuildPanel")
    else:
        N10X.Editor.ExecuteCommand("BuildActiveWorkspace")