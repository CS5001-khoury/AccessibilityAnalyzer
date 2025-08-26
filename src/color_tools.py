""" 
Functions to help better understand Red, Green, Blue color values.

Name:
Semester: 
"""

# Constants to avoid magic numbers
GAMMA_THRESHOLD = 0.03928
GAMMA_DIVISOR = 12.92
GAMMA_OFFSET = 0.055
GAMMA_MULTIPLIER = 1.055
GAMMA_EXPONENT = 2.4

# WCAG luminance coefficients
RED_LUMINANCE_COEFFICIENT = 0.2126
GREEN_LUMINANCE_COEFFICIENT = 0.7152
BLUE_LUMINANCE_COEFFICIENT = 0.0722

# Brightness calculation coefficients
RED_BRIGHTNESS_COEFFICIENT = 0.299
GREEN_BRIGHTNESS_COEFFICIENT = 0.587
BLUE_BRIGHTNESS_COEFFICIENT = 0.114

# WCAG contrast standards
WCAG_AA_NORMAL_RATIO = 4.5
WCAG_AA_LARGE_RATIO = 3.0
WCAG_AAA_NORMAL_RATIO = 7.0
WCAG_AAA_LARGE_RATIO = 4.5

# Color value limits
RGB_MIN = 0
RGB_MAX = 255
LUMINANCE_OFFSET = 0.05

# Loop function constants
GRAY_STEP_SIZE = 5
RGB_INCREMENT = 1
MAX_RGB_VALUE = 255

# Colorblindness condition strings
PROTANOPIA = "protanopia"
DEUTERANOPIA = "deuteranopia"
TRITANOPIA = "tritanopia"

# WCAG level strings
WCAG_AA_NORMAL = "AA_NORMAL"
WCAG_AA_LARGE = "AA_LARGE"
WCAG_AAA_NORMAL = "AAA_NORMAL"
WCAG_AAA_LARGE = "AAA_LARGE"


def calculate_luminance(r: int, g: int, b: int) -> float:
    """
    Calculate relative luminance for WCAG contrast calculations.

    Examples:
        >>> round(calculate_luminance(255, 255, 255), 3)
        1.0
        >>> round(calculate_luminance(0, 0, 0), 3)
        0.0
        >>> round(calculate_luminance(128, 128, 128), 3)
        0.216

    Arguments:
        r (int): Red component (0-255)
        g (int): Green component (0-255)
        b (int): Blue component (0-255)

    Returns:
        float: Relative luminance value (0.0-1.0)
    """
    # Convert to 0-1 range
    r_norm = r / RGB_MAX
    g_norm = g / RGB_MAX
    b_norm = b / RGB_MAX

    # Apply gamma correction (WCAG formula)
    def gamma_correct(channel):
        if channel <= GAMMA_THRESHOLD:
            return channel / GAMMA_DIVISOR
        else:
            return ((channel + GAMMA_OFFSET) / GAMMA_MULTIPLIER) ** GAMMA_EXPONENT

    r_linear = gamma_correct(r_norm)
    g_linear = gamma_correct(g_norm)
    b_linear = gamma_correct(b_norm)

    # Calculate luminance using WCAG coefficients
    luminance = (
        RED_LUMINANCE_COEFFICIENT * r_linear
        + GREEN_LUMINANCE_COEFFICIENT * g_linear
        + BLUE_LUMINANCE_COEFFICIENT * b_linear
    )
    return luminance


def simulate_colorblindness(r: int, g: int, b: int, condition: str) -> tuple:
    """
    Simulate how colors appear with different types of colorblindness.
    Uses simplified transformations for educational purposes.

    Examples:
        >>> simulate_colorblindness(255, 128, 64, "protanopia")
        (191, 191, 64)
        >>> simulate_colorblindness(255, 128, 64, "deuteranopia")
        (223, 223, 64)
        >>> simulate_colorblindness(255, 128, 64, "tritanopia")
        (255, 128, 96)

    Arguments:
        r (int): Red component (0-255)
        g (int): Green component (0-255)
        b (int): Blue component (0-255)
        condition (str): "protanopia", "deuteranopia", or "tritanopia"

    Returns:
        tuple: (r, g, b) values as perceived by colorblind person
    """
    if condition == PROTANOPIA:
        # Red-green colorblind (missing L-cones): blend red and green
        new_rg = int((r + g) / 2)
        return (new_rg, new_rg, b)
    elif condition == DEUTERANOPIA:
        # Red-green colorblind (missing M-cones): blend red and green differently
        new_rg = int((r * 0.75 + g * 0.25))
        return (new_rg, new_rg, b)
    elif condition == TRITANOPIA:
        # Blue-yellow colorblind (missing S-cones): blend blue with others
        new_b = int((g + b) / 2)
        return (r, g, new_b)
    else:
        # Unknown condition, return original
        return (r, g, b)

