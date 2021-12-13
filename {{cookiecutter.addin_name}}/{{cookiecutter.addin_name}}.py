import adsk.core, adsk.fusion, traceback

handlers = []
cmd = None
ctrl = None
ui = None


class {{cookiecutter.addin_name|upper}}CreatedHandler(adsk.core.CommandCreatedEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args: adsk.core.CommandCreatedEventArgs):
        print("started {{cookiecutter.addin_name|upper}}CreatedHandler")
        try:
            inputChangedHandler = {{cookiecutter.addin_name|upper}}InputChangedHandler()
            handlers.append(inputChangedHandler)
            args.command.inputChanged.add(inputChangedHandler)

            executeHandler = {{cookiecutter.addin_name|upper}}ExecuteHandler()
            handlers.append(executeHandler)
            args.command.execute.add(executeHandler)

            args.command.commandInputs.addBoolValueInput(
                "{{cookiecutter.addin_name}}BoolInputId", "bool input", True
            )
        except:
            if ui:
                ui.messageBox(traceback.format_exc())


class {{cookiecutter.addin_name|upper}}InputChangedHandler(adsk.core.InputChangedEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args):
        print("started {{cookiecutter.addin_name|upper}}InputChangedHandler")
        try:
            command = args.firingEvent.sender
            cmdInput = args.input

        except:
            if ui:
                ui.messageBox(traceback.format_exc())


class {{cookiecutter.addin_name|upper}}ExecuteHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args):
        print("started {{cookiecutter.addin_name|upper}}ExecuteHandler")
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
            "{{cookiecutter.addin_name}}commandid", "my command", ""
        )
        ctrl = panel.controls.addCommand(cmd)

        onCreated = {{cookiecutter.addin_name|upper}}CreatedHandler()
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
