import numpy as np
from PIL import Image

def get_random_eraser(p=0.5, sl=0.02, sh=0.4, r1=0.3, r2=1/0.3, vl=0, vh=255, mode='IRE'):
	def calc(row, col, h, w):
		while True:
			se = np.random.uniform(sl, sh) * h * w
			re = np.random.uniform(r1, r2)
			we = int(np.sqrt(se / re))
			he = int(np.sqrt(se * re))
			left = np.random.randint(col, col+w)
			top = np.random.randint(row, row+h)

			if left + we <= col + w and top + he <= row + h:
				return (top, left, he, we)

	def eraser(input_img: str, input_bbox: str = None):
		img = np.array(Image.open(input_img))
		img_h, img_w, img_c = img.shape

		p1 = np.random.rand()
		if p1 > p:
			return img
		else:
			if mode == 'IRE' or mode == 'I+ORE':
				top, left, he, we = calc(0, 0, img_h, img_w)
				img[top:top+he, left:left+we] = np.random.uniform(vl, vh, (he, we, img_c))

			if mode == 'ORE' or mode == 'I+ORE':
				if input_bbox == None:
					raise Exception('must input bbox txt file')
				with open(input_bbox, 'r') as f:
					bbox = [list(map(float, i.split(' '))) for i in f.readlines()]
					for i in bbox:
						i[3] = int(i[3] * img_w)
						i[4] = int(i[4] * img_h)

						i[1] = int(i[1] * img_w - i[3] / 2)
						i[2] = int(i[2] * img_h - i[4] / 2)
						top, left, he, we = calc(i[2], i[1], i[4], i[3])
						img[top:top+he, left:left+we] = np.random.uniform(vl, vh, (he, we, img_c))

			return img
	return eraser