# Student - you will start implementing each function below
# Remember, you need to have at least six (6) examples in the doctests. 
# this is meant to encourage you to think through the function
# before coding. 

def contrast_ratio(fg_r: int, fg_g: int, fg_b: int, 
                   bg_r: int, bg_g: int, bg_b: int) -> float:
    """
    Calculate contrast ratio between foreground and background colors.

    Implementation:
    The contrast ratio is calculated using WCAG standards. First, calculate the relative
    luminance for both colors using the calculate_luminance() function. Then apply the
    WCAG contrast formula: (L1 + 0.05) / (L2 + 0.05), where L1 is the luminance of
    the lighter color and L2 is the luminance of the darker color. You'll need to
    determine which color is lighter and ensure it's used as the numerator.

    Examples:
        >>> round(contrast_ratio(0, 0, 0, 255, 255, 255), 1)
        21.0
        >>> round(contrast_ratio(255, 255, 255, 255, 255, 255), 1)
        1.0
        >>> round(contrast_ratio(128, 128, 128, 255, 255, 255), 1)
        3.9

    In the examples, the round is used to make the returned result easier to compare.
    As a student you are free to use that for your example. 

    Arguments:
        fg_r (int): Foreground red (0-255)
        fg_g (int): Foreground green (0-255)
        fg_b (int): Foreground blue (0-255)
        bg_r (int): Background red (0-255)
        bg_g (int): Background green (0-255)
        bg_b (int): Background blue (0-255)

    Returns:
        float: Contrast ratio (1.0-21.0)
    """
    return 0 # replace

def passes_wcag_level(ratio: float, level: str) -> bool:
    """
    Check if contrast ratio meets WCAG standards.

    Implementation:
    Use conditional statements to check the input level string against the defined
    WCAG level constants. For each level, compare the ratio against the appropriate
    threshold constant. Return True if the ratio meets or exceeds the threshold,
    False otherwise. Handle unknown level strings by returning False.

    Examples:
        >>> passes_wcag_level(4.5, "AA_NORMAL")
        True
        >>> passes_wcag_level(4.0, "AA_NORMAL")
        False
        >>> passes_wcag_level(7.0, "AAA_NORMAL")
        True

    Arguments:
        ratio (float): Contrast ratio to check
        level (str): WCAG level ("AA_NORMAL", "AA_LARGE", "AAA_NORMAL", "AAA_LARGE")

    Returns:
        bool: True if ratio meets the specified level
    """
    return False # replace with your code


def calculate_brightness(r: int, g: int, b: int) -> int:
    """
    Calculate perceived brightness of a color.

    Implementation:
    Use the standard luminance formula but return the result as an integer from 0-255.
    The formula weights the RGB components differently because human eyes are more
    sensitive to green than red, and more sensitive to red than blue. Multiply each
    RGB component by its coefficient, sum them, and convert to integer. Use the
    brightness coefficient constants defined at the top of the file.

    Examples:
        >>> calculate_brightness(255, 255, 255)
        255
        >>> calculate_brightness(0, 0, 0)
        0
        >>> calculate_brightness(255, 0, 0)
        76

    Arguments:
        r (int): Red component (0-255)
        g (int): Green component (0-255)
        b (int): Blue component (0-255)

    Returns:
        int: Perceived brightness (0-255)
    """
    return 0 # replace


