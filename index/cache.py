def exports():
    local = locals()
    globa = globals()

    if 'distdurCache' not in local and 'distdurCache' not in globa:
        distdurCache = {}
    if 'os' not in local and 'os' not in globa:
        import os
    if 'GoogleMaps' not in local and 'GoogleMaps' not in globa:
        from googlemaps import Client as GoogleMaps
    if 'pd' not in local and 'pd' not in globa:
        import pandas as pd


    return distdurCache, os, GoogleMaps, pd
