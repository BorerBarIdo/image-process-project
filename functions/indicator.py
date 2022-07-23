def indicator(img, px, py):
    img[px-5: px+5, py-5: py+5, 1] = 1
    # img[px + 1][py + 1] = (255, 0, 0)
    # img[px][py + 1] = (255, 0, 0)
    # img[px - 1][py] = (255, 0, 0)
    # img[px - 1][py - 1] = (255, 0, 0)
    # img[px][py - 1] = (255, 0, 0)
    # img[50:75, 50:75, 0] = 0
    # img[50:75, 50:75, 1] = 0
    return img
