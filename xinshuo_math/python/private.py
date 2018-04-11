# Author: Xinshuo Weng
# email: xinshuo.weng@gmail.com

# this file includes private functions for internal use only
import numpy as np

from xinshuo_miscellaneous import islist, isnparray, isbbox

def safe_npdata(input_data):
	'''
	copy a list of data or a numpy data to the buffer for use

	parameters:
		input_data:		a list or numpy data

	outputs:
		np_data:		a copy of numpy data
	'''
	if islist(input_data):
		np_data = np.array(input_data)
	elif isnparray(input_data):
		np_data = input_data.copy()
	else:
		assert False, 'only list of data and numpy data are supported'

	return np_data

def safe_bbox(input_bbox, debug=True):
	'''
	make sure to copy the bbox without modifying it and make the dimension to N x 4

	parameters:
		input_bbox: 	a list of 4 elements, a numpy array with shape or (N, 4) or (4, )

	outputs:
		np_bboxes:		N X 4 numpy array
	'''
	if islist(input_bbox):
		if debug:
			assert len(input_bbox) == 4, 'the input bbox list does not have a good shape'
		np_bboxes = np.array(input_bbox).reshape((1, 4))
	elif isnparray(input_bbox):
		input_bbox = input_bbox.copy()
		if input_bbox.shape == (4, ):
			np_bboxes = input_bbox.reshape((1, 4))
		else:
			if debug:
				assert isbbox(input_bbox), 'the input bbox numpy array does not have a good shape'
			np_bboxes = input_bbox
	else:
		assert False, 'only list and numpy array for bbox are supported'

	return np_bboxes

def bboxcheck_TLBR(input_bbox, debug=True):
    '''
    check the input bounding box to be TLBR format

    parameters:
        input_bbox:   TLBR format, a list of 4 elements, a numpy array with shape or (N, 4) or (4, )
    
    outputs:
        True if the x2 > x1 and y2 > y1
    '''
    np_bboxes = safe_bbox(input_bbox, debug=debug)
    if debug:
        assert isbbox(np_bboxes), 'the input bboxes are not good'

    return (np_bboxes[:, 3] >= np_bboxes[:, 1]).all() and (np_bboxes[:, 2] >= np_bboxes[:, 0]).all()      # coordinate of bottom right point should be larger or equal than top left point

def bboxcheck_TLWH(input_bbox, debug=True):
    '''
    check the input bounding box to be TLBR format

    parameters:
        input_bbox:   TLBR format, a list of 4 elements, a numpy array with shape or (N, 4) or (4, )
    
    outputs:
        True if the width and height are >= 0
    '''
    np_bboxes = safe_bbox(input_bbox, debug=debug)
    if debug:
        assert isbbox(np_bboxes), 'the input bboxes are not good'

    return (np_bboxes[:, 3] >= 0).all() and (np_bboxes[:, 2] >= 0).all()      # coordinate of bottom right point should be larger or equal than top left point