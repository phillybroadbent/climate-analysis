"""Functions for converting imperial to metric"""

def inches_to_mm(inches):
    """Converts rainfall in inches to mm
    
    Arguments
        inches: rainfall in inches
        
    Returns:
        mm: rainfall in millimetres
    """
    mm = inches * 25.4
    return mm

