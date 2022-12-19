class IModelChanger:
    """
    interface IModelChanger
    Method:
        notify_changer:
            notifies about changes in model
    """
    def notify_change(self, sender: 'IModelChanger'):
        pass
