
def singleton(_class):
    instances = {}
    def get_instance(*args):
        if _class not in instances:
            instances[_class] = _class(*args)
        return instances[_class]
    return get_instance