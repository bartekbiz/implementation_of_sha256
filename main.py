
def translate_string_to_bits(message):
    # string characters to unicode values
    charcodes = [ord(c) for c in message]
    # unicode values to 8-bit strings (removed binary indicator)
    bytes_array = []
    for char in charcodes:
        bytes_array.append(bin(char)[2:].zfill(8))
    # 8-bit strings to list of bits as integers
    bits = []
    for byte in bytes_array:
        for bit in byte:
            bits.append(int(bit))
    return bits


def binary_to_hexadecimal(value):
    # takes list of 32 bits
    # convert to string
    value = ''.join([str(x) for x in value])

    # creat 4 bit chunks, and add bin-indicator
    binaries = []
    for d in range(0, len(value), 4):
        binaries.append('0b' + value[d:d+4])

    # transform to hexadecimal and remove hex-indicator
    hexes = ''

    for b in binaries:
        hexes += hex(int(b, 2))[2:]

    return hexes


# Helper functions
def fill_zeros(bits, required_len=8, append=True):
    bits_len = len(bits)
    if append is True:
        for i in range(bits_len, required_len):
            bits.append(0)
    else:
        while bits_len < required_len:
            bits.insert(0, 0)
            bits_len = len(bits)
    return bits


def chunker(bits, chunk_size=8):
    # divides list of bits into desired byte/word chunks,
    # starting at LSB
    chunked_bits = []
    for p in range(0, len(bits), chunk_size):
        chunked_bits.append(bits[p:p + chunk_size])
    return chunked_bits


print(translate_string_to_bits("XO"))
print(binary_to_hexadecimal([0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1]))
