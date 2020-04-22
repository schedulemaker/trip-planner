def exports():
    local = locals()
    globa = globals()

    if 'distdurCache' not in local and 'distdurCache' not in globa:
        distdurCache = {}
    return distdurCache
