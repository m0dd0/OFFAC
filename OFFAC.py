import logging
import adsk.core, adsk.fusion, traceback

handlers = []
cmd = None
ctrl = None
ui = None


class MyCreatedHandler(adsk.core.CommandCreatedEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args: adsk.core.CommandCreatedEventArgs):
        print("started MyCreatedHandler")
        try:
            myInputChangedHandler = MyInputChangedHandler()
            handlers.append(myInputChangedHandler)
            args.command.inputChanged.add(myInputChangedHandler)

            myExecuteHandler = MyExecuteHandler()
            handlers.append(myExecuteHandler)
            args.command.execute.add(myExecuteHandler)

            args.command.commandInputs.addBoolValueInput(
                "MyAddinBoolInputId", "bool input", True
            )
        except:
            if ui:
                ui.messageBox(traceback.format_exc())


class MyInputChangedHandler(adsk.core.InputChangedEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args):
        print("started MyInputChangedHandler")
        try:
            command = args.firingEvent.sender
            cmdInput = args.input

        except:
            if ui:
                ui.messageBox(traceback.format_exc())


class MyExecuteHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args):
        print("started MyExecuteHandler")
        try:
            command = args.firingEvent.sender

        except:
            if ui:
                ui.messageBox(traceback.format_exc())


def run(context):
    try:
        global ui
        global cmd
        global ctrl

        app: adsk.core.Application = adsk.core.Application.get()
        ui = app.userInterface

        ws = ui.workspaces.itemById("FusionSolidEnvironment")
        tab = ws.toolbarTabs.itemById("ToolsTab")
        panel = tab.toolbarPanels.itemById("SolidScriptsAddinsPanel")
        cmd = ui.commandDefinitions.addButtonDefinition(
            "verycustomcommandid", "my command", ""
        )
        ctrl = panel.controls.addCommand(cmd)

        onCreated = MyCreatedHandler()
        cmd.commandCreated.add(onCreated)
        handlers.append(onCreated)

    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))


def stop(context):
    try:
        global cmd
        global ctrl

        ctrl.deleteMe()
        cmd.deleteMe()
    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))
