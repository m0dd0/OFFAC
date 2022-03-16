import adsk.core, adsk.fusion, traceback

handlers = []
cmd = None
ctrl = None
ui = None


class {{cookiecutter.addin_name|capitalize}}CreatedHandler(adsk.core.CommandCreatedEventHandler):
    def notify(self, eventArgs: adsk.core.CommandCreatedEventArgs):
        print("started {{cookiecutter.addin_name|capitalize}}CreatedHandler")
        try:
            inputChangedHandler = {{cookiecutter.addin_name|capitalize}}InputChangedHandler()
            handlers.append(inputChangedHandler)
            eventArgs.command.inputChanged.add(inputChangedHandler)

            executeHandler = {{cookiecutter.addin_name|capitalize}}ExecuteHandler()
            handlers.append(executeHandler)
            eventArgs.command.execute.add(executeHandler)

            eventArgs.command.commandInputs.addBoolValueInput(
                "{{cookiecutter.addin_name}}BoolInputId", "bool input", True
            )
        except:
            if ui:
                ui.messageBox(traceback.format_exc())


class {{cookiecutter.addin_name|capitalize}}InputChangedHandler(adsk.core.InputChangedEventHandler):
    def notify(self, eventArgs: adsk.core.InputChangedEventArgs):
        print("started {{cookiecutter.addin_name|capitalize}}InputChangedHandler")
        try:
            command = eventArgs.firingEvent.sender
            cmdInput = eventArgs.input

        except:
            if ui:
                ui.messageBox(traceback.format_exc())


class {{cookiecutter.addin_name|capitalize}}ExecuteHandler(adsk.core.CommandEventHandler):
    def notify(self, eventArgs: adsk.core.CommandEventArgs):
        print("started {{cookiecutter.addin_name|capitalize}}ExecuteHandler")
        try:
            command = eventArgs.firingEvent.sender

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
            "{{cookiecutter.addin_name}}commandid", "{{cookiecutter.addin_name}}", ""
        )
        ctrl = panel.controls.addCommand(cmd)

        onCreated = {{cookiecutter.addin_name|capitalize}}CreatedHandler()
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
