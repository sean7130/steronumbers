# code works
import stero_numbers

if __name__ == "__main__":
    stero_numbers.OFFSET = (stero_numbers.FONT_SPACING // 5)
    stero_numbers.generate_numbers([1,5,3,7,9,9,3,1,8,7])
    # stero_numbers.image.show()
