
def add_proj(nc_obj, epsg, nc_to_copy):
    """
    Adds the projection using two different methods. One from an internet
    source using the epsg value and the other from an existing file containing
    it.
    Args:
        nc_obj: netCDF4 dataset object needing the projection information
        nc_to_copy: netcdf obj or path that has desired projection information

    Returns:
        nc_obj: Original nc_bj plus the projection information
    """
    try:
        map_meta = add_proj_from_web(epsg)
    except:
        print("Failed to get projection info from the internet...\n"
        "Using a local netcdf to determine the projection...")
        map_meta = add_proj_from_file(nc_to_copy)

    # Create a variable called projection
    nc_obj.createVariable("projection","S1")
    nc_obj["projection"].setncatts(map_meta)

    # Adding coordinate system info to
    for name,var in nc_obj.variables.items():
        out.respond(name)
        # Assume all 2D+ vars are the same projection
        if 'x' in var.dimensions and 'y' in var.dimensions:
            nc_obj[name].setncatts({"grid_mapping":"projection"})

        elif name.lower() in ['x','y']:
            # Set a standard name, which is required for recognizing projections
            nc_obj[name].setncatts({"standard_name":"projection_{}_coordinate"
            "".format(name.lower())})

            # Set the units
            nc_obj[name].setncatts({"units":"meters".format(name.lower())})

    return nc_obj


def add_proj_from_file(nc_to_copy):
    """
    Use a netcdf file converted from a tif using gdal to retrieve the projection
    information

    Args:
        nc_to_copy: netcdf obj or path that has desired projection information

    Returns:
        map_meta: dictionary of attributes to add for spatial reference
s    """
    if os.path.isfile(nc_to_copy):
        nc_to_copy = Dataset(nc_to_copy)

    map_meta = parse_wkt(nc_to_copy['transverse_mercator'].getncattr('spatial_ref'))

    return map_meta


def add_proj_from_web(epsg):
    """
    Adds the appropriate attributes to the netcdf for managing projection info

    Args:
        epsg:   projection information to be added

    Returns:
        map_meta: dictionary of attributes to add for spatial reference
    """
    #Retrieving projection information...
    # function to generate .prj file information using spatialreference.org
    # access projection information
    try:
        wkt = urlopen("http://spatialreference.org/ref/epsg/{0}/prettywkt/".format(epsg))
    except:
        wkt = urlopen("http://spatialreference.org/ref/sr-org/{0}/prettywkt/".format(epsg))

    # remove spaces between charachters
    remove_spaces = ((wkt.read()).decode('utf-8')).replace(" ","")

    # Add in the variable for holding coordinate system info
    map_meta = parse_wkt(remove_spaces)

    return map_meta


def parse_wkt(epsg_string):
    """
    Processes the epsg string returned from the URL request.

    Args:
        epsg_str: String received from the epsg request.

    Returns:
        map_meta: dictionary of projection data to be added to the netcdf
    """
    map_meta = {}
    wkt_data = (epsg_string.lower()).split(',')

    # Add more projection parsers here
    if 'utm' in epsg_string.lower():
        map_meta = gather_utm_meta(epsg_string)

    # Projection information to be added
    # for k,v in map_meta.items():
    #     out.respond("{}: {}".format(k,repr(v)))
    return map_meta