def recommend_adjustment(current_ratio: float, target_ratio: float) -> str:
    """
    Suggest how to improve contrast ratio.

    Implementation:
    Calculate the gap (target_ratio - current_ratio). Use conditional
    statements to categorize the gap: if current >= target, success; if gap <= 1.5,
    minor improvement needed; if gap > 1.5, major improvement needed. The threshold
    of 1.5 represents the boundary between minor and major adjustments. Return
    specific recommendation strings for each category.

    Examples:
        >>> recommend_adjustment(3.0, 4.5)
        'Increase contrast by making colors more different'
        >>> recommend_adjustment(5.0, 4.5)
        'Contrast ratio already meets target'
        >>> recommend_adjustment(2.0, 7.0)
        'Significant contrast improvement needed - consider much darker or lighter colors'

    Arguments:
        current_ratio (float): Current contrast ratio
        target_ratio (float): Desired contrast ratio

    Returns:
        str: Recommendation message
    """
    improvement_threshold = 1.5
    return '' # replace with your code


def find_minimum_brightness_steps(r: int, g: int, b: int, min_brightness: int) -> int:
    """
    Count steps needed to reach minimum brightness by incrementing RGB values equally.
    Uses while loop to increase brightness until threshold is met.

    Implementation:
    First check if the color is already bright enough using calculate_brightness().
    If so, return 0. Otherwise, use a while loop to increment all three RGB values
    by RGB_INCREMENT each iteration (but don't exceed 255). Count each iteration as a step.
    Continue until calculate_brightness() returns a value >= min_brightness. Include
    a safety check to prevent infinite loops when the target can't be reached.

    Examples:
        >>> find_minimum_brightness_steps(0, 0, 0, 50)
        50
        >>> find_minimum_brightness_steps(100, 100, 100, 50)
        0
        >>> find_minimum_brightness_steps(10, 20, 30, 100)
        82

    Arguments:
        r, g, b (int): Current RGB values
        min_brightness (int): Minimum brightness target (0-255)

    Returns:
        int: Number of steps needed (0 if already bright enough)
    """
    return 0 # replace with your code


def calculate_contrast_with_grays(color_r: int, color_g: int, color_b: int) -> int:
    """
    Find how many gray levels (0, 5, 10, 15... 255) meet AA contrast standards.
    Uses while loop to test gray values from 0 to 255 in steps of 5.

    Implementation:
    Initialize a counter and a gray value variable. Use a while loop to iterate
    through gray levels from 0 to 255 in steps of 5. For each gray level, create
    a gray color by using the same value for R, G, and B components. Calculate the
    contrast ratio between the input color and this gray using contrast_ratio().
    If the ratio meets AA standards (4.5:1), increment your counter. Return the
    total count of passing gray levels.

    Examples:
        >>> calculate_contrast_with_grays(0, 0, 0)
        28
        >>> calculate_contrast_with_grays(255, 255, 255)
        24
        >>> calculate_contrast_with_grays(128, 128, 128)
        5

    Arguments:
        color_r, color_g, color_b (int): RGB values of the test color

    Returns:
        int: Count of gray levels that provide AA contrast (4.5:1 or better)
    """
    passing_count = 0
    # add your code
    return passing_count


def find_accessible_gray_background(text_r: int, text_g: int, text_b: int) -> int:
    """
    Find the darkest gray background that still provides AA contrast with given text.
    Uses while loop to test gray values starting from white (255).

    Implementation:
    Start with the lightest gray (255) and work toward darker values (0). Use a
    while loop to decrement the gray value. For each gray level, calculate the
    contrast ratio with the text color using contrast_ratio(). Keep track of the
    darkest gray that still provides AA contrast (4.5:1). The key insight is that
    you want the darkest valid option, so continue testing even after finding
    valid grays. Return the darkest gray that meets the standard.

    Examples:
        >>> find_accessible_gray_background(0, 0, 0)
        117
        >>> find_accessible_gray_background(255, 255, 255)
        0
        >>> find_accessible_gray_background(100, 100, 100)
        225

    Arguments:
        text_r, text_g, text_b (int): RGB values of the text color

    Returns:
        int: Darkest gray value (0-255) that provides AA contrast, or 255 if none work
    """
    return 0 # replace


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
