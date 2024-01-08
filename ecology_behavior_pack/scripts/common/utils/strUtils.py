def JoinPath(*args):
    # type: (str) -> str
    """将多个路径用 '/' 连接"""
    path = ""
    for arg in args:
        path = arg if path == "" else "{0}/{1}".format(path, arg)
    return path