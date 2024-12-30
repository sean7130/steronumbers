from PIL import Image, ImageDraw, ImageFont

# SOURCE_FILE = "stero_numbers_text_to_encode"
SOURCE_FILE = "pi200"

FONT_SPACING = 10
COL_SPACING = FONT_SPACING*10 - 3
ROW_SPACING = 25

OFFSET = FONT_SPACING // 10

width, height = 600, 400 
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

font_path = "arial.ttf"  # Replace with the path to the Arial font file on your system
font_size = 36
font = ImageFont.truetype(font_path, font_size)

################### redefiniton function of draw and image ################### 
# this function will create a new `image` and `draw` variable (which is      #
# global) based on a desired new width and height                            #
#                                                                            #
# once width and height has been redefined, the draw and image variabe       #
# will need to be regenerated to take change of the update                   #
##############################################################################
def redefine_image_and_draw(w, h):
    global image, draw, width, height
    width = w
    height = h
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

def get_img_dim():
    return width, height

def extract_source():
    fd = open(SOURCE_FILE, "r")
    ret = fd.readlines()
    return ret[0].strip()

# by default, this generate offset will generate no additional stero 
# information in the last col of each row, this is done to add visiblity
def generate_offset(numbers, padding_at_the_end=True):
    char_idx = 0
    offset = []
    curr_number = int(numbers[char_idx])
    for row in range(height // ROW_SPACING):
        this_row = []
        this_col = [0 for _ in range(10)]
        for col in range(width // COL_SPACING - 1 - int(padding_at_the_end)):
            this_col = this_col.copy()
            offset_pointer = -1
            while curr_number > offset_pointer:
                offset_pointer = curr_number
                this_col[offset_pointer] += 1
                char_idx += 1
                if char_idx == len(numbers):
                    this_row.append(this_col)
                    offset.append(this_row)
                    return offset
                curr_number = int(numbers[char_idx])
            this_row.append(this_col)
        if padding_at_the_end:
            this_row.append(this_col.copy())
        offset.append(this_row)
    print(f"WARN: Cutoff hit, char_idx={char_idx}")
    return offset

def fill_last_row(unfinished):
    while len(unfinished[-1]) < len(unfinished[0]):
        unfinished[-1].append(unfinished[-1][-1].copy())

def grad_pink_to_green(num):
    return (200- num*18, 100 + num*10, 200-num*18)

def grad_glacier(num):
    return (149- int((149/9*num)), 114+int(56/9*num), 255)

def grad_none(num): # pure black
    return (0, 0, 0)

def grad_hue(num):
    return [
        (255, 0, 0),      # Red
        (255, 102, 0),    # Orange
        (255, 204, 0),    # Golden Yellow
        (170, 255, 0),    # Yellow-Green
        (0, 255, 85),     # Green
        (0, 255, 255),    # Cyan-Green
        (0, 170, 255),    # Cyan-Blue
        (0, 85, 255),     # Blue
        (85, 0, 255),     # Violet
        (170, 0, 255)     # Magenta
    ][num]


def grad_bg(num):
    if num%2:
        return (100, 100, 100)
    return (0, 0, 0)


def generate_gradient_preview_image(gradient=grad_none):
    """ 
    this is not the function that creates the sterogram:
    this function is intended to generate just one line of number to preview
    a gradient
    """
    col_repeat = 3
    required_width = (col_repeat-1)*COL_SPACING + 9*FONT_SPACING + 15
    grad_preview = Image.new("RGB", (required_width, 40), (240,240,240))
    grad_preview_draw = ImageDraw.Draw(grad_preview)
    for col in range(col_repeat):
        for num in range(10):
            color = gradient(num)
            # I removed the offset and row spacing, they are not needed for preview
            grad_preview_draw.text((FONT_SPACING * num + COL_SPACING * (col), 
                                    0), str(num), font=font, fill=color)
    grad_preview.save("gradient_preview.png")

def draw_dummy_first_column(row_num, norm_val):
    for num in range(10):
        color = STERO_COLOR_GRADIENT(num)
        draw.text((FONT_SPACING * num + norm_val * OFFSET, row_num*ROW_SPACING), 
                  str(num), 
                  font=font, 
                  fill=color)

def approx(val):
    floor = int(val)
    if val - floor > 0.5:
        return floor + 1
    return floor

def update_row_with_norm_val(row, norm_val):
    for col in row:
        for i in range(len(col)):
            col[i] -= norm_val
    row.append(norm_val)

def normalize_offset(offset, method="default"):
    if method == "end":
        for row in offset: 
            norm_val = (row[-1][-1]//2)
            update_row_with_norm_val(row, norm_val)
    else: 
        elements_per_row = len(offset[0]) * len(offset[0][0])
        for row in offset:
            total = 0
            for col in row:
                total += sum(col)
            norm_val = approx(total/elements_per_row)
            # print(f"average value for row: "
            #      f"{total/elements_per_row}->{norm_val} "
            #      f"sums: before={total}, after{total-norm_val*elements_per_row}")
            update_row_with_norm_val(row, norm_val)

def encode_numbers(numbers, filename="preview.png"):
    draw.rectangle((0, 0, width, height), fill=(240,240,240))
    offset = generate_offset(numbers)
    if len(offset[0]) != len(offset[-1]):
        fill_last_row(offset)

    # This will add another (int) element at the ending of each row, denoting how many
    # values have been subtrated from orgional offset during normazation
    normalize_offset(offset, method="end")

    # check if normalization has been added, otherwise add another dummy norm
    # for consistency
    if type(offset[0][-1]) != type(0):
        for row in offset:
            row.append(0)

    # for row in offset:
    #     print(row[-1])

    for row in range(len(offset)):
        draw_dummy_first_column(row, offset[row][-1])
        for col in range(len(offset[row]) - 1): # last item in row is not a list item
            for num in range(10):
                # draw.text((FONT_SPACING * num + COL_SPACING * (col+1) - offset[row][col][num] * OFFSET, 
                #            row*ROW_SPACING), str(num), font=font, fill="black")
                color = STERO_COLOR_GRADIENT(num)
                draw.text((FONT_SPACING * num + COL_SPACING * (col+1) - offset[row][col][num] * OFFSET, 
                           row*ROW_SPACING), str(num), font=font, fill=color)

    image.save(filename)

STERO_COLOR_GRADIENT = grad_pink_to_green

if __name__ == "__main__":
 
    numbers = extract_source()
    encode_numbers(numbers)

    # run_example()
    # image.show()
