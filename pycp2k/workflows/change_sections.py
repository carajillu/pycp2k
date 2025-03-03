from pycp2k import CP2K

def parse_list(lines: list):
    """Parse a list of strings into a CP2K object."""
    for line in lines:
        line=line.strip()

def iterate_sections(obj, prefix=""):
    """Recursively iterate over all attributes of a myClass instance."""
    
    for key in obj.__dict__.keys():
        if hasattr(obj.__dict__[key],"__dict__"):
            iterate_sections(obj.__dict__[key])
        elif type(obj.__dict__[key]) is list:
            obj.__dict__[key]=replace_first_item_with_last(obj.__dict__[key])
        else:
            continue
    return obj
        


def replace_first_item_with_last(section: list):
    """Replace the first item in a list with the last item."""
    if len(section) > 1:
       section[0]= section[-1]
       del section[-1]
    return section

def replace_sections(calc: CP2K, new_input: str):
    calc.parse(new_input)
    calc=iterate_sections(calc.CP2K_INPUT)

    
