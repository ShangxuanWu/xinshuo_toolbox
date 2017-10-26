% Author: Xinshuo Weng
% email: xinshuo.weng@gmail.com

% compute essential matrix from fudamental matrix after calibration
%	det(E) = 0
% 	2EE'E - trace(EE')E = 0
function E = compute_E_from_F_calibrated(F, K1, K2, debug_mode);
	if nargin < 4
		debug_mode = true;
	end

	epsilon = 1e-5;
	if debug_mode
		assert(all(size(F) == [3, 3]), 'the input fudamental matrix does not have a good shape');
		assert(all(size(K1) == [3, 3]), 'the input intrinsic matrix1 does not have a good shape');
		assert(all(size(K2) == [3, 3]), 'the input intrinsic matrix2 does not have a good shape');
		assert(isUpper(K1) && isUpper(K2), 'the input intrinsic matrix is not upper triangular');
		assert(det(F) < epsilon, 'the determinant of fundamental matrix is not close to 0')
	end

	E = K2' * F * K1;

	det(E)
	2 * E * E' * E - trace(E * E') * E
	svd(E)
	pause;
end