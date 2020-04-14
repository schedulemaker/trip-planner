from googlemaps import Client as GoogleMaps
import pandas as pd

# src_addr and dst_addr is a string form of an address. e.g. "Temple University", "Temple University Tech Center", etc.
def getLatLng(src_addr,dst_addr, gmaps):
    
# Run geocode API to get lat and lng info 
    src_geocode = gmaps.geocode(src_addr)
    dst_geocode = gmaps.geocode(dst_addr)
    
    # Extract Lat and Lng info from geocode result
    srcLat = src_geocode[0]['geometry']['location']['lat']
    srcLng = src_geocode[0]['geometry']['location']['lng']
    
    dstLat = dst_geocode[0]['geometry']['location']['lat']
    dstLng = dst_geocode[0]['geometry']['location']['lng']
    
    src = (srcLat, srcLng)
    dst = (dstLat,dstLng)
    
    # Using distance API to find distance
    result = gmaps.distance_matrix(src, dst, mode='driving')
    distance = result['rows'][0]['elements'][0]['distance']
    duration = result['rows'][0]['elements'][0]['duration']
    #dist_dur = {'src_geocode': src_geocode, 'dst_geocode':dst_geocode,'result':result,'distance': distance,'duration': duration}
    dist_dur = [distance, duration]
    
    return dist_dur

def main():
    keyfile = "MAP_KEY"
    MAP_KEY = ''
    
    # Get API key from a file
    try:
        with open(keyfile, 'r+') as fh:
            MAP_KEY = fh.readline()
    except FileNotFoundError:
        print('API key file does not exist. Exit the program.')
        exit()
        
    # Create gmaps
    try:
        gmaps = GoogleMaps(MAP_KEY)
    except ValueError:
        print('Invalid API key provided. Exit the program.')
        exit()
    
    # Get src_addr and dst_addr. Currently hardcoded. Need to be changed.
    src_addr = 'temple university' 
    dst_addr = 'temple university ambler campus Learning Center Parking Lot'
    
    # Get distance and duration of src_addr and dst_addr
    # return format examples: {'text': '25.3 km', 'value': 25318}, {'text': '25.3 km', 'value': 25318}
    distance, duration = getLatLng(src_addr,dst_addr, gmaps)
    print(distance)
    print(duration)
    
    
    """
    TODO:
    1. decide where to get src_addr and dst_addr? (currently, it is hard-coded.)
    2. todo: cache
    3. todo: update schedule based on trip-planner
    """
    

if __name__ == "__main__":
    main()
















    

